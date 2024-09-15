import pymysql
import datetime

# DB 생성
def createDB():
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = 'CREATE DATABASE Board'

    cursor.execute(sql)

    conn.commit()
    conn.close()


# Table 생성
def createMDBT():
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    default_img="static/profile/default.jpg"
    sql = "CREATE TABLE Member_Table(name varchar(100) NOT NULL, id varchar(100) NOT NULL, pwd varchar(100) NOT NULL, img varchar(255) DEFAULT default_img, email varchar(100) NOT NULL, school varchar(100) NOT NULL)"

    # Table 삭제
    #sql = "DROP TABLE Board_Table"

    cursor.execute(sql)

    conn.commit()
    conn.close()
    
# DATABASE TABLE에 정보 추가    
def insertMDB(m_name, m_id, m_password, m_img, m_email, m_shcool):
    now = datetime.datetime.now()
    sqlData = (m_name, m_id, m_password, m_img, m_email, m_shcool)

    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "INSERT INTO Member_Table (name, id, pwd, img, email, school) VALUES (%s, %s, %s, %s, %s, %s)"

    cursor.execute(sql, sqlData)

    conn.commit()
    conn.close()
    
# DATABASE TABLE에서 정보 조회
def selectMDB():
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Member_Table"
    cursor.execute(sql)

    data_list = cursor.fetchall()
    print(data_list)
    conn.commit()
    conn.close()
    
    return data_list
    
# DATABASE TABLE에서 정보 삭제 (id를 받아 삭제)
def deleteMDB(value):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "DELETE FROM Member_Table WHERE id=%s"

    cursor.execute(sql, value)

    conn.commit()
    conn.close()

# DATABASE TABLE에서 정보 검색
def searchidMDB(m_id):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Member_Table WHERE id = %s"
    cursor.execute(sql, m_id)
    data = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    return data

def searchpwdMDB(m_pwd):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Member_Table WHERE pwd = %s"
    cursor.execute(sql,m_pwd)
    data = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    return data


def searchnameMDB(m_name):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Member_Table WHERE name = %s"
    cursor.execute(sql,m_name)
    data = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    return data

def searchemailMDB(m_email):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Member_Table WHERE email = %s"
    cursor.execute(sql,m_email)
    data = cursor.fetchall()

    conn.commit()
    conn.close()
    
    return data

def searchschoolMDB(m_school):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "SELECT * FROM Member_Table WHERE school = %s"
    cursor.execute(sql,m_school)
    data = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    return data

# DATABASE TABLE에서 정보 수정
# 이름 수정
def updatenameMDB(val1, val2):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "UPDATE Member_Table SET name=%s WHERE name=%s"
    list=(val1, val2)
    data = cursor.execute(sql, list)

    conn.commit()
    conn.close()
# 학교 수정
def updateschoolMDB(val1, val2):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "UPDATE Member_Table SET school=%s WHERE school=%s"
    list=(val1, val2)
    data = cursor.execute(sql, list)

    conn.commit()
    conn.close()
# 이메일 수정
def updateemailMDB(val1, val2):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "UPDATE Member_Table SET email=%s WHERE email=%s"
    list=(val1, val2)
    data = cursor.execute(sql, list)

    conn.commit()
    conn.close()
# 비밀번호 수정
def updatepwdMDB(val1, val2):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "UPDATE Member_Table SET pwd=%s WHERE pwd=%s"
    list=(val1, val2)
    data = cursor.execute(sql, list)

    conn.commit()
    conn.close()
    
def updateimgMDB(val1, val2):
    conn = pymysql.connect(host='localhost', user='root', password='', database='db', charset='utf8')
    cursor = conn.cursor()

    sql = "UPDATE Member_Table SET img=%s WHERE img=%s"
    list=(val1, val2)
    data = cursor.execute(sql, list)

    conn.commit()
    conn.close()


    
