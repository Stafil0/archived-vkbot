from service import db


class Schedules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Binary)
