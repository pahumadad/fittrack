from ..db import db


class BFP(db.Model):
    __tablename__ = "bfp"
    id = db.Column(db.Integer, primary_key=True)
    female_up_limit = db.Column(db.Float)
    male_up_limit = db.Column(db.Float)
    conclusion = db.Column(db.String(120))
