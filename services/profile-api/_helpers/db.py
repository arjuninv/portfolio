import os
import mysql.connector

DB_NAME = "profile"

class manager:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            passwd=os.environ['DB_PASSWORD'],
            database=DB_NAME
        )


    def get_structure(self):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('SELECT * FROM root where id="structure"')
        myresult = self.mycursor.fetchone()
        return myresult[1].replace('||n', '\n')
        self.mycursor.close()

    def get_page(self, page):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(f'SELECT * FROM pages where id="{page}"')
        myresult = self.mycursor.fetchone()
        return myresult[1].replace('||n', '\n')
        self.mycursor.close()
