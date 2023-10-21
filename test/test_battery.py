import unittest
from datetime import datetime

from src.battery.nubbin_battery import NubbinBattery
from src.battery.spindler_battery import SpindlerBattery


class TestBattery(unittest.TestCase):
    def test_nubbin_should_be_serviced(self):
        today = datetime.today().date()
        battery = NubbinBattery(
            last_service_date=today.replace(year=today.year - 4), current_date=today
        )
        self.assertTrue(battery.needs_service())

    def test_nubbin_should_not_be_serviced(self):
        today = datetime.today().date()
        battery = NubbinBattery(
            last_service_date=today.replace(year=today.year - 3), current_date=today
        )
        self.assertFalse(battery.needs_service())

    def test_spindler_should_be_serviced(self):
        today = datetime.today().date()
        battery = SpindlerBattery(
            last_service_date=today.replace(year=today.year - 3), current_date=today
        )
        self.assertTrue(battery.needs_service())

    def test_spindler_should_not_be_serviced(self):
        today = datetime.today().date()
        battery = SpindlerBattery(
            last_service_date=today.replace(year=today.year - 1), current_date=today
        )
        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
