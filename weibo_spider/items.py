# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboFakenewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    informers = scrapy.Field()
    informants = scrapy.Field()
    informants_id = scrapy.Field()
    informers_content = scrapy.Field()
    content = scrapy.Field()

    forwarded_count = scrapy.Field()
    comment_count = scrapy.Field()
    like_count = scrapy.Field()
    informers_count = scrapy.Field()
    informants_time = scrapy.Field()
    reason = scrapy.Field()
    url = scrapy.Field()

    pass


class CommentsItem(scrapy.Item):
    author = scrapy.Field()
    author_comment = scrapy.Field()
    flag = scrapy.Field()
    like_count = scrapy.Field()
    id = scrapy.Field()
    time = scrapy.Field()


class AuthorItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    follow_count = scrapy.Field()
    follower_count = scrapy.Field()
    weibo_count = scrapy.Field()
    verified = scrapy.Field()
    rank = scrapy.Field()
    description = scrapy.Field()


class WeiboItem(scrapy.Item):
    id = scrapy.Field()
    author = scrapy.Field()
    author_id = scrapy.Field()
    content = scrapy.Field()

    like_count = scrapy.Field()
    forwarded_count = scrapy.Field()
    comment_count = scrapy.Field()

    device = scrapy.Field()

    time = scrapy.Field()


class ImageItem(scrapy.Field):
    image_url = scrapy.Field()
    image_name = scrapy.Field()
