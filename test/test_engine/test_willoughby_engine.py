import unittest

from src.engine.willoughby_engine import WilloughbyEngine


class TestEngine(unittest.TestCase):
    def test_willoughby_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=60001, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_willoughby_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=59999, last_service_mileage=0)
        self.assertFalse(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
