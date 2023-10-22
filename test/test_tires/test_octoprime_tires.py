import unittest

from src.tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_octoprime_tires_should_be_serviced(self):
        tires = OctoprimeTires([1, 1, 1, 0])
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_should_not_be_serviced(self):
        tires = OctoprimeTires([0.7, 0.7, 0.7, 0.8])
        self.assertFalse(tires.needs_service())
