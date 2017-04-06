from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY']='Biggest Baddest Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/trs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['REDIS_URL']= 'redis://localhost'
# app.register_blueprint(sse,url_prefix='/getEta')

db=SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


app.config.from_object(__name__)
from app import views
