from ..db import db


class UserMeasurements(db.Model):
    __tablename__ = "user_measurements"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    measurement = db.Column(db.Integer,
                            db.ForeignKey("measurements.id"),
                            nullable=False)
