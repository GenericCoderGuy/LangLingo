from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    def hash_my_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_my_password(self, password):
        return check_password_hash(self.password, password)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    body = db.Column(db.String(1200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1200))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    languageOriginal = db.Column(db.String(250))
    languageTranslated = db.Column(db.String(250))
    textOriginal = db.Column(db.String(1200))
    textTranslated = db.Column(db.String(1200))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)