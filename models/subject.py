from app.db import db


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    homework = db.relationship('Homework', backref='subject', lazy=True)
    books = db.relationship('Books', backref='subject', lazy=True)
    schedule = db.relationship('Schedule', backref='subject', lazy=True)
