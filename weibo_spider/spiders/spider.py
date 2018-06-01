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
from scrapy_redis.spiders import Spider
import logging


class FakeNewsSpider(Spider):
    name = 'fakenews'
    urls = []
    for i in range(600, 1000):
        urls.append(['https://service.account.weibo.com/?type=5&status=4&page={0}'.format(i)])

    def start_requests(self):

        for url in self.urls:
            url = url[0]
            yield Request(url=url, callback=self.parse)

    def parse(self, response):

        text = response.text

        urls = re.findall(r'show\?rid=\w+', text)

        for i in range(12, 13):
            url = 'http://service.account.weibo.com/' + urls[i]

            yield Request(url=url, callback=self.parse_fake, meta={'url': url})

    def parse_fake(self, response):
        # todo 用户表=。=
        item = WeiboFakenewsItem()
        informers = []
        informers_content = []
        item['url'] = response.meta['url']
        # item['url'] = response.meta['url']
        text = response.text

        html = re.findall(r'<script>[\s\S]*?</script>', text)[0].strip('<script>').strip('</script>')

        html = html.strip('STK && STK.pageletM && STK.pageletM.view(').strip(')')

        html = json.loads(html)['html']
        people = []
        item['reason'] = Selector(text=html).xpath('//*[@class="p"]/text()').extract()
        item['reason'] = dealstr(''.join(item['reason']))
        contents = Selector(text=html).xpath('//*[@class="con"]').extract()
        for content in contents:

            try:
                people.append(re.findall(r'blank\">[\s\S]*?</a>', content)[0].strip('blank\">').strip('</a>'))
                content = Selector(text=content).xpath('//*[@class="con"]/input/@value').extract()[0]
                content = dealstr(content)
                informers_content.append(content)

            except:
                try:
                    content = re.findall(r'/a>[\s\S]*?</div>', content)[0].strip('/a>').strip('</div>')
                    content = dealstr(content)
                except:
                    content = '已被删除'
                informers_content.append(content)

        backup = informers_content[-1]
        del informers_content[-1]
        item['informers_content'] = informers_content
        item['informants'] = people[-1]
        del people[-1]
        item['informers'] = people

        people_count = \
            Selector(text=html).xpath('//span[@class="W_f12 W_textb"]/text()').extract()[
                0]

        item['informers_count'] = re.findall(r'\d+', people_count)[0]

        informants_time = Selector(text=html).xpath('//div[@class="item top"]/p[@class="publisher"]/text()').extract()
        informants_time = ''.join(informants_time).split('发布时间：')[1].split()
        item['informants_time'] = ' '.join(informants_time)
        informants_url = Selector(text=html).xpath('//*[@class="item top"]/div/a/@href').extract()[0]
        item['informants_id'] = re.findall(r'\d+', informants_url)[0]

        yield Request(url=informants_url, callback=self.parse_author,
                      meta={'id': item['informants_id'], 'name': item['informants']})

        try:
            url = Selector(text=html).xpath('//p[@class="publisher"]/a/@href').extract()[0]
            yield Request(url=url, callback=self.parse_fakeweibo, meta={'item': item})
        except:
            item['content'] = backup
            a = str(random.randint(0, 99999999))
            item['id'] = '999999999' + a
            item['forwarded_count'] = 0
            item['comment_count'] = 0
            item['like_count'] = 0
            if not informants_time:
                item['informants_time'] = '2000-01-01 00:00'
            yield item

    def parse_author(self, response):
        text = response.text
        item = AuthorItem()

        item['id'] = response.meta['id']
        item['name'] = response.meta['name']

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
        item['description'] = response.xpath('//meta[@name="description"]/@content').extract()[0].strip(
            '新浪微博，随时随地分享身边的新鲜事儿。')
        yield item

    def parse_fakeweibo(self, response):
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

        yield item

        # 找到所有评论和转发
        for i in range(1, page_max1 + 1):
            url_comment = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id={0}&page={1}&__rnd={2}'.format(id, i, rnd)
            yield Request(url=url_comment, callback=self.parse_comments,
                          meta={'id': item['id'], 'flag': 'comment'})
        page_max2 = int(math.ceil(int(item['forwarded_count']) / 20))

        for i in range(1, page_max2 + 1):
            url_forwarded = 'https://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id={0}&page={1}&__rnd={2}'.format(id, i,
                                                                                                              rnd)
            yield Request(url=url_forwarded, callback=self.parse_comments, meta={'id': item['id'], 'flag': 'forwarded'})

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

        item['like_count'] = Selector(text=html).xpath('////span[@node-type="like_status"]/em[2]/text()').extract()
        lens = len(item['like_count'])

        for i in range(0, lens):
            item['like_count'][i] = item['like_count'][i].replace('赞', '0')

        yield item
