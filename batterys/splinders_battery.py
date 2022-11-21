from abc import ABC
from battery import Battery
from datetime import datetime


class SplindersBattery(Battery,ABC):
    def __init__(self, last_service_date,current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def battery_should_be_serviced(self):

        if self.last_service_date + self.current_date > datetime.today():
            return True

        else:
            return False    
