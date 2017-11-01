import pymysql
# pymysql.install_as_MySQLdb()
conn = pymysql.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    passwd = "123456",
    db = "hello",
)

cursor = conn.cursor()

sql_insert = "insert into user(userid, username) values(10, 'name10')"
sql_update = "update user set username = 'zhangsan' where userid=2"
sql_delete = "delete from user where userid<3"
try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    conn.commit()
except BaseException,e:
    print e 
    conn.rollback()
cursor.close()
conn.close()