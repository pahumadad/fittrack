from ..db import db
from .user_measurements import UserMeasurements


class Measurements(db.Model):
    __tablename__ = "measurements"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    fullname = db.Column(db.String(120))
    users = db.relationship("UserMeasurements",
                            backref="measurements",
                            lazy="dynamic",
                            foreign_keys="UserMeasurements.measurement")
