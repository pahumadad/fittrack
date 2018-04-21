from ..db import db


class Muscle(db.Model):
    __tablename__ = "muscle"
    id = db.Column(db.Integer, primary_key=True)
    female_up_limit = db.Column(db.Float)
    male_up_limit = db.Column(db.Float)
    conclusion = db.Column(db.String(120))
