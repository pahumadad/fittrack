from ..db import db


class Visceral(db.Model):
    __tablename__ = "visceral"
    id = db.Column(db.Integer, primary_key=True)
    up_limit = db.Column(db.Float)
    conclusion = db.Column(db.String(120))
