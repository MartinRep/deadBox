from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for
from datetime import datetime
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_mail import Mail


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:maximus14@localhost/postgres' #postgresql://username(db):password@urlAddress/DBname
app.config['SECRET_KEY'] = 'super-secret-key'   #You should change this
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Get rid of SQLAlchemy overhead warnings
app.config['SECURITY_REGISTERABLE'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'    #make sure to change this to your mail server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'deadBoxTest@gmail.com'   # email to send confirmation mails from
app.config['MAIL_PASSWORD'] = 'deadbox123'  # email account password
mail = Mail(app)
app.debug = True        # debugged
db = SQLAlchemy(app)

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

class Clipboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    clipping = db.Column(db.String(1024))
    time = db.Column(db.String(30))

    # Constractor
    def __init__(self, userId, clipping, time):
        self.userId = userId
        self.clipping = clipping
        self.time = time
    # toString
    def __repr__(self):
        return '<%r>' % self.clipping

# Creates database structure
@app.before_first_request
def create():
    db.create_all()
    db.session.commit()

@app.route('/')
def index():
    # myClippings = Clipboard.query.all()
    myClippings = Clipboard.query.filter_by(userId=0).all()
    return render_template('post.html', myClippings=myClippings)

@app.route('/post', methods=['POST'])
def post():
    userId = 0
    clip = Clipboard(userId,request.form['clipping'],datetime.now())
    db.session.add(clip)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/profile/<email>')
def profile(email):
    
    user = User.query.filter_by(email=email).first()
    return render_template('profile.html', user=user)


if __name__ == "__main__":  #make sure the app will be run on it's own, not as API
    
    app.run()