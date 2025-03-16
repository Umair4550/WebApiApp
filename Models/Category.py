from db import db

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(90), nullable=True)
    isDeleted = db.Column(db.Boolean, nullable=False, default=False)  # Matches BIT DEFAULT 0 in the table
    chats = db.relationship('Chat', backref='category', lazy=True)

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'isDeleted': self.isDeleted
        }
