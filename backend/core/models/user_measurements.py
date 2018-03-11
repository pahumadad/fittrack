from ..db.schema.user_measurements import UserMeasurements

from .queries import insert_elements
from .queries import get_user_by_id
from .queries import get_measurement_by_id
from .queries import get_user_measurement
from .queries import delete_user_measurements


class UserMeasurementsModels(object):
    @staticmethod
    def add(user_id, measurements):
        if not get_user_by_id(user_id):
            raise RuntimeError("User not found")

        elements = []
        for m_id in set(measurements):
            if not get_measurement_by_id(m_id):
                raise RuntimeError("Measurement not found")

            if get_user_measurement(user_id, m_id):
                continue

            elements.append(UserMeasurements(user=user_id,
                                             measurement=m_id))

        insert_elements(elements)

    @staticmethod
    def delete(user_id, measurements):
        delete_user_measurements(user_id, measurements)
