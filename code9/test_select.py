import pymysql

conn = pymysql.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    passwd = "123456",
    db = "hello",
)
cursor = conn.cursor()
sql = "select * from user"

cursor.execute(sql)
rs = cursor.fetchall()
print rs
# for user in rs:
#     print user[0], user[1]


# rs = cursor.fetchone()
# print rs

# rs = cursor.fetchmany(2)
# print rs

cursor.close()
conn.close()