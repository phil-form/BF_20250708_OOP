from Exercices.Exo3.Models.Animal import Animal


class Girafe(Animal):
    longeur_cou = 0
    def __init__(self,  name, appetite, care_taker, longeur_cou):
        super().__init__(name, appetite, care_taker)
        self.__longeur_cou = longeur_cou
        self.__thirst = 0

    def manger_feuille(self):
        self.eat()

    def drink_water(self):
        self._thirst -= 1


girafe = Girafe(50)

print(girafe.__dict__)
print(girafe.longeur_cou)
girafe.longeur_cou = 5
print(girafe.__dict__)
print(Girafe.longeur_cou)
