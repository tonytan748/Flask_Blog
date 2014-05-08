from flask import Flask
form flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)

from app import views,models



