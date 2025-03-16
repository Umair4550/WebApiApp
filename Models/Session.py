from db import db

class Session(db.Model):
    __tablename__ = 'session'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(90), nullable=True)
    isDeleted = db.Column(db.Boolean, default=False, nullable=False)  # Matches BIT NOT NULL DEFAULT 0
    chats = db.relationship('Chat', backref='session', lazy=True)

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'isDeleted': self.isDeleted
        }

