class GameCharacter:
    def __init__(self, name, health):
        self._name = name
        self._health = health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health cannot be negative!")
        if value > 100:
            raise ValueError("Health cannot exceed 100!")
        self._health = value

character = GameCharacter("Player", 50)
