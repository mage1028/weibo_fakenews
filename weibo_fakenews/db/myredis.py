import redis
from weibo_fakenews.login.login1 import getoneCookies
import time
import json
import logging
import scrapy
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
    if account in r.hgetall('weibo_cookies'):
        return True


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
