import json
import base64
import requests
import redis
import logging
from weibo_spider.db.mysql_insert import insert_cookie
import json
logger = logging.getLogger(__name__)
# reds=redis.Redis.from_url(REDIS_URL,db=,decode_response=True)

myWeiBo = [
    {'no': '18066635323', 'psw': 'seaways220'},
    {'no': '16144606536', 'psw': 'add38853G'},
    {'no': '13859991449', 'psw': 'axd81075D'},
    {'no': '16417933166', 'psw': 'agd11070L'},
    {'no': '18813663191', 'psw': 'axd88201w'},
    {'no': '17887004042', 'psw': 'aCd70552m'},

]


def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']
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
            cookie = [session.cookies.get_dict(), elem['no']]
            cookies.append(cookie)

        else:
            print("Failed!( Reason:%s )" % info["reason"].encode("utf-8"))
    print('ojbk!!!!!!!!!!!!')
    return cookies

def getoneCookies(account,password):
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

    pass
