import sqlite3


db_path = "/users/songpengfei/pengfei.db"

sql_update_person = "update person set pname = ?,age = ? where pno = ?"
conn = sqlite3.connect(db_path)

cursor=conn.cursor()

try:
    cursor.execute(sql_update_person,("songna1",35,2))
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

