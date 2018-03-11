from ..db.schema.measurements import Measurements

from .queries import insert_element
from .queries import delete_element
from .queries import get_measurement_by_id
from .queries import get_measurement_by_name


class MeasurementsModels(object):
    @staticmethod
    def add(name, fullname):
        if get_measurement_by_name(name):
            raise RuntimeError("Measurement already exist")

        measurement = Measurements(name=name, fullname=fullname)
        insert_element(measurement)

    @staticmethod
    def delete(name):
        measurement = get_measurement_by_id(id)
        if not measurement:
            raise RuntimeError("Measurement not found")

        delete_element(measurement)
