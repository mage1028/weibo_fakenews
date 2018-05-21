import pymysql


def connect():
    db = pymysql.connect(host='localhost', user='root', password='', db='fakenewsb', port=3306, charset='utf8mb4')
    return db


def addTable_weibo():
    sql = '''create table fakenews(
    id bigint primary key,
    informers varchar(42),
    informers_counts int,
    informants varchar(20),
    forwarded_counts int,
    comment_counts int,
    like_counts int,
    informers_content varchar(400),
    reason varchar(300),
    content varchar(2000),
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
    sql = '''create table comments(
    id bigint,
    flag char(10),
    author varchar(20) not null,
    author_comment varchar(150) not null,
    like_counts int,
    comment_time timestamp ,
    primary key (author,author_comment))
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

#
# def addTable_cookies():
#     sql = '''create table cookies(
#     account varchar(40),
#     cookie varchar(300)
#
#     )
#     '''
#     conn = connect()
#     cursor = conn.cursor()
#     try:
#         cursor.execute(sql)
#         conn.commit()
#         print('ojbk')
#     except Exception as e:
#         conn.rollback()
#         conn.close()
#         print(e)


def addTable_author():
    sql = '''create table Author(
    id bigint primary key,
    name varchar(40),
    follow_count int,
    follower_count int,
    weibo_count int,
    description varchar(800))
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
if __name__ == '__main__':
    addTable_weibo()
    addTable_comments()
    addTable_author()

