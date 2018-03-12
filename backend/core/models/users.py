from ..db.schema.users import Users

from .queries import insert_element
from .queries import delete_element
from .queries import get_user_by_id
from .queries import get_user_by_email
from .queries import get_user_measurements
from .queries import get_user_measurements_sessions


class UsersModels(object):
    @staticmethod
    def add(name, email, gender=False, height=False, age=False):
        if get_user_by_email(email):
            raise RuntimeError("User already exist")

        user = Users(
            name=name,
            email=email,
            gender=gender,
            height=height,
            age=age
        )
        insert_element(user)

    @staticmethod
    def delete(id):
        user = get_user_by_id(id)
        if not user:
            raise RuntimeError("User not found")

        delete_element(user)

    @staticmethod
    def measurements(id):
        user = get_user_by_id(id)
        if not user:
            raise RuntimeError("User not found")

        return get_user_measurements(id)

    @staticmethod
    def measurements_sessions(id):
        user = get_user_by_id(id)
        if not user:
            raise RuntimeError("User not found")

        return get_user_measurements_sessions(id)
