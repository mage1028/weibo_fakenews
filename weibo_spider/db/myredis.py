#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
import requests
import redis

import json
import logging

from scrapy.exceptions import CloseSpider


def connect():
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r


def insert_account(account, pwd):
    r = connect()
    try:
        r.hmset('weibo_account', {account: pwd})
    except Exception as e:
        print(e)


def select_account(account):
    r = connect()
    pwd = r.hmget('weibo_account', '{0}'.format(account))[0]

    return pwd


def insert_cookie(account):
    r = connect()
    pwd = select_account(account)

    cookie = getoneCookies(account, pwd)[0]
    cookie = json.dumps(cookie)
    r.hmset('weibo_cookies', {account: cookie})


def fresh_cookie():
    r = connect()
    accounts = r.hgetall('weibo_account')
    for account in accounts:
        if not testcookie(account):
            insert_cookie(account)


def del_cookie(cookie):
    r = connect()
    accounts = r.hgetall('weibo_cookies')
    for account in accounts:
        if r.hget('weibo_cookies', account) == cookie:
            r.hdel('weibo_cookies', account)
            logging.exception('已删除无用cookie %s' % account)


def del_account(account):
    r = connect()
    r.hdel('weibo_account', account)


def testcookie(account):
    r = connect()
    try:
        if account in r.hgetall('weibo_cookies'):
            return True
    except:
        return False


def getall_cookies():
    r = connect()
    cookies = []
    accounts = r.hgetall('weibo_cookies')
    for account in accounts:
        cookies.append(json.loads(r.hget('weibo_cookies', account)))
    return cookies


def end_spider():
    r = connect()
    if r.hlen('weibo_cookies') == 0:
        raise CloseSpider('cookies用尽啦')


def getoneCookies(account, password):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
    postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    session = requests.Session()
    r = session.post(loginURL, data=postData)
    jsonStr = r.content.decode('gbk')
    info = json.loads(jsonStr)
    if info["retcode"] == "0":
        print("Get Cookie Success!( Account:%s )" % account)
        cookie = session.cookies.get_dict()
        cookies.append(cookie)
    else:
        print("Failed!( Reason:%s )" % info["reason"].encode("utf-8"))
    print('ojbk!!!!!!!!!!!!')
    return cookies


if __name__ == '__main__':
    fresh_cookie()

# def select_allcookie():
# insert_account('18066635323', 'seaways220')
# insert_account('16144606536', 'add38853G')
# insert_account('13859991449', 'axd81075D')
# insert_account('16417933166', 'agd11070L')异常
# insert_account('18813663191', 'axd88201w')异常
# insert_account('17887004042', 'aCd70552m')异常
# insert_account('13609249748','xuanbaobao')
