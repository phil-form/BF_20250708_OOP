from Models.Soigneur import Soigneur


class Elephant:
    __name = 'Test'
    __hunger = 0
    __happnies = 0
    __alive = True
    __caretaker = None

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

    def pet(self):
        self.__happnies = 100

    @property
    def info(self):
        return f'{self.name} | {self.__hunger} | {self.happnies} | {self.alive}'

    def reset(self):
        self.__happnies = 0
        self.__alive = True
        self.__hunger = 100