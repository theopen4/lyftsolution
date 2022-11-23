import unittest
from datetime import datetime
from batterys.splinders_battery import SplinderBattery
from batterys.nubbin_battery import NubbinBattery
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from cars_factory import Car
from cars_factory import CarFactory
from utils import add_years_to_date

class TestCalliope(unittest.TestCase):
      def capulet_needservice(self):
          current_date = datetime.today().date()
          last_sevice_date = last_service_date = current_date.replace(year=current_date.year - 3)
          current_mileage = 0
          last_service_mileage = 0
          result = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
          return result

test = TestCalliope()
print (test.capulet_needservice)
