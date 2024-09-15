import pymysql

# Table 생성
conn = pymysql.connect(host='localhost', user='root', password='EKdms001^^', db='Board', charset='utf8')
cursor = conn.cursor()

sql = "CREATE TABLE Board_Table(idx int AUTO_INCREMENT PRIMARY KEY, datetime DATETIME NOT NULL, name varchar(100) NOT NULL, title varchar(500) NOT NULL, content varchar(500) NOT NULL)"

# Table 삭제
#sql = "DROP TABLE Board_Table"

cursor.execute(sql)

conn.commit()
conn.close()