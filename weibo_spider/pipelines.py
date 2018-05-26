# -*- coding: utf-8 -*-# Define your item pipelines here## Don't forget to add your pipeline to the ITEM_PIPELINES setting# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.htmlfrom weibo_spider.db.mysql_insert import *import timeimport jsonimport reimport osfrom weibo_spider.spiders.dealtime import deal_timefrom scrapy import Requestfrom scrapy.pipelines.images import ImagesPipelinefrom scrapy.exceptions import DropItemclass WeiboFakenewsPipeline(object):    def process_item(self, item, spider):        if 'reason' in item:            item['informers'] = json.dumps(item['informers'], ensure_ascii=False)            item['informers_content'] = json.dumps(item['informers_content'], ensure_ascii=False)            params = [item['id'], item['informers'], item['informers_count'], item['informants'],                      item['forwarded_count'],                      item['comment_count'],                      item['like_count'], item['informers_content'], item['reason'],                      item['content'],                      item['informants_time']]            insert_fakenews(params)        if 'flag' in item:            lens = len(item['author'])            for i in range(0, lens):                if re.match(r'共\d+条回复', item['author'][i]):                    del item['author'][i]                    del item['author_comment'][i]                # 处理评论的item                if item['flag'] == 'comment':                    # 处理各种时间                    item['time'][i] = deal_time(item['time'][i])                    if re.match(r'第\d+楼 ', item['time'][i]):                        floor = re.findall(r'第\d+楼 ', item['time'][i])[0]                        item['time'][i] = item['time'][i].replace(floor, '')                    if re.match(r'201\d', item['time'][i]):                        item['time'][i] = item['time'][i].strip(' ')                        item['time'][i] = item['time'][i].split('-')                        if int(item['time'][i][1]) < 10:                            item['time'][i][1] = '0' + item['time'][i][1]                        if int(item['time'][i][2].split(' ')[0]) < 10:                            item['time'][i][2] = '0' + item['time'][i][2]                        item['time'][i] = ('-'.join(item['time'][i])).rstrip(' ')                    else:                        if re.match(r'今天', item['time'][i]):                            timereplace = time.strftime("%F")                            timereplace = item['time'][i].replace('今天', timereplace)                            item['time'][i] = timereplace.rstrip(' ')                        else:                            item['time'][i] = item['time'][i].replace('月', '-').replace('日', '')                            year = time.strftime('%Y', time.localtime(time.time()))                            item['time'][i] = (year + '-' + item['time'][i]).split('-')                            if int(item['time'][i][1]) < 10:                                item['time'][i][1] = '0' + item['time'][i][1]                            if int(item['time'][i][2].split(' ')[0]) < 10:                                item['time'][i][2] = '0' + item['time'][i][2]                            item['time'][i] = ('-'.join(item['time'][i])).rstrip(' ')                params = [item['id'], item['flag'], item['author'][i], item['author_comment'][i],                          item['like_count'][i], item['time'][i]                          ]                if spider.name == 'fakenews':                    insert_comments_fakenews(params)                if spider.name == 'flight_girl':                    insert_comments_flightgirl(params)        if 'description' in item:            if spider.name == 'flight_girl':                params = [item['id'], item['name'], item['follow_count'], item['follower_count'], item['weibo_count']                    , item['verified'], item['rank'], item['description']]                insert_author_flightgirl(params)            if spider.name == 'fakenews':                params = [item['id'], item['name'], item['follow_count'], item['follower_count'], item['weibo_count']                    , item['description']]                insert_author_fakenews(params)        if 'device' in item:            params = [item['id'],                      item['author'],                      item['author_id'],                      item['forwarded_count'],                      item['comment_count'],                      item['like_count'],                      item['content'],                      item['device'],                      item['time']]            insert_flightgirl(params)class WeiboImgDownloadPipeline(ImagesPipeline):    def get_media_requests(self, item, info):        if 'image_url' in item:            #     for image_url in item['image_urls']:            yield Request(item['image_url'])        return item    def item_completed(self, results, item, info):        if 'image_url' in item:            image_paths = [x['path'] for ok, x in results if ok]            if not image_paths:                raise DropItem("Item contains no images")            newname = item['image_name'] + '.jpg'            os.rename("/hbasestorage/spider/spider_2018_2_files/flightgirl_weibo/images/" + image_paths[0],                      "/hbasestorage/spider/spider_2018_2_files/flightgirl_weibo/images/" + newname)            return item        return item