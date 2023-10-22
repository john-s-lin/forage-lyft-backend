import unittest
from datetime import datetime

from src.battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        today = datetime.today().date()
        battery = NubbinBattery(
            last_service_date=today.replace(year=today.year - 4), current_date=today
        )
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        battery = NubbinBattery(
            last_service_date=today.replace(year=today.year - 3), current_date=today
        )
        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
