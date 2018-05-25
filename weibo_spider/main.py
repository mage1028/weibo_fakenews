#!/usr/bin/python
# -*- coding: UTF-8 -*-
from scrapy import cmdline

if __name__ == '__main__':

    cmdline.execute("scrapy crawl weibo_spider".split())
