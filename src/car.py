from abc import abstractmethod
from engine.engine import Engine
from battery.battery import Battery
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
