from db import db

class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Matches [Chat_id] in the table
    Question = db.Column(db.Text, nullable=True)  # Matches NVARCHAR(MAX) in the table
    Answer = db.Column(db.Text, nullable=True)  # Matches NVARCHAR(MAX) in the table
    Time = db.Column(db.Time, nullable=True)
    Date = db.Column(db.Date, nullable=True)
    Person_Id = db.Column(db.Integer,db.ForeignKey('Person.id'))  # Foreign key for Person
    Session_Id = db.Column(db.Integer,db.ForeignKey('session.id'))  # Foreign ky for Session
    Program_Id = db.Column(db.Integer,db.ForeignKey('Program.id'))  # Foreign key for Program
    Category_id = db.Column(db.Integer,db.ForeignKey('category.id'))  # Foreign key for Category
    isDeleted = db.Column(db.Boolean, nullable=False, default=False)  # Matches BIT DEFAULT 0 in the table

    def as_dict(self):
        return {
            'id': self.id,
            'Question': self.Question,
            'Answer': self.Answer,
            'Time': self.Time.strftime("%H:%M:%S") if self.Time else None,
            'Date': self.Date.isoformat() if self.Date else None,
            'Person_Id': self.Person_Id,
            'Session_Id': self.Session_Id,
            'Program_Id': self.Program_Id,
            'Category_id': self.Category_id,
            'isDeleted': self.isDeleted
        }

