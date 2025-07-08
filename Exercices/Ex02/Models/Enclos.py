class Enclos:
    __name = 'Enclos'
    __max = 10
    __size = 15
    __animals = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, value):
        if value < 0:
            raise ValueError('Max cannot be negative')
        self.__max = value

    @property
    def size(self):
        return self.__size

    @property
    def animals(self):
        return self.__animals