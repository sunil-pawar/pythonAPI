'''
Created on Dec 4, 2020
creating config file for DB
@author: opc
'''
from app import app
#from  flask_mysql  import MySQL
#import mysql.connector
from flask_mysqldb import MySQL

mysql = MySQL()
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'clients'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)