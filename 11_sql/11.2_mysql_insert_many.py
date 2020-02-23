#insert
import pymysql

conn = pymysql.connect(host='192.168.1.100',user ="song",password = "Song521@",database = "school")
cursor = conn.cursor()
sql_insert_many = "insert into student (name,gender,score) values(%s,%s,%s)"

try:
    list_values = [("黎明",'m',30.2),('刘德华','m',90.3),('章子怡','f',80.2),('闫妮','f',79.3)]
    cursor.executemany(sql_insert_many,list_values)
    conn.commit()
    pass
except Exception as e:
    print(e)
    conn.rollback()
    pass
finally:
    cursor.close()
    conn.close()
    pass

