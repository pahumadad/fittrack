from ..db.db import db
from ..db.schema.users import Users


class UsersModels(object):
    @staticmethod
    def exist_user(email):
        if not get_user(email):
            return False

        return True

    @staticmethod
    def add_user(name, email, gender=False, height=False, age=False):
        if get_user(email):
            raise RuntimeError("User already exist")

        user = Users(
            name=name,
            email=email,
            gender=gender,
            height=height,
            age=age
        )
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def delete_user(email):
        user = get_user(email)
        if not user:
            raise RuntimeError("User not found")

        db.session.delete(user)
        db.session.commit()


def get_user(email):
    return Users.query.filter_by(email=email).first()
