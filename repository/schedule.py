from service import db


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    starts = db.Column(db.DateTime, nullable=False)
    ends = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
