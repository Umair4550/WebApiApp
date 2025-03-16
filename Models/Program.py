from db import db  # Import the db object

class Program(db.Model):
    __tablename__ = 'Program'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Matches INT IDENTITY(1,1)
    name = db.Column(db.String(90), nullable=True)  # Matches NVARCHAR(90)
    isDeleted = db.Column(db.Boolean, default=False, nullable=False)  # Matches BIT NOT NULL DEFAULT 0
    chats = db.relationship('Chat', backref='Program', lazy=True)

    def __repr__(self):
        return f"<Program {self.name}>"

    def as_dict(self):
        """Convert model instance to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'isDeleted': self.isDeleted
        }
