from db import db

class KnowledgeBase(db.Model):
    __tablename__ = 'KnowledgeBase'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(90), nullable=True)
    value = db.Column(db.String(90), nullable=True)
    isDeleted = db.Column(db.Boolean, nullable=False, default=False)
    def as_dict(self):
        return {
            'id': self.id,
            'key': self.key,
            'value': self.value,
            'isDeleted': self.isDeleted,

        }
