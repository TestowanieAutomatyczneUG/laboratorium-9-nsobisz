from src.CarImpl import *
from src.Car import *
from unittest.mock import *
from unittest import TestCase, main

class test_Car(TestCase):
    def test_need_fuel_false(self):
        test_object = Car()
        test_object.needsFuel = Mock(name = 'needsFuel')
        test_object.needsFuel.return_value = False


        test_object_2 = CarImpl(test_object)
        self.assertEqual(test_object_2 .needs_fuel_check(), "Masz wystarczająco paliwa")

    def test_need_fuel_true(self):
        test_object = Car()
        test_object.needsFuel = Mock(name='needsFuel')
        test_object.needsFuel.return_value = True

        test_object_2 = CarImpl(test_object)
        self.assertEqual(test_object_2.needs_fuel_check(), "Musisz zatankować")



    def test_engine_temperature_too_low(self):
        test_object = Car()
        test_object.getEngineTemperature = Mock(name='getEngineTemperature')
        test_object.getEngineTemperature.return_value = 20

        test_object_2 = CarImpl(test_object)
        self.assertEqual(test_object_2.get_engine_temperature_check(), "Silnik ma za niską temperaturę")

    def test_engine_temperature_too_high(self):
        test_object = Car()
        test_object.getEngineTemperature = Mock(name='getEngineTemperature')
        test_object.getEngineTemperature.return_value = 200

        test_object_2 = CarImpl(test_object)
        self.assertEqual(test_object_2.get_engine_temperature_check(), "Silnik ma za wysoką temperaturę")

    def test_engine_temperature_good(self):
        test_object = Car()
        test_object.getEngineTemperature = Mock(name='getEngineTemperature')
        test_object.getEngineTemperature.return_value = 90

        test_object_2 = CarImpl(test_object)
        self.assertEqual(test_object_2.get_engine_temperature_check(), "Silnik ma prawidłową temperaturę")

    def test_drive_to_paryz(self):
        test_object = Car()
        test_object.driveTo = Mock(name='driveTo')
        test_object.driveTo.return_value = "Paryż"

        test_object_2 = CarImpl(test_object)
        self.assertEqual(test_object_2.drive_to_check("Paryż"), "Jadę do Paryż")

    def test_drive_to_tokio(self):
        test_object = Car()
        test_object.driveTo = Mock(name='driveTo')
        test_object.driveTo.return_value = "Tokio"

        test_object_2 = CarImpl(test_object)
        self.assertEqual(test_object_2.drive_to_check("Tokio"), "Jadę do Tokio")




if __name__ == '__main__':
    main()
