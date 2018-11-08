from app.db import db


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    file = db.Column(db.Binary, nullable=False)