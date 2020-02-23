import sqlite3


db_path = "/users/songpengfei/pengfei.db"

sql_del_person = "delete from person where pname = ?"

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# It's very important to notice that if the tuple  has only one element ,please add a comma after it
try:
    cursor.execute(sql_del_person,("姚明",))

    conn.commit()

    pass
except Exception as e:
    print(e)

    pass
finally:
    cursor.close()
    conn.close()
    pass














