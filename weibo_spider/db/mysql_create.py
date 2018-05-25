import pymysql


def connect():
    db = pymysql.connect(host='192.168.100.103', user='root', password='root', db='Weibo_Flightgirl_Spider', port=3306,
                         charset='utf8mb4')
    return db


def connect_fgirl():
    db = pymysql.connect(host='192.168.100.103', user='root', password='root', db='Weibo_Flightgirl_Spider', port=3306,
                         charset='utf8mb4')
    return db


def addTable_weibo():
    sql = '''create table weibo_spider(
    id bigint primary key,
    informers tinytext,
    informers_count int,
    informants tinytext,
    forwarded_count int,
    comment_count int,
    like_count int,
    informers_content text,
    reason text,
    content text,
    informants_time timestamp )
    '''

    print(sql)
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        conn.commit()
        print('ojbk')
    except Exception as e:
        conn.rollback()  # 回滚
        conn.close()


def addTable_comments():
    sql = '''create table Comments(
    id bigint,
    flag char(10),
    author varchar(40) not null,
    author_comment varchar(1000),
    like_count int,
    comment_time timestamp ,
    primary key (author,comment_time))
    '''
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        conn.commit()
        print('ojbk')
    except Exception as e:
        conn.rollback()
        conn.close()
        print(e)



def addTable_author():
    sql = '''create table Author(
    id bigint primary key,
    name varchar(40),
    follow_count int,
    follower_count int,
    weibo_count int,
    verified char(30),
    rank int,
    description text)
    '''
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        conn.commit()
        print('ojbk')
    except Exception as e:
        conn.rollback()
        conn.close()
        print(e)
def addTable_weiboFG():
    sql = '''create table FlightGirl_Weibo(
    id bigint primary key,
    author tinytext,
    author_id bigint,
    forwarded_count int,
    comment_count int,
    like_count int,   
    content text,
    device varchar (30),
    time timestamp )
    '''
    print(sql)
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        conn.commit()
        print('ojbk')
    except Exception as e:
        conn.rollback()  # 回滚
        conn.close()
if __name__ == '__main__':

    addTable_comments()
    addTable_author()
    addTable_weiboFG()
