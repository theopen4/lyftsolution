from abc import ABC
from serviceable import Serviceable


class Engine(Serviceable, ABC):
    def __init__(self,last_service_date):
        super().__init__(last_service_date)
        """add property"""

     