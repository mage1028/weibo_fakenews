# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from fakenews.db.mysql_insert import insert_fakenews, insert_comments, insert_author
import time
import json
import re
from fakenews.spiders.dealtime import deal_time


class WeiboFakenewsPipeline(object):
    def process_item(self, item, spider):
        if 'content' in item:
            item['informers'] = json.dumps(item['informers'], ensure_ascii=False)
            item['informers_content'] = json.dumps(item['informers_content'], ensure_ascii=False)
            params = [item['id'], item['informers'], item['informers_counts'], item['informants'],
                      item['forwarded_counts'],
                      item['comment_counts'],
                      item['like_counts'], item['informers_content'], item['reason'],
                      item['content'],
                      item['informants_time']]
            insert_fakenews(params)
        if 'flag' in item:

            lens = len(item['author'])

            for i in range(0, lens):
                if re.match(r'共\d+条回复', item['author'][i]):
                    del item['author'][i]
                    del item['author_comment'][i]
                # 处理评论的item

                if item['flag'] == 'comment':
                    # 处理各种时间
                    item['time'][i] = deal_time(item['time'][i])
                    if re.match(r'第\d+楼 ', item['time'][i]):
                        floor = re.findall(r'第\d+楼 ', item['time'][i])[0]
                        item['time'][i] = item['time'][i].replace(floor, '')
                    if re.match(r'201\d', item['time'][i]):
                        item['time'][i] = item['time'][i].strip(' ')
                        item['time'][i] = item['time'][i].split('-')
                        if int(item['time'][i][1]) < 10:
                            item['time'][i][1] = '0' + item['time'][i][1]
                        if int(item['time'][i][2].split(' ')[0]) < 10:
                            item['time'][i][2] = '0' + item['time'][i][2]
                        item['time'][i] = ('-'.join(item['time'][i])).rstrip(' ')
                    else:
                        if re.match(r'今天', item['time'][i]):
                            timereplace = time.strftime("%F")
                            timereplace = item['time'][i].replace('今天', timereplace)
                            item['time'][i] = timereplace.rstrip(' ')

                        else:
                            item['time'][i] = item['time'][i].replace('月', '-').replace('日', '')
                            year = time.strftime('%Y', time.localtime(time.time()))
                            item['time'][i] = (year + '-' + item['time'][i]).split('-')
                            if int(item['time'][i][1]) < 10:
                                item['time'][i][1] = '0' + item['time'][i][1]
                            if int(item['time'][i][2].split(' ')[0]) < 10:
                                item['time'][i][2] = '0' + item['time'][i][2]
                            item['time'][i] = ('-'.join(item['time'][i])).rstrip(' ')

                params = [item['id'], item['flag'], item['author'][i], item['author_comment'][i],
                          item['like_counts'][i], item['time'][i]
                          ]
                insert_comments(params)
        if 'description' in item:
            params = [item['id'], item['name'], item['follow_count'], item['follower_count'], item['weibo_count'],
                      item['description']]
            insert_author(params)
