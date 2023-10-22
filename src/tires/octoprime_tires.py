from src.tires.tires import Tires


class OctoprimeTires(Tires):
    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3
