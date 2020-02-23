#query
import pymysql
conn = pymysql.connect(host="192.168.1.102",user="song",password="Song521@",database="school")
cursor = conn.cursor()

sql_query="select * from student where gender =%s"

try:
    cursor.execute(sql_query,"m")
    print(cursor.arraysize)
    obj = cursor.fetchone()
    objs = cursor.fetchmany(size=4)
    print(obj)
    print(objs)

    pass
except Exception as e:
    print(e)

    pass
finally:
    cursor.close()
    conn.close()
    pass


