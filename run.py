from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import rasp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rasp.db'
db = SQLAlchemy(app)
db.create_all()

app.register_blueprint(rasp)



if __name__ == '__main__':
    app.run()