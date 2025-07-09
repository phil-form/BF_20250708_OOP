import datetime


class Soigneur:
    __name = ''
    __birth_date = datetime.datetime(2000, 1,1)
    __experience = 0
    __animal_nbr = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def age(self):
        if not isinstance(self.__birth_date, datetime.datetime):
            raise AttributeError("birth_date must be of type datetime.datetime")

        today = datetime.date.today()
        return today.year - self.__birth_date.year

    @property
    def experience(self):
        return self.__experience

    @property
    def animal_nbr(self):
        return self.__animal_nbr

    def nourrir(self, animal):
        animal.eat()

    def pet(self, animal):
        animal.pet()