from private_car import PrivateCar

class SpeedChecker:
    def check_speed(self, car):
        try:
            return car.get_speed()
        except AttributeError:
            return "The car object does not have a speed attribute"

red_car = PrivateCar("Red", 120)

speed_checker = SpeedChecker()
print( "Speed of car is " + str(speed_checker.check_speed(red_car))) 