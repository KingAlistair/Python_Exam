class Car:
    def __init__(self, color, speed):
        self._color = color
        self._speed = speed

    def drive(self):
        print(f"The {self._color} car is driving at {self._speed}mph.")

    def stop(self):
        print(f"The {self._color} car has stopped.")

my_car = Car("Red", 50)
new_car = Car("Blue", 60)