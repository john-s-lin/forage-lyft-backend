import unittest

from src.engine.capulet_engine import CapuletEngine
from src.engine.sternman_engine import SternmanEngine
from src.engine.willoughby_engine import WilloughbyEngine


class TestEngine(unittest.TestCase):
    def test_capulet_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=30001, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_capulet_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=29999, last_service_mileage=0)
        self.assertFalse(engine.needs_service())

    def test_sternman_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_sternman_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())

    def test_willoughby_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=60001, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_willoughby_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=59999, last_service_mileage=0)
        self.assertFalse(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
