#coding:utf-8
from flask import Flask
from flask.ext.mongoegine import MongoEngine

app=Flask(__name__)
app.config.from_object('config')
db=MongoEngine(app)
from app import views,models
