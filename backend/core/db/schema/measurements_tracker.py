from ..db import db


class MeasurementsTracker(db.Model):
    __tablename__ = "measurements_tracker"
    id = db.    Column(db.Integer, primary_key=True)
    session = db.Column(db.Integer,
                        db.ForeignKey("measurements_sessions.id"),
                        nullable=False)
    measurement = db.Column(db.Integer,
                            db.ForeignKey("measurements.id"),
                            nullable=False)
    value = db.Column(db.Float)
    conclusion = db.Column(db.String(120), nullable=True)
