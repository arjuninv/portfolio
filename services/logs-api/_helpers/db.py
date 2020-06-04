import os
import mysql.connector
import datetime

DB_NAME = "logs"

class manager:
    def __init__(self):
        # self.setup_db()

        self.mydb = mysql.connector.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            passwd=os.environ['DB_PASSWORD'],
            database=DB_NAME
        )       
        self.mycursor = self.mydb.cursor()

    def get_structure(self):
        self.mycursor.execute('SELECT DISTINCT (log) FROM logs')
        myresult = self.mycursor.fetchall()
        if not myresult:
            return []
        logs = []
        for log in myresult:
            logs.append(log[0])
        return logs

    def get_log(self, name):
        self.mycursor.execute(f'SELECT * FROM logs where log="{name}"')
        myresult = self.mycursor.fetchall()
        if not myresult:
            return []
        logs = []
        for log in myresult:
            logs.append({"timestamp": log[0], "data": log[2]})
        return logs

    def add_log(self, name, data):
        self.mycursor.execute(f'INSERT INTO logs VALUES("{datetime.datetime.now().strftime("%Y-%m-%d:%H:%M:%S")}", "{name}", "{data}")')
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        return False


