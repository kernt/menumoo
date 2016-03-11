from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('menumoo')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menumoo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#  Security
from flask import session as login_session
import random, string

import menumoo.views

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
