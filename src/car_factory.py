import datetime
from typing import List

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date: datetime.date,
        last_service_date: datetime.date,
        current_mileage: int,
        last_service_mileage: int,
        tire_wear: List[float],
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear=tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(
        current_date: datetime.date,
        last_service_date: datetime.date,
        current_mileage: int,
        last_service_mileage: int,
        tire_wear: List[float],
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_wear=tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(
        current_date: datetime.date,
        last_service_date: datetime.date,
        warning_light_on: bool,
        tire_wear: List[float],
    ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear=tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(
        current_date: datetime.date,
        last_service_date: datetime.date,
        current_mileage: int,
        last_service_mileage: int,
        tire_wear: List[float],
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_wear=tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(
        current_date: datetime.date,
        last_service_date: datetime.date,
        current_mileage: int,
        last_service_mileage: int,
        tire_wear: List[float],
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear=tire_wear)
        return Car(engine, battery, tires)
