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
import copy
import logging


class FakenewsSpider(scrapy.Spider):
    name = 'flight_girl'
    urls = [
        'https://s.weibo.com/weibo/%25E7%25A9%25BA%25E5%25A7%2590%25E6%25BB%25B4%25E6%25BB%25B4&scope=ori&suball=1&timescope=custom:2018-05-10-0:2018-05-10-23&Refer=g&page=1']

    def start_requests(self):
        for url in self.urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        item_weibo = WeiboItem()
        item_author = AuthorItem()
        item_url = ImageItem()

        text = response.text
        page = int(re.findall(r'page=\d+', text)[-2].strip('page='))

        html = re.findall(r'<script>[\s\S]*?</script>', text)
        html = html[12].strip('<script>').strip('</script>')
        html = html.strip('STK && STK.pageletM && STK.pageletM.view(').strip(')')
        html = json.loads(html)['html']
        htmlcontents = Selector(text=html).xpath('//*[@class="WB_cardwrap S_bg2 clearfix"]').extract()
        for html in htmlcontents:
            author_name = Selector(text=html).xpath('//*[@class="feed_content wbcon"]/a/@nick-name').extract()[0]
            item_author['name'] = author_name
            item_weibo['author'] = author_name
            item_weibo['author_id'] = \
                Selector(text=html).xpath('//*[@class="feed_content wbcon"]/a/@usercard').extract()[0]

            item_author['id'] = re.findall(r'\d+', item_weibo['author_id'])[0]
            item_weibo['author_id'] = item_author['id']
            try:
                item_author['verified'] = \
                    Selector(text=html).xpath('//*[@class="feed_content wbcon"]/a/@alt').extract()[0]
            except:
                item_author['verified'] = '无认证'
            author_url = Selector(text=html).xpath('//*[@class="feed_content wbcon"]/a[@nick-name]/@href').extract()[0]
            weibo_url = Selector(text=html).xpath('//*[@class="feed_from W_textb"]/a[@suda-data]/@href').extract()[0]
            item_weibo['time'] = \
                Selector(text=html).xpath('//*[@class="feed_from W_textb"]/a[@suda-data]/@title').extract()[0]
            try:
                item_weibo['device'] = \
                    Selector(text=html).xpath('//*[@class="feed_from W_textb"]/a[@rel]/text()').extract()[0]
            except:
                item_weibo['device'] = '设备未显示'
            item_weibo['id'] = Selector(text=html).xpath('//*[@mid]/@mid').extract()[0]

            # 处理微博图片
            try:
                imgs = Selector(text=html).xpath('//*[@class="bigcursor"]/@src').extract()
                i = 1
                for image in imgs:
                    item_url['image_url'] = ('https:' + image).replace('thumbnail', 'bmiddle').replace('square',
                                                                                                       'bmiddle')
                    item_url['image_name'] = item_weibo['id'] + '-' + '{0}'.format(i)
                    i += 1
                    yield copy.deepcopy(item_url)
            except:
                pass

            yield Request(url='https:' + author_url, callback=self.parse_author,
                          meta={'item': copy.deepcopy(item_author)})
            yield Request(url='https:' + weibo_url, callback=self.parse_weibo, meta={'item': copy.deepcopy(item_weibo)})

        # 处理后面的几页
        url = response.url
        find_page = re.findall(r'page=\d+', url)[0]
        if find_page == 'page=1':
            for i in range(2, page + 1):
                newurl = url.replace(find_page, 'page={0}'.format(i))

                yield Request(url=newurl, callback=self.parse)

    def parse_author(self, response):
        text = response.text
        item = response.meta['item']

        author_data = re.findall(r'strong class=\\"W_f1\d\\">\d+<', text)
        front = re.findall(r'strong class=\\"W_f1\d\\">', author_data[0])[0]
        item['follow_count'] = author_data[0].strip(front).strip('<')
        if item['follow_count'] == '':
            item['follow_count'] = '0'
        front = re.findall(r'strong class=\\"W_f1\d\\">', author_data[1])[0]
        item['follower_count'] = author_data[1].strip(front).strip('<')
        if item['follower_count'] == '':
            item['follower_count'] = '0'
        front = re.findall(r'strong class=\\"W_f1\d\\">', author_data[2])[0]
        item['weibo_count'] = author_data[2].strip(front).strip('<')
        if item['weibo_count'] == '':
            item['weibo_count'] = '0'
        item['rank'] = re.findall(r'title=\\"微博等级\d+\\"', text)[0].strip('title=\\"微博等级').strip('\\"')

        item['description'] = response.xpath('//meta[@name="description"]/@content').extract()[0].strip(
            '新浪微博，随时随地分享身边的新鲜事儿。')
        yield copy.deepcopy(item)

    def parse_weibo(self, response):
        item = response.meta['item']
        text = response.text
        try:
            content = re.findall(r'WB_text [\s\S]*?div>', text)[0]

            # 处理详情内容字符串
            titles = re.findall('WB_text[\s\S]*?>', content)
            for title in titles:
                content = content.split(title)
                content = ''.join(content)
            content = content.rstrip('<\\/div>')
            item['content'] = dealstr(content)
        except Exception as e:
            logging.exception(e)

        # 处理赞，转发 ，评论
        try:
            forwarded_count = re.findall(r'<em>[\s\S]*?em>', text)[4].lstrip('<em>').split('<')[0]
            if forwarded_count == '转发':
                forwarded_count = '0'
            item['forwarded_count'] = forwarded_count
        except:
            forwarded_count = re.findall(r'<em>[\s\S]*?em>', text)[1].lstrip('<em>').split('<')[0]
            if forwarded_count == '转发':
                forwarded_count = '0'
            item['forwarded_count'] = forwarded_count
        try:
            comment_count = re.findall(r'<em>[\s\S]*?em>', text)[5].lstrip('<em>').split('<')[0]
            if comment_count == '评论':
                comment_count = '0'
            item['comment_count'] = comment_count
        except:
            comment_count = re.findall(r'<em>[\s\S]*?em>', text)[2].lstrip('<em>').split('<')[0]
            if comment_count == '评论':
                comment_count = '0'
            item['comment_count'] = comment_count
        try:
            like_count = re.findall(r'<em>[\s\S]*?em>', text)[6].lstrip('<em>').split('<')[0]
            if like_count == '赞':
                like_count = '0'
            item['like_count'] = like_count
        except:
            like_count = re.findall(r'<em>[\s\S]*?em>', text)[3].lstrip('<em>').split('<')[0]
            if like_count == '赞':
                like_count = '0'
            item['like_count'] = like_count

        # 处理url
        id = re.findall(r'mblog&act=\w+', text)[0].lstrip('mblog&act=')
        item['id'] = id

        # 处理时间戳 id page
        tick = time.time()
        rnd = int(tick * 1000)
        page_max1 = int(math.ceil(int(item['comment_count']) / 20))

        yield copy.deepcopy(item)

        # 找到所有评论和转发
        for i in range(1, page_max1 + 1):
            url_comment = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id={0}&page={1}&__rnd={2}'.format(id, i, rnd)
            yield Request(url=url_comment, callback=self.parse_comments,
                          meta={'id': item['id'], 'flag': 'comment'})
        page_max2 = int(math.ceil(int(item['forwarded_count']) / 20))

        for i in range(1, page_max2 + 1):
            url_forwarded = 'https://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id={0}&page={1}&__rnd={2}'.format(id, i,
                                                                                                              rnd)
            yield Request(url=url_forwarded, callback=self.parse_comments,
                          meta={'id': copy.deepcopy(item['id']), 'flag': copy.deepcopy('forwarded')})

    def parse_comments(self, response):

        item = CommentsItem()
        item['id'] = response.meta['id']
        item['flag'] = response.meta['flag']
        item['author'] = []
        item['author_comment'] = []
        item['time'] = []

        text = response.text
        restojson = json.loads(text, encoding='utf-8')
        html = restojson['data']['html']
        html = html.split('\\n')
        html = ''.join(html)
        author_comments = Selector(text=html).xpath('//*[@class="WB_text"]').extract()

        for author_comment in author_comments:

            item['author'].append(Selector(text=author_comment).xpath('//a/text()').extract()[0])
            remove_author = Selector(text=author_comment).xpath('//a/text()').extract()[0]

            author_comment = dealcontent(author_comment)
            comment = Selector(text=author_comment).xpath('//text()').extract()
            comment.remove(remove_author)
            comment = ''.join(comment)

            while re.match(r'^ ', comment):
                comment = comment.strip(' ')

            item['author_comment'].append(comment)

        if item['flag'] == 'forwarded':
            item['time'] = Selector(text=html).xpath('//*[@class="WB_from S_txt2"]/a/@title').extract()
        if item['flag'] == 'comment':
            item['time'] = Selector(text=html).xpath('//*[@class="WB_from S_txt2"]/text()').extract()

        item['like_count'] = Selector(text=html).xpath(
            '////span[@node-type="like_status"]/em[2]/text()').extract()
        lens = len(item['like_count'])

        for i in range(0, lens):
            item['like_count'][i] = item['like_count'][i].replace('赞', '0')

        yield copy.deepcopy(item)
