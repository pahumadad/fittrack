from ..db import db
from .measurements_tracker import MeasurementsTracker


class MeasurementsSessions(db.Model):
    __tablename__ = "measurements_sessions"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date = db.Column(db.DateTime)
    trackers = db.relationship("MeasurementsTracker",
                               backref="measurements_sessions",
                               lazy="dynamic",
                               foreign_keys="MeasurementsTracker.session")
