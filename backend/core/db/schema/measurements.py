from ..db import db


class Measurements(db.Model):
    __tablename__ = "measurements"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    fullname = db.Column(db.String(120))
