from car import Car

class SportsCar(Car): 
    def __init__(self, color, speed, horsepower):
        super().__init__(color, speed)
        self.horsepower = horsepower # Additional attribute

    def drive(self): #Overrides parent class drive method
        print(f"The {self.horsepower} horsepower {self._color} sports car is driving at {self._speed}mph.")

my_car = Car("Blue", 40)
my_sportscar = SportsCar("Black", 150, 500)
