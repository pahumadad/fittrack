from ..db import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    gender = db.Column(db.String(6))
    height = db.Column(db.Float)
    age = db.Column(db.Integer)