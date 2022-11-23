from batterys.splinders_battery import SplinderBattery
from batterys.nubbin_battery import NubbinBattery
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from cars_factory import Car

class CarFactory:
      @staticmethod
      def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

      @staticmethod
      def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

      @staticmethod
      def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SplinderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

      @staticmethod
      def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

      @staticmethod
      def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
