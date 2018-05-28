import pymysql
import logging


def connect_flightgirl():
    db = pymysql.connect(host='192.168.100.103', user='root', password='root', db='Weibo_Flightgirl_Spider', port=3306,
                         charset='utf8mb4')
    return db


def connect_fakenews():
    db = pymysql.connect(host='192.168.100.103', user='root', password='root', db='fakenewsb', port=3306,
                         charset='utf8mb4')
    return db


def insert_fakenews(params):
    sql = '''insert into weibo_fakenews(id,
    informers,
    informers_count,
    informants,
    
    forwarded_count,
    comment_count,
    like_count,
    informers_content,
    reason,
    content,
    informants_time,
    url)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    conn = connect_fakenews()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
        logging.info('------------------------------insert weibo_spider ojbk-----------------------------')
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.info(e)
        logging.info(params)


def insert_comments_flightgirl(params):
    sql = '''insert into Comments(id,flag,author,author_comment,like_count,comment_time) 
    values (%s,%s,%s,%s,%s,%s)
    '''
    conn = connect_flightgirl()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
        logging.info('---------------------insert comments ojbk-----------------------')
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.info(e)
        logging.info(params)

def insert_comments_fakenews(params):
    sql = '''insert into comments(id,flag,author,author_comment,like_count,comment_time) 
    values (%s,%s,%s,%s,%s,%s)
    '''
    conn = connect_fakenews()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
        logging.info('---------------------insert comments ojbk-----------------------')
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.info(e)
        logging.info(params)

def insert_author_flightgirl(params):
    sql = '''insert into Author(id,name,follow_count,follower_count,weibo_count,verified,rank,description) values (%s,%s,%s,%s,%s,%s,%s,%s)
       '''
    conn = connect_flightgirl()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
        logging.info('-----------------------------------insert author ojbk---------------------------------')
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.info(e)
        logging.info(params)

def insert_author_fakenews(params):
    sql = '''insert into Author(id,name,follow_count,follower_count,weibo_count,description) values (%s,%s,%s,%s,%s,%s)
       '''
    conn = connect_fakenews()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
        logging.info('-----------------------------------insert author ojbk---------------------------------')
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.info(e)
        logging.info(params)


def insert_flightgirl(params):
    sql = '''insert into FlightGirl_Weibo(
    id,
    author,
    author_id,
    forwarded_count,
    comment_count,
    like_count,
    content,
    device,
    time)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    conn = connect_flightgirl()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
        logging.info('------------------------------insert weibo_flightgirl ojbk-----------------------------')
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.info(e)
        logging.info(params)
