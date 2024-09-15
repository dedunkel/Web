import pymysql
import datetime

# DB 생성
def createDB():
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = 'CREATE DATABASE Board'

    cursor.execute(sql)

    conn.commit()
    conn.close()


# Table 생성
def createDBT():
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "CREATE TABLE Board_Table(idx int AUTO_INCREMENT PRIMARY KEY, datetime DATETIME NOT NULL, name varchar(100) NOT NULL, title varchar(500) NOT NULL, content varchar(500) NOT NULL, file varchar(255) NOT NULL)"

    # Table 삭제
    #sql = "DROP TABLE Board_Table"

    cursor.execute(sql)

    conn.commit()
    conn.close()
    
# DATABASE TABLE에 정보 추가    
def insertDB(writer, title, content, file):
    now = datetime.datetime.now()
    format = '%Y-%m-%d %H:%M:%S'
    now = now.strftime(format)
    sqlData = (now, writer, title, content, file)

    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "INSERT INTO Board_Table (idx, datetime, name, title, content, file) VALUES (NULL, %s, %s, %s, %s, %s)"

    cursor.execute(sql, sqlData)

    conn.commit()
    conn.close()
    
# DATABASE TABLE에서 정보 조회
def selectDB():
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Board_Table"
    cursor.execute(sql)

    data_list = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    return data_list
    
# DATABASE TABLE에서 정보 삭제
def deleteDB(value):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "DELETE FROM Board_Table WHERE idx=%s"

    cursor.execute(sql, value)

    conn.commit()
    conn.close()

# DATABASE TABLE에서 정보 검색
def searchidDB(id):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Board_Table WHERE idx = %s"
    cursor.execute(sql, id)
    data = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    return data

def searchtitleDB(title):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Board_Table WHERE title = %s"
    cursor.execute(sql,title)
    data = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    return data

def searchcontentDB(content):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Board_Table WHERE content = %s"
    cursor.execute(sql,content)
    data = cursor.fetchall()

    conn.commit()
    conn.close()
    
    return data

def searchnameDB(name):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Board_Table WHERE name = %s"
    cursor.execute(sql,name)
    data = cursor.fetchall()

    print(data)
    
    conn.commit()
    conn.close()
    
    return data


# DATABASE TABLE에서 정보 수정
def updatenameDB(val1, val2):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "UPDATE Board_Table SET name=%s WHERE name=%s"
    list=(val1, val2)
    data = cursor.execute(sql, list)

    conn.commit()
    conn.close()

def updatetitleDB(val1, val2):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "UPDATE Board_Table SET title=%s WHERE title=%s"
    list=(val1, val2)
    data = cursor.execute(sql, list)

    conn.commit()
    conn.close()

def updatecontentDB(val1, val2):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "UPDATE Board_Table SET content=%s WHERE content=%s"
    list=(val1, val2)
    data = cursor.execute(sql, list)

    conn.commit()
    conn.close()

def updatefileDB(val1, val2):
    conn = pymysql.connect(host='localhost', user='root', password='', charset='utf8')
    cursor = conn.cursor()

    sql = "UPDATE Board_Table SET file=%s WHERE file=%s"
    list=(val1, val2)
    data = cursor.execute(sql, list)

    conn.commit()
    conn.close()

