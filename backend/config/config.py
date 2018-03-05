import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    APP_NAME = "fittrack"

    FITTRACK_DB_USER = os.environ.get("FITTRACK_DB_USER")
    FITTRACK_DB_PASS = os.environ.get("FITTRACK_DB_PASS")
    FITTRACK_DB_HOST = os.environ.get("FITTRACK_DB_HOST")
    FITTRACK_DB_NAME = os.environ.get("FITTRACK_DB_NAME")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
