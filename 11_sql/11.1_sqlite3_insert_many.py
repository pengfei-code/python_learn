#insert many


import sqlite3


db_path = "/users/songpengfei/pengfei.db"

sql_insert_person_many = "insert into person (pname,age) values(?,?)"

conn = sqlite3.connect(db_path)

cursor = conn.cursor()


try:
    cursor.executemany(sql_insert_person_many,[("lining",33),("张三",15),("李四",24),("董卿",35)])

    # cursor.execute(sql_insert_person_many,("hongwu",66))
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

