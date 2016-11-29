from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:maximus14@localhost/deadBox' #postgresql://username(db):password@urlAddress/DBname
app.debug = True
db = SQLAlchemy(app)
db.create_all()

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

@app.route('/')
def index():
    myClippings = Clipboard.query.all()
    oneItem = Clipboard.query.filter_by(userId=0).first()
    return render_template('post.html', myClippings=myClippings, oneItem=oneItem)

@app.route('/post_user', methods=['POST'])
def post_user():
    clip = Clipboard(request.form['clipping']) 
    clip.userId = 0
    clip.time = datetime.now()
    db.session.add(clip)
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == "__main__":  #make sure the app will be run on it's own, not as API
    
    app.run()