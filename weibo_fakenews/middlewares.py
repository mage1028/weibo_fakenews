# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy import signals
from fakenews.data import agents
import re
import json
from fakenews.db.myredis import del_cookie, getall_cookies,end_spider

class CookiesMiddleware(object):
    def process_request(self, request, spider):
        url = request.url
        if re.findall(r'//weibo.com/login', url):
            cookie = json.dumps(request.cookies)
            del_cookie(cookie)
            request=request.replace(url=request.meta['redirect_urls'][0])
        if re.findall(r'//login.sina', url):
            cookie = json.dumps(request.cookies)
            del_cookie(cookie)
            request = request.replace(url=request.meta['redirect_urls'][0])
        if re.findall(r'//weibo.com/signup', url):
            cookie = json.dumps(request.cookies)
            del_cookie(cookie)
            request = request.replace(url=request.meta['redirect_urls'][0])
        end_spider()
        cookies = getall_cookies()
        cookie = random.choice(cookies)
        request.cookies = cookie


class Random_UA(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(agents)
        request.headers.setdefault('User-Agent', ua)


# #
# class WeiboFakenewsSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class WeiboFakenewsDownloaderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#
#         return None
#
#     def process_response(self, request, response, spider):
#
#         # 删除无效cookie
#
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
