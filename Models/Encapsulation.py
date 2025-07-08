class Voiture:
    __marque = "Toyota"
    __matricule = "1-ABC-123"
    __speed = 0
    _test = 5
    __test2 = 5

    @property
    def marque(self):
        return self.__marque

    @marque.setter
    def marque(self, value):
        self.__marque = value

    @marque.deleter
    def marque(self):
        del self.__marque

    # Read only
    @property
    def matricule(self):
        return self.__matricule

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("Speed must be an integer or a float")

        if value < 0 or value > 150:
            raise ValueError("Speed must be between 0 and 150")

        self.__speed = value

car = Voiture()
# appel le getter
print(car.marque)
# Appel le setter
car.marque = 'Mercedes'
print(car.marque)
print(car.__dict__)
del car.marque
car.marque = 'BMW'
print(car.__dict__)
# car.matricule = '1-ABC-124'

# Simple vs double underscore
# le double underscore permet de retourner une execption en cas de tentative d'accès
# ce qui n'est pas le cas du simple underscore qui ne fait que mettre un avertissement
# dans l'IDE.
# Le simple underscore est donc plus à voir comme étant un avertissement qu'il ne faut
# pas utiliser cette variable directement (et
print(car._test)
car._test = 55
print(car._test)

print(car.__test2)
car.__test2 = 55
print(car.__test2)
