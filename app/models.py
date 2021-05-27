from app import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    loans = db.relationship('Loan', backref='loan', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, unique=True)
    author = db.Column(db.String(120))
    genre = db.Column(db.String(64)) # literary, scifi, romance, fantasy, western, children
    borrowers = db.relationship('Loan', backref='borrower', lazy='dynamic')

    def __repr__(self):
        return '<Book {}>'.format(self.title)


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean(), default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))