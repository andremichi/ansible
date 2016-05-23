#!/usr/bin/env python

import datetime
from flask import Flask
from pymongo import MongoClient
import sys

try:
   client = MongoClient("mongodb://{{ mongodb_username }}:{{ mongodb_password }}@mongodb-{{ app_name }}-{{ app_env }}-member1.{{ app_env }}.mycompany.com")
except:
   print "Error connecting to mongodb host"
   sys.exit(1)

db = client.app_database
collection = db.app_collection

app = Flask(__name__)

@app.route("/app", methods=['POST'])
def insertData():
    document = { "user": "someUser",
                 "timestamp": datetime.datetime.utcnow()
               }
    try:
      collection.insert(document)
      print "Timestamp successfuly inserted"
      return "OK",200
    except:
      print "Error inserting Data"
      return "[ERROR]", 500

if __name__ == "__main__":
  app.run()
