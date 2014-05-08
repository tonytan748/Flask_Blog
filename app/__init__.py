from flask import Flask
form flask.ext.sqlalchemy import SQLAlchemy

import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app=Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)

lm=LoginManager()
lm.init_app(app)
oid=OPenID(app,os.path.join(basedir,'tmp'))

from app import views,models



