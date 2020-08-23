from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f021fcff13fe1e30aa8436ec92d8449c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)