#insert
import pymysql
conn = pymysql.connect(host="192.168.1.100",password="Song521@",user ="song",port = 3306,database="school")
sql_insert = "insert into student (name,gender,score) values(%s,%s,%s)"
cursor = conn.cursor()
try:
    cursor.execute(sql_insert,('song',"m","99.9"))
    conn.commit()
    pass
except Exception as e:
    print(e)
    conn.rollback()
    pass
finally:
    cursor.close()
    conn.close()