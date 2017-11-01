# coding:utf-8
import pymysql


class TransferMoney(object):

    def __init__(self, conn):
        self._conn = conn
        

    def check_money(self, acctid, money):
        cursor = self._conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>%s"%(acctid, money)
            print "check_money",sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号 %s没有足够的钱"%acctid)
        finally:
            cursor.close()

    def check_acct(self, acctid):
        cursor = self._conn.cursor()
        try:
            sql = "select * from account where acctid=%s"%acctid
            print "check_acct",sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号 %s不存在"%acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        cursor = self._conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s"%(money,acctid)
            print "reduce_money",sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("账号 %s减款失败"%acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        cursor = self._conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s"%(money,acctid)
            print "add_money",sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("账号 %s加款失败"%acctid)
        finally:
            cursor.close()

    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct(source_acctid)
            self.check_acct(target_acctid)
            self.check_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()
            raise e

if __name__ == "__main__":
    source_acctid = 1
    target_acctid = 2
    money = 100
    conn = pymysql.Connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        passwd = "123456",
        db = "hello",
    )
    tr_money = TransferMoney(conn)
    try:
        tr_money.transfer(source_acctid, target_acctid, money)
        print u"转账成功"
    except Exception as e:
        print e 
    finally:
        conn.close()

