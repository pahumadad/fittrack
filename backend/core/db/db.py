from flask_sqlalchemy import SQLAlchemy

from ..app import app
from ...config.config import Config


app.config["SQLALCHEMY_DATABASE_URI"] = \
    "postgresql://{user}:{passwd}@{host}/{dbname}".format(
        user=Config.FITTRACK_DB_USER,
        passwd=Config.FITTRACK_DB_PASS,
        host=Config.FITTRACK_DB_HOST,
        dbname=Config.FITTRACK_DB_NAME
    )

db = SQLAlchemy(app)
