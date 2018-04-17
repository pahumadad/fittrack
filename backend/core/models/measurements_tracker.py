from ..db.schema.measurements_tracker import MeasurementsTracker

from .queries import insert_element
from .queries import delete_element
from .queries import get_user_by_id
from .queries import get_measurement_by_id
from .queries import get_measurements_session_by_id
from .queries import get_measurements_tracker_by_id
from .queries import get_bfp_conclusion
from .queries import get_bmi_conclusion
from .queries import get_muscle_conclusion
from .queries import get_visceral_conclusion


class MeasurementsTrackerModels(object):
    @staticmethod
    def add(u_id, m_id, s_id, value):
        user = get_user_by_id(u_id)
        if not user:
            raise RuntimeError("User not found")

        msr = get_measurement_by_id(m_id)
        if not msr:
            raise RuntimeError("Measurement not found")

        if not get_measurements_session_by_id(s_id):
            raise RuntimeError("Session not found")

        conclusion = MeasurementsTrackerModels.get_conclusion(
            msr.name, user.gender, value
        )

        m_track = MeasurementsTracker(session=s_id,
                                      measurement=m_id,
                                      value=value,
                                      conclusion=conclusion)

        insert_element(m_track)

    @staticmethod
    def delete(m_t_id):
        m_track = get_measurements_tracker_by_id(m_t_id)
        if not m_track:
            raise RuntimeError("Measurement session track not found")

        delete_element(m_track)

    @staticmethod
    def get_conclusion(msr, gender, value):
        if msr == "bfp":
            return get_bfp_conclusion(value, gender).conclusion
        elif msr == "bmi":
            return get_bmi_conclusion(value).conclusion
        elif msr == "muscle":
            return get_muscle_conclusion(value, gender).conclusion
        elif msr == "visceral":
            return get_visceral_conclusion(value).conclusion
        else:
            return None
