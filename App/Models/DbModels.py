from App.db import db

class Person(db.Model):
    __tablename__ = 'person'
    Pid = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Phno = db.Column(db.String(15))
    Password = db.Column(db.String(255))
    Profile_url = db.Column(db.String(255))


class Program(db.Model):
    __tablename__ = 'program'
    Pid = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))


class Session(db.Model):
    __tablename__ = 'session'
    Sid = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255))


class Category(db.Model):
    __tablename__ = 'category'
    Cid = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255))


class Chat(db.Model):
    __tablename__ = 'chat'
    Id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.Text)
    Answer = db.Column(db.Text)
    Date = db.Column(db.Date)
    Time = db.Column(db.Time)

    Pid = db.Column(db.Integer, db.ForeignKey('person.Pid'))
    Sid = db.Column(db.Integer, db.ForeignKey('session.Sid'))
    CategoryId = db.Column(db.Integer, db.ForeignKey('category.Cid'))
    Program_Id = db.Column(db.Integer, db.ForeignKey('program.Pid'))

    person = db.relationship('Person', backref=db.backref('chats', lazy=True))
    session = db.relationship('Session', backref=db.backref('chats', lazy=True))
    category = db.relationship('Category', backref=db.backref('chats', lazy=True))
    program = db.relationship('Program', backref=db.backref('chats', lazy=True))
