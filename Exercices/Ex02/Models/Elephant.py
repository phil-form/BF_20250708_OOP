from Models.Soigneur import Soigneur


class Elephant:
    __name = 'Test'
    __famished = 0
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
    def famished(self):
        return self.__famished

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
