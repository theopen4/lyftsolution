from abc import ABC, abstractmethod


class Serviceable(ABC):
    def __init__(self,last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def need_service(self):
        service = True
        return service
        