import mysql.connector
from mysql.connector import Error
class DatabaseHandler:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', database='annotation', user='root', password='')
            if self.conn.is_connected():
                print("database is connected")
        except Error as e:
            print(e)
    def countElement(self):
        try:
            self.cur=self.conn.cursor()
            self.cur.execute("select count(*) from parameters")
            count = self.cur.fetchall()
            return count[0][0]
        except Error as e:
            print(e)
    def getConnection(self):
        return self.conn
