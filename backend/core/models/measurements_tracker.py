from ..db.schema.measurements_tracker import MeasurementsTracker

from .queries import insert_element
from .queries import delete_element
from .queries import get_measurement_by_id
from .queries import get_measurements_session_by_id
from .queries import get_measurements_tracker_by_id


class MeasurementsTrackerModels(object):
    @staticmethod
    def add(session_id, measurement_id, value, conclusion):
        if not get_measurements_session_by_id(session_id):
            raise RuntimeError("Session not found")

        if not get_measurement_by_id(measurement_id):
            raise RuntimeError("Measurement not found")

        m_track = MeasurementsTracker(session=session_id,
                                      measurement=measurement_id,
                                      value=value,
                                      conclusion=conclusion)

        insert_element(m_track)

    @staticmethod
    def delete(m_t_id):
        m_track = get_measurements_tracker_by_id(m_t_id)
        if not m_track:
            raise RuntimeError("Measurement session track not found")

        delete_element(m_track)
