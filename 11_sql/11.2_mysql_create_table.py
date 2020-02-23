import pymysql

conn = pymysql.connect(host="192.168.1.100",user="song",password="Song521@",database="school",port=3306)

sql_table_student = '''
                        create table student(
                            id int primary key auto_increment,
                            name varchar(32) not null,
                            gender varchar(2) default 'm',
                            score float(3,1)
                        )
'''
cursor = conn.cursor();

try:
    cursor.execute(sql_table_student);

    pass
except BaseException as e:
    print(e)
finally:
    cursor.close();
    conn.close();
    pass



