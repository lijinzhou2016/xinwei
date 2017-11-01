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

rs = cursor.fetchall()

for row in rs:
    print "userid={0}, username={1}".format(row[0], row[1])

cursor.close()
conn.close()