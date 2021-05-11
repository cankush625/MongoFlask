from flask import Flask, render_template
import subprocess as sp
from pymongo import MongoClient
from mongopass import mongopass

app = Flask("myapp")

client = MongoClient(mongopass)
db = client.curd
myCollection = db.myColl

@app.route("/")
def my_home():
    date = sp.getoutput("date /t")
    return render_template("home.html", date=date)

@app.route("/curd")
def insert_val():
    return render_template("curd.html")

@app.route("/read")
def read():
    cursor = myCollection.find()
    for record in cursor:
        print(cursor)
    return render_template("response.html")

@app.route("/insert")
def insert():
    return render_template("response.html")
