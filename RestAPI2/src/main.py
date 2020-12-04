'''
Created on Dec 4, 2020

@author: opc
'''
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from MySQLdb import _exceptions



        
@app.route('/add', methods=['POST'])
def add_emp():
    try:
        _json =  request.json
        _name = _json['name']
        _cpf = _json['cpf']
        _address = _json['address']        
        if _name and _cpf and _address and request.method == 'POST':            
            sqlQuery = '''INSERT INTO employees(Name, cpf, address) VALUES(%s, %s, %s)'''
            bindData = (_name, _cpf, _address)
            cur = mysql.connection.cursor()
      #      try:
            cur.execute(sqlQuery, bindData)
            mysql.connection.commit() 
      #      except _exceptions.DatabaseError as dber:
        #        return str(dber)
            cur.close()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except (_exceptions.DatabaseError,_exceptions.MySQLError) as e:
        return e
   
        
@app.route('/emp')
def emp():
    try:
        cur = mysql.connection.cursor()
        cur.execute('''SELECT Name, cpf, address FROM employees''')
        empRows = cur.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        return str(e)
   
       
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()