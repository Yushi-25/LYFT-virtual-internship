from Battery.battery import Battery
from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery
from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car
from tire.octoprime_tire import OctoprimeTire
from tire.tire import Tire
from tire.carrigan_tire import CarriganTire

class CarFactory:

  def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire): 
    engine = CapuletEngine(current_mileage,last_service_mileage)
    battery = SpindlerBattery(current_date,last_service_date)
    tire = OctoprimeTire(tire)
    return Car(engine,battery,tire)
  def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,tire): 
    engine = WilloughbyEngine(current_mileage,last_service_mileage)
    battery = SpindlerBattery(current_date,last_service_date)
    tire = CarriganTire(tire)
    return Car(engine,battery,tire)
  def create_palindrome(current_date, last_service_date, warning_light_on, tire): 
    engine = SternmanEngine(warning_light_on)
    battery = SpindlerBattery(current_date,last_service_date)
    tire = OctoprimeTire(tire)
    rreturn Car(engine,battery,tire)
  def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tire):
    engine = WilloughbyEngine(current_mileage,last_service_mileage)
    battery = NubbinBattery(current_date,last_service_date)
    tire = CarriganTire(tire)
    return Car(engine,battery,tire)
  def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,tire):
    engine = CapuletEngine(current_mileage,last_service_mileage)
    battery = NubbinBattery(current_date,last_service_date)
    tire = OctoprimeTire(tire)
    return Car(engine,battery,tire)
