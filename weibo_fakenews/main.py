from scrapy import cmdline
from fakenews.db.myredis import fresh_cookie
if __name__ == '__main__':
    fresh_cookie()
    cmdline.execute("scrapy crawl fakenews".split())
