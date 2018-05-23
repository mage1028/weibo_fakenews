import pymysql
import json


def connect():
    db = pymysql.connect(host='localhost', user='root', password='', db='weibo_fakenews', port=3306, charset='utf8mb4')
    return db


def select_cookie():
    '''

    :return: list格式的cookies集合
    '''
    sql = '''select cookie from cookies
    '''
    conn = connect()
    cursor = conn.cursor()
    try:
        cookies = []
        cursor.execute(sql)
        cookies_db = cursor.fetchall()
        for i in cookies_db:
            cookie = json.loads(i[0])
            cookies.append(cookie)
        return cookies
    except Exception as e:
        conn.rollback()
        conn.close()
        print(e)
