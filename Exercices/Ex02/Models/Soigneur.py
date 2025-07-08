class Soigneur:
    __name = ''
    __birth_date = ''
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
    def experience(self):
        return self.__experience

    @property
    def animal_nbr(self):
        return self.__animal_nbr