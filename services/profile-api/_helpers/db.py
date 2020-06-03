import os
import mysql.connector

DB_NAME = "profile"

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
        self.mycursor.execute(f'CREATE TABLE IF NOT EXISTS root (id varchar(24) primary key, value LONGTEXT)')
        self.mycursor.execute(f'CREATE TABLE IF NOT EXISTS pages (id varchar(24) primary key, value LONGTEXT)')
        
    def setup_db(self):
        mydb = mysql.connector.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            passwd=os.environ['DB_PASSWORD']
        )
        mycursor = mydb.cursor()

        mycursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')

        mydb.commit()

    def get_structure(self):
        self.mycursor.execute('SELECT * FROM root where id="structure"')
        myresult = self.mycursor.fetchone()
        return myresult[1].replace('||n', '\n')

    def get_page(self, page):
        self.mycursor.execute(f'SELECT * FROM pages where id="{page}"')
        myresult = self.mycursor.fetchone()
        return myresult[1].replace('||n', '\n')


