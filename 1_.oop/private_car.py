class PrivateCar:
    def __init__(self, color, speed):
        self.color = color
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def __drive(self):
        print(f"The {self.color} car is driving at {self.__speed}mph.")

    def stop(self):
        print(f"The {self.color} car has stopped.")

my_car = PrivateCar("Red", 50)
