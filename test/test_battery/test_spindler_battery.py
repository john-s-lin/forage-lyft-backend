import unittest
from datetime import datetime

from src.battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_should_be_serviced(self):
        today = datetime.today().date()
        battery = SpindlerBattery(
            last_service_date=today.replace(year=today.year - 4), current_date=today
        )
        self.assertTrue(battery.needs_service())

    def test_spindler_should_not_be_serviced(self):
        today = datetime.today().date()
        battery = SpindlerBattery(
            last_service_date=today.replace(year=today.year - 2), current_date=today
        )
        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
