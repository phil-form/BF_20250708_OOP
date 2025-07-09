import random
from abc import ABC, abstractmethod

from Models.Soigneur import Soigneur


class Animal:
    def __init__(self, name, appetite, care_taker):
        self.__name = name
        self.__hunger = appetite
        self.__happnies = 100
        self.__alive = True
        self.__caretaker = care_taker
        self._thirst = 0

    @abstractmethod
    def observe_env(self):
        pass

    @abstractmethod
    def ramasser_objet(self):
        pass

    @property
    @abstractmethod
    def proba_deces(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def appetite(self):
        return self.__hunger

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
        self.__hunger = 0

    def drink(self):
        self._thirst = 0

    def pet(self):
        self.__happnies = 100

    @property
    def info(self):
        return f'{self.name} | {self.__hunger} | {self.happnies} | {self.alive}'

    def reset(self):
        self.__happnies = 0
        self.__alive = True
        self.__hunger = 100

    def comportement_hasard(self):
        nbr = random.randint(1, 2)

        if nbr == 1:
            self.drink()
        elif nbr == 2:
            self.eat()