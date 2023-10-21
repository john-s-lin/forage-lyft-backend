import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    def create_calliope(
        current_date: datetime.date,
        last_service_date: datetime.date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(
        current_date: datetime.date,
        last_service_date: datetime.date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(
        current_date: datetime.date,
        last_service_date: datetime.date,
        warning_light_on: bool,
    ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(
        current_date: datetime.date,
        last_service_date: datetime.date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(
        current_date: datetime.date,
        last_service_date: datetime.date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
