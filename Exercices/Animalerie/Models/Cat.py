from Models.Animal import Animal
from datetime import datetime

class Cat(Animal):
    def __init__(self, name: str, weight: int, 
            size: int, sex: bool, age: int, 
            arrival: datetime, caractere: str,
            claws: bool, furLength: bool):
        super().__init__(name, weight, 
            size, sex, age, arrival, 0.5, "meow")
        self.caractere = caractere
        self.claws = claws
        self.furLength = furLength