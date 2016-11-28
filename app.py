from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:maximus14@localhost/deadBox' #postgresql://username(db):password@urlAddress/DBname
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return


if __name__ == "__main__":  #make sure the app will be run on it's own, not as API
    
    app.run()