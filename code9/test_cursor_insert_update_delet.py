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

sql_insert = "insert into user(userid, username) values(4, 'name4')"
sql_update = "update user set username = 'zhangsan' where userid=3"
sql_delete = "delete from user where userid<3"


cursor.execute(sql_insert)
print cursor.rowcount
cursor.execute(sql_update)
print cursor.rowcount
cursor.execute(sql_delete)
print cursor.rowcount
conn.commit()

cursor.close()
conn.close()