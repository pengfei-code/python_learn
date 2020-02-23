import sqlite3

#connect the database and create the table

db_path = "/users/songpengfei/pengfei.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

sql_create_table_person='''
        create table person (
            pno INTEGER primary key  autoincrement,
            pname varchar not null ,
            age INTEGER 
        )
'''
try:
    cursor.execute(sql_create_table_person)
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()



