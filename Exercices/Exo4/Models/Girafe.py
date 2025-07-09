from Exercices.Exo3.Models.Animal import Animal
import random

class Girafe(Animal):
    longeur_cou = 0
    def __init__(self,  name, appetite, care_taker, longeur_cou):
        super().__init__(name, appetite, care_taker)
        self.__longeur_cou = longeur_cou
        self.__thirst = 0

    def observe_env(self):
        print("Girafe objet")

    def ramasser_objet(self):
        print("Ramasser objet")

    def manger_feuille(self):
        self.eat()

    def drink_water(self):
        self._thirst -= 1

    def comportement_hasard(self):
        nbr = random.randint(1, 2)

        if nbr == 1:
            self.manger_feuille()
        elif nbr == 2:
            self.drink_water()

    @property
    def proba_deces(self):
        return 0.4


girafe = Girafe(50)

print(girafe.__dict__)
print(girafe.longeur_cou)
girafe.longeur_cou = 5
print(girafe.__dict__)
print(Girafe.longeur_cou)
