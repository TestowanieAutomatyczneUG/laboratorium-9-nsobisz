from src.Car import Car

class CarImpl:

    def __init__(self, car: Car):
        self.car = car

    def needs_fuel_check(self):
        if self.car.needsFuel()==True:
            return "Musisz zatankować"
        else:
            return "Masz wystarczająco paliwa"

    def get_engine_temperature_check(self):
        if self.car.getEngineTemperature()<80:
            return "Silnik ma za niską temperaturę"
        elif self.car.getEngineTemperature()>95:
            return "Silnik ma za wysoką temperaturę"
        else:
            return "Silnik ma prawidłową temperaturę"


    def drive_to_check(self, destination):
        return "Jadę do " + self.car.driveTo(destination)
