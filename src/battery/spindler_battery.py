import datetime

from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(
        self, last_service_date: datetime.date, current_date: datetime.date
    ) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date > datetime.timedelta(
            days=(365 * 2)
        )
