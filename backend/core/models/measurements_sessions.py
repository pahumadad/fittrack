from datetime import datetime

from ..db.schema.measurements_sessions import MeasurementsSessions

from .queries import insert_element
from .queries import delete_element
from .queries import get_user_by_id
from .queries import get_measurements_session_by_id


class MeasurementsSessionsModels(object):
    @staticmethod
    def add(user_id, date=False):
        if not get_user_by_id(user_id):
            raise RuntimeError("User not found")

        if not date:
            date = datetime.utcnow()

        if not isinstance(date, datetime):
            try:
                date = datetime.strptime(date, "%Y%m%d").date()
            except:
                raise RuntimeError("Wrong date format. Should be yyyymmdd")

        session = MeasurementsSessions(user=user_id, date=date)

        insert_element(session)

    @staticmethod
    def delete(m_s_id):
        session = get_measurements_session_by_id(m_s_id)
        if not session:
            raise RuntimeError("Measurement session not found")

        delete_element(session)
