from scrapy import cmdline
from weibo_spider.db.myredis import fresh_cookie

if __name__ == '__main__':
    fresh_cookie()

    cmdline.execute("scrapy crawl weibo_spider".split())
