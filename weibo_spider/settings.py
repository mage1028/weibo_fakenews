# -*- coding: utf-8 -*-

# Scrapy settings for weibo_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo_spider'

SPIDER_MODULES = ['weibo_spider.spiders']
NEWSPIDER_MODULE = 'weibo_spider.spiders'

DOWNLOADER_MIDDLEWARES = {
    # 'weibo_spider.middlewares.Random_cookies': 401,
    'weibo_spider.middlewares.Random_UA': 401,
    'weibo_spider.middlewares.CookiesMiddleware': 400,

}
FEED_EXPORT_ENCODING = 'utf-8'

# redis配置

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# #去重过滤器
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# LOG_ENABLED = True
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'weibo_spider.middlewares.WeiboFakenewsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'weibo_spider.middlewares.WeiboFakenewsDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'weibo_spider.pipelines.WeiboFakenewsPipeline': 999,
    'scrapy_redis.pipelines.RedisPipeline': 300,
    'weibo_spider.pipelines.WeiboImgDownloadPipeline': 800,
}

REDIS_URL = 'redis://@localhost:6379'
#
#
# LOG_FILE = "/hbasestorage/spider/spider_logs/fakenews_weibo/scrapy.log"
# LOG_FILE = "/hbasestorage/spider/spider_logs/fakenews_weibo/scrapy2.log"

# IMAGES_STORE = '/hbasestorage/spider/spider_2018_2_files/flightgirl_weibo/images'
DEFAULT_REQUEST_HEADERS = {
    #   SINAGLOBAL=2548624436092.2637.1577608974270; login_sid_t=d151efbff5bb1496d6de7d5fdb0946e2; cross_origin_proto=SSL; _s_tentry=-; Apache=1188468703273.8105.1588270614259; ULV=1588270614266:6:1:1:1188468703273.8105.1588270614259:1586852654132; S_ACCOUNT-G0=a1c00fe9e544064d664e61096bd4d187; SSOLoginState=1590326292; un=18066635323; SCF=AstiSN-bn44ABUkezJ24AlMbj2H1nEzWxoZ6jtf_UbI5xxBzxs5LQqloqBUtKEP4Jd59tBGBwjgEa9lQ4AjBJ0Q.; SUB=_2A25z-G6VDeRhGeVJ7FoV-S_Jzj6IHXVQjMddrDV8PUJbmtANLWHhkW9NT8RACzCXaJX-JPEraElrzOP4Dfnkd_4N; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW98Vb6BMxbNWLW24e2R0L55JpX5K-hUgL.FoeNS0nX1K2fSKz2dJLoI0qLxKnLBKzLB-zLxK.L1KBLBKBLxKqL1K.L1K-LxKML1-2L1hBLxK-LBo5L12qLxK.LBonLBK2t; SUHB=0jB4_VGTqCnOqg; ALF=1625117251; wvr=6; UOR=,,login.sina.com.cn; WBStorage=42212210b087ca50|undefined; webim_unReadCount=%7B%22time%22%3A1593587454442%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D
    "cookie": "SINAGLOBAL=2548624436092.2637.1577608974270; login_sid_t=d151efbff5bb1496d6de7d5fdb0946e2; cross_origin_proto=SSL; Ugrow-G0=6fd5dedc9d0f894fec342d051b79679e; YF-V5-G0=99df5c1ecdf13307fb538c7e59e9bc9d; _s_tentry=-; Apache=1188468703273.8105.1588270614259; ULV=1588270614266:6:1:1:1188468703273.8105.1588270614259:1586852654132; WBtopGlobal_register_version=fd6b3a12bb72ffed; SSOLoginState=1590326292; un=18066635323; UOR=,,login.sina.com.cn; TC-Page-G0=e1a5a1aae05361d646241e28c550f987|1594208910|1594208905; TC-V5-G0=595b7637c272b28fccec3e9d529f251a; lang=zh-tw; _ga=GA1.2.1108465334.1594298316; _gid=GA1.2.14011703.1594298316; _gat=1; _gat_AllWeiboTracker=1; WBStorage=42212210b087ca50|undefined; Hm_lvt_50f34491c9065a59f87d0d334df29fa4=1594298317; Hm_lpvt_50f34491c9065a59f87d0d334df29fa4=1594298317; __gads=ID=057bbbdf4f39d869:T=1594298317:S=ALNI_MZXzpYkYhy9YmZQ7UllcHPf5in0Bw; wb_view_log=1792*11202; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW98Vb6BMxbNWLW24e2R0L55JpX5K2hUgL.FoeNS0nX1K2fSKz2dJLoI0qLxKnLBKzLB-zLxK.L1KBLBKBLxKqL1K.L1K-LxKML1-2L1hBLxK-LBo5L12qLxK.LBonLBK2t; ALF=1625834345; SCF=AstiSN-bn44ABUkezJ24AlMbj2H1nEzWxoZ6jtf_UbI5vo7-k09DMQE1uZUJ3rjcOpqzKkzZey_UXfkadoqYYtE.; SUB=_2A25yA3-6DeRhGeVJ7FoV-S_Jzj6IHXVRedZyrDV8PUNbmtANLWLMkW9NT8RAC5pfoKH8bjqNODSMnAjWvmk5EJI6; SUHB=0idbCUuftxOw0z; wvr=6; wb_view_log_3778491552=1792*11202; YF-Page-G0=761bd8cde5c9cef594414e10263abf81|1594298359|1594298359; webim_unReadCount=%7B%22time%22%3A1594298361063%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Language': "zh-CN,zh;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Host": "service.account.weibo.com",
    'Content-Type': 'application/x-www-form-urlencoded'
}
