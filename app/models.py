from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
from app import errors
from app.errors import ItemUnvailableError, CannotCheckInError

loans = db.Table('loans',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, unique=True)
    author = db.Column(db.String(120))
    genre = db.Column(db.String(64)) # literary, scifi, romance, fantasy, western, children
    borrowers = db.relationship('User', secondary=loans, backref='books')

    def __repr__(self):
        return '<Book {}>'.format(self.title)

    def available(self):
        return self.borrowers == []
    
    def checkout(self, user):
        if not self.available():
            raise ItemUnvailableError
        
        self.borrowers.append(user)
        db.session.commit()
             
    def checkin(self, user):
        if self.available() or user not in self.borrowers:
            raise CannotCheckInError
           
        self.borrowers.remove(user)
        db.session.commit()
    
    