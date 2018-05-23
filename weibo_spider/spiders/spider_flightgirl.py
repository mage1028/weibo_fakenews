import scrapy
import re
from scrapy import Request
from weibo_spider.items import *
import time
import math
import json
from scrapy.selector import Selector
from weibo_spider.spiders.str import dealstr, dealcontent
import random

import logging


class FakenewsSpider(scrapy.Spider):
    name = 'flight_girl'
    start_urls = [
        'https://s.weibo.com/weibo/%25E7%25A9%25BA%25E5%25A7%2590%25E6%25BB%25B4%25E6%25BB%25B4&scope=ori&suball=1&timescope=custom:2018-05-10-0:2018-05-10-1&Refer=g']
    def parse(self, response):
        text=response.text
        html=re.findall(r'<script>[\s\S]*?</script>',text)[10].strip('<script>').stript('</script>')
