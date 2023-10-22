import unittest

from src.tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_carrigan_tires_should_be_serviced(self):
        tires = CarriganTires([0, 0, 0.9, 0])
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_should_not_be_serviced(self):
        tires = CarriganTires([0.89, 0.89, 0.89, 0.89])
        self.assertFalse(tires.needs_service())
