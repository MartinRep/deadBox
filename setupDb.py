from flask import Flask
from flask_sqlalchemy import SQLAlchemy

setupDb = Flask(__name__)
setupDb.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:maximus14@localhost/deadBox' #postgresql://username(db):password@urlAddress/DBname
db = SQLAlchemy(setupDb)

class Clipboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    clipping = db.Column(db.String(1024))
    time = db.Column(db.String(30))

    def __init__(self, userId, clipping, time):
        self.userId = userId
        self.clipping = clipping
        self.time = time

    def __repr__(self):
        return '<Clipboard %r>' % self.clipping


    db.create_all()
    print("Database created....")