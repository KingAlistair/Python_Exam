class Cat:
    def __init__(self, name, color):
        self.name = name
        self._color = color


    @property   
    def color(self):
        return self._color
    
    @color.setter
    def color(self,value):
        if value != "red":
            print("Color can only be red")
        self._color = value
            



cat = Cat("Red", "red")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    

kate = Person("Kate", 20)

print(kate)