from Models.Soigneur import Soigneur
from Models.Animal import Animal
import random

from Interface.IAnimal import IAnimal


class Elephant(Animal, IAnimal):
    def __init__(self, name, appetite, care_taker, horn_length):
        super().__init__(name, appetite, care_taker)
        self.horn_length = horn_length

    def manger(self):
        self.__hunger = 0

    def observer(self):
        print("Elephan observe")

    def faire_une_sieste(self):
        print("dodo")

    def proba_deces(self):
        return 6

    def diminuer_rassasier(self):
        self.__hunger = 0

    def diminuer_bonheur(self):
        self.happnies -= 1

    def bain_de_boue(self):
        self.happnies += 1

    def apirer_eau(self):
        self._thirst -= 1

    def observe_env(self):
        super().observe_env()
        self._thirst += 1

    def ramasser_objet(self):
        print("Ramasser objet")

    def comportement_hasard(self):
        nbr = random.randint(1, 5)

        if nbr == 1:
            self.drink()
        elif nbr == 2:
            self.eat()
        elif nbr == 3:
            self.observe_env()
        elif nbr == 4:
            self.apirer_eau()
        elif nbr == 5:
            self.bain_de_boue()

    @property
    def proba_deces(self):
        return 0.9


