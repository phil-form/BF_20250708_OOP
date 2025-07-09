from Models.Animal import Animal
from datetime import datetime

class Dog(Animal):
    def __init__(self, name: str, weight: int, 
            size: int, sex: bool, age: int, 
            arrival: datetime, colar: str,
            trained: bool, race: str):
        super().__init__(name, weight, 
            size, sex, age, arrival, 1, "whouf")
        self.colar = colar
        self.trained = trained
        self.race = race