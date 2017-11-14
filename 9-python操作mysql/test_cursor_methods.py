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

sql = "select * from user"
cursor.execute(sql)

print cursor.rowcount

# print cursor.fetchone()

# print cursor.fetchmany(2)

print cursor.fetchall()

cursor.close()
conn.close()