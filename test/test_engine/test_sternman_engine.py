import unittest

from src.engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_sternman_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_sternman_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
