from app import db 

loans = db.Table('loans',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, unique=True)
    author = db.Column(db.String(120))
    genre = db.Column(db.String(64)) # literary, scifi, romance, fantasy, western, children
    borrowers = db.relationship('User', secondary=loans, backref='books')

    def __repr__(self):
        return '<Book {}>'.format(self.title)

    def checked_out(self):
        return self.borrowers
    
    def checkout(self, user):
        if not self.checked_out():
            self.borrowers.append(user)
        
    
    def checkin(self, user):
        if user in self.borrowers:
            self.borrowers.remove(user)
    
    