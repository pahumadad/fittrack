from ..db.db import db
from ..db.schema.users import Users
from ..db.schema.measurements import Measurements
from ..db.schema.user_measurements import UserMeasurements
from ..db.schema.measurements_tracker import MeasurementsTracker
from ..db.schema.measurements_sessions import MeasurementsSessions
from ..db.schema.bfp import BFP
from ..db.schema.bmi import BMI
from ..db.schema.muscle import Muscle
from ..db.schema.visceral import Visceral


def delete_element(element):
    db.session.delete(element)
    db.session.commit()


def insert_element(element):
    db.session.add(element)
    db.session.commit()


def insert_elements(elements):
    db.session.bulk_save_objects(elements)
    db.session.commit()


def get_user_by_id(id):
    return Users.query.filter_by(id=id).first()


def get_user_by_email(email):
    return Users.query.filter_by(email=email).first()


def get_user_measurement(u_id, m_id):
    return Measurements.query \
        .join(UserMeasurements) \
        .filter(Measurements.id == m_id) \
        .join(Users) \
        .filter(Users.id == u_id) \
        .all()


def get_user_measurements(user_id):
    return Measurements.query \
        .join(UserMeasurements) \
        .join(Users) \
        .filter(Users.id == user_id) \
        .all()


def get_user_measurements_sessions(user_id):
    return MeasurementsSessions.query \
        .filter_by(user=user_id) \
        .order_by(MeasurementsSessions.date.desc(),
                  MeasurementsSessions.id.desc()) \
        .all()


def get_user_measurements_tracks(u_id, m_id):
    return MeasurementsTracker.query \
        .filter(MeasurementsTracker.measurement == m_id) \
        .join(MeasurementsSessions) \
        .filter(MeasurementsSessions.user == u_id) \
        .all()


def get_measurement_by_id(m_id):
    return Measurements.query.filter_by(id=m_id).first()


def get_measurement_by_name(name):
    return Measurements.query.filter_by(name=name).first()


def delete_user_measurements(user_id, measurements):
    stmt = UserMeasurements.__table__.delete() \
        .where(UserMeasurements.user == user_id) \
        .where(UserMeasurements.measurement.in_(measurements))
    db.engine.execute(stmt)


def get_measurements_session_by_id(m_s_id):
    return MeasurementsSessions.query.filter_by(id=m_s_id).first()


def get_measurements_tracker_by_id(m_t_id):
    return MeasurementsTracker.query.filter_by(id=m_t_id).first()


def get_bfp_conclusion(value, gender):
    if gender == "female":
        return BFP.query.filter(BFP.female_up_limit >= value).first()
    elif gender == "male":
        return BFP.query.filter(BFP.male_up_limit >= value).first()
    else:
        return None


def get_bmi_conclusion(value):
    return BMI.query.filter(BMI.up_limit >= value).first()


def get_muscle_conclusion(value, gender):
    if gender == "female":
        return Muscle.query.filter(Muscle.female_up_limit >= value).first()
    elif gender == "male":
        return Muscle.query.filter(Muscle.male_up_limit >= value).first()
    else:
        return None


def get_visceral_conclusion(value):
    return Visceral.query.filter(Visceral.up_limit >= value).first()
