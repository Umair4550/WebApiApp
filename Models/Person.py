from db import db  # Import the db object

class Person(db.Model):
    __tablename__ = 'Person'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Matches INT IDENTITY(1,1)
    Name = db.Column(db.String(50), nullable=True)  # Matches NVARCHAR(50)
    Phno = db.Column(db.String(45), nullable=True)  # Matches NVARCHAR(45)
    Password = db.Column(db.String(45), nullable=True)  # Matches NVARCHAR(45)
    Profile_Url = db.Column(db.String(90), nullable=True)  # Matches NVARCHAR(90)
    isDeleted = db.Column(db.Boolean, default=False, nullable=False)  # Matches BIT NOT NULL DEFAULT 0
    chats = db.relationship('Chat', backref='Person', lazy=True)
    def __repr__(self):
        return f"<Person {self.Name}>"

    def as_dict(self):

        return {
            'id': self.id,
            'Name': self.Name,
            'Phno': self.Phno,
            'Password': self.Password,
            'Profile_Url': self.Profile_Url,
            'isDeleted': self.isDeleted
        }

