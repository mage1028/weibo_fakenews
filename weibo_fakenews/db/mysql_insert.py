import pymysql
import logging

def connect():
    db = pymysql.connect(host='192.168.100.103', user='root', password='root', db='fakenewsb', port=3306, charset='utf8mb4')
    return db


def insert_fakenews(params):

    sql = '''insert into fakenews(id,
    informers,
    informers_counts,
    informants,
    
    forwarded_counts,
    comment_counts,
    like_counts,
    informers_content,
    reason,
    content,
    informants_time)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
        logging.info('------------------------------insert fakenews ojbk-----------------------------')
    except Exception as e:
        conn.rollback()
        conn.close()
        # logging.exception(e)
        logging.info(params)


def insert_comments(params):
    sql = '''insert into comments(id,flag,author,author_comment,like_counts,comment_time) 
    values (%s,%s,%s,%s,%s,%s)
    '''
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
        logging.info('---------------------insert comments ojbk-----------------------')
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.exception(e)
        logging.info(params)



def insert_cookie(params):
    sql='''insert into cookies(account,cookie) values (%s,%s)
    '''
    conn=connect()
    cursor=conn.cursor()
    try:
        cursor.execute(sql,params)
        conn.commit()
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.exception(e)
        logging.info(params)
def delete_cookies(cookie):
    sql='''delete from cookies where cookie='{0}'
    '''.format(cookie)
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        print('已删除无效cookie')
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.exception(e)
def insert_author(params):
    sql = '''insert into Author(id,name,follow_count,follower_count,weibo_count,description) values (%s,%s,%s,%s,%s,%s)
       '''
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
        logging.info('-----------------------------------insert author ojbk---------------------------------')
    except Exception as e:
        conn.rollback()
        conn.close()
        logging.exception(e)
        logging.info(params)