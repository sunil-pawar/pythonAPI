'''
Created on Dec 4, 2020

@author: opc
'''
# intitalising the flask module
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)    

