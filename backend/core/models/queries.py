from ..db.db import db
from ..db.schema.users import Users
from ..db.schema.measurements import Measurements
from ..db.schema.user_measurements import UserMeasurements


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


def get_measurement_by_id(m_id):
    return Measurements.query.filter_by(id=m_id).first()


def get_measurement_by_name(name):
    return Measurements.query.filter_by(name=name).first()


def delete_user_measurements(user_id, measurements):
    stmt = UserMeasurements.__table__.delete() \
        .where(UserMeasurements.user == user_id) \
        .where(UserMeasurements.measurement.in_(measurements))
    db.engine.execute(stmt)
