from scrapy import cmdline
from weibo_fakenews.db.myredis import fresh_cookie

if __name__ == '__main__':
    fresh_cookie()

    cmdline.execute("scrapy crawl weibo_fakenews".split())
