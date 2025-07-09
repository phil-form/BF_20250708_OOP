from Models.Soigneur import Soigneur


class Animal:
    def __init__(self, name, appetite, care_taker):
        self.__name = name
        self.__appetite = appetite
        self.__happnies = 100
        self.__alive = True
        self.__caretaker = care_taker
        self._thirst = 0

    def observe_env(self):
        self.__happnies += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def appetite(self):
        return self.__appetite

    @property
    def happnies(self):
        return self.__happnies

    @property
    def alive(self):
        return self.__alive

    @property
    def caretaker(self):
        return self.__caretaker

    @caretaker.setter
    def caretaker(self, value):
        if not isinstance(value, Soigneur):
            raise TypeError('caretaker must be a Soigneur')

        self.__caretaker = value


    def eat(self):
        self.__appetite = 0

    def pet(self):
        self.__happnies = 100

    @property
    def info(self):
        return f'{self.name} | {self.__appetite} | {self.happnies} | {self.alive}'

    def reset(self):
        self.__happnies = 0
        self.__alive = True
        self.__appetite = 100