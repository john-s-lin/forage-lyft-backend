from src.tires.tires import Tires


class CarriganTires(Tires):
    def needs_service(self) -> bool:
        return any([x >= 0.9 for x in self.tire_wear])
