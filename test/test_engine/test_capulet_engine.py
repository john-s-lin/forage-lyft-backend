import unittest

from src.engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=30001, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=29999, last_service_mileage=0)
        self.assertFalse(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
