#insert the value
#single row
#rows

import sqlite3


sql_insert_person = "insert into person (pname,age) values(?,?)"
db_path = "/users/songpengfei/pengfei.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


try:
    cursor.execute(sql_insert_person,("姚明",40))
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
