import sqlite3

db_path = "/users/songpengfei/pengfei.db"
sql_select ="select * from person"

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

try:
    cursor.execute(sql_select)
    # lists= cursor.fetchall()
    # print(lists)
    items = cursor.fetchmany(3)
    print(items)
    oneitem=cursor.fetchone()
    print(oneitem)
    pass
except Exception as e:
    print(e)

    pass
finally:
    cursor.close()
    conn.close()

    pass

