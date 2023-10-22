from abc import ABC, abstractmethod
from typing import List


class Tires(ABC):
    def __init__(self, tire_wear: List[float]) -> None:
        self.tire_wear = tire_wear

    @abstractmethod
    def needs_service(self) -> bool:
        pass
