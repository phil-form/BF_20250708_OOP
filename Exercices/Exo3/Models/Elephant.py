from Models.Soigneur import Soigneur
from Models.Animal import Animal

class Elephant(Animal):
    def __init__(self, name, appetite, care_taker, horn_length):
        super().__init__(name, appetite, care_taker)
        self.horn_length = horn_length

    def bain_de_boue(self):
        self.happnies += 1

    def apirer_eau(self):
        self._thirst -= 1

    def observe_env(self):
        super().observe_env()
        self._thirst += 1

