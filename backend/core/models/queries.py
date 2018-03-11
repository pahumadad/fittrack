from ..db.db import db
from ..db.schema.users import Users as u
from ..db.schema.measurements import Measurements as m


def delete_element(element):
    db.session.delete(element)
    db.session.commit()


def insert_element(element):
    db.session.add(element)
    db.session.commit()


def get_user_by_id(id):
    return u.query.filter_by(id=id).first()


def get_user_by_email(email):
    return u.query.filter_by(email=email).first()


def get_measurement_by_id(m_id):
    return m.query.filter_by(id=m_id).first()


def get_measurement_by_name(name):
    return m.query.filter_by(name=name).first()
