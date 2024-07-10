from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.car_engine = engine
        self.car_battery = battery
        self.car_tire = tire

    def needs_service(self):
        if car_engine.needs_service() or car_battery.needs_service() or car_tire.needs_service():
            return True
        return False
