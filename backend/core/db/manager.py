from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from backend.core.app import app
from backend.core.db.db import db
from backend.core.db.schema.users import Users
from backend.core.db.schema.measurements import Measurements
from backend.core.db.schema.user_measurements import UserMeasurements
from backend.core.db.schema.measurements_sessions import MeasurementsSessions


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
