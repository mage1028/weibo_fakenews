# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy import signals
from weibo_spider.data import agents
import re
import json
from weibo_spider.db.myredis import del_cookie, getall_cookies, end_spider


class CookiesMiddleware(object):
    def process_request(self, request, spider):
        pass
        # url = request.url
        # if re.findall(r'//weibo.com/login', url):
        #     cookie = json.dumps(request.cookies)
        #     del_cookie(cookie)
        # if re.findall(r'//login.sina', url):
        #     cookie = json.dumps(request.cookies)
        #     del_cookie(cookie)
        # if re.findall(r'//weibo.com/signup', url):
        #     cookie = json.dumps(request.cookies)
        #     del_cookie(cookie)
        # end_spider()
        # cookies = getall_cookies()
        # cookie = random.choice(cookies)
        # request.cookies = cookie
        
        # cookie="SINAGLOBAL=2548624436092.2637.1577608974270; login_sid_t=d151efbff5bb1496d6de7d5fdb0946e2; cross_origin_proto=SSL; _s_tentry=-; Apache=1188468703273.8105.1588270614259; ULV=1588270614266:6:1:1:1188468703273.8105.1588270614259:1586852654132; SSOLoginState=1590326292; un=18066635323; SCF=AstiSN-bn44ABUkezJ24AlMbj2H1nEzWxoZ6jtf_UbI5xxBzxs5LQqloqBUtKEP4Jd59tBGBwjgEa9lQ4AjBJ0Q.; SUB=_2A25z-G6VDeRhGeVJ7FoV-S_Jzj6IHXVQjMddrDV8PUJbmtANLWHhkW9NT8RACzCXaJX-JPEraElrzOP4Dfnkd_4N; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW98Vb6BMxbNWLW24e2R0L55JpX5K-hUgL.FoeNS0nX1K2fSKz2dJLoI0qLxKnLBKzLB-zLxK.L1KBLBKBLxKqL1K.L1K-LxKML1-2L1hBLxK-LBo5L12qLxK.LBonLBK2t; SUHB=0jB4_VGTqCnOqg; ALF=1625117251; wvr=6; UOR=,,login.sina.com.cn; webim_unReadCount=%7B%22time%22%3A1593586099318%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D"        
        # request.headers.setdefault("cookie",cookie)



class Random_UA(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(agents)
        request.headers.setdefault('User-Agent', ua)

