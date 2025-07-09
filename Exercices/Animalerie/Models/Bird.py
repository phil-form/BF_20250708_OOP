from Models.Animal import Animal
from datetime import datetime

class Bird(Animal):
    def __init__(self, name: str, weight: int, 
            size: int, sex: bool, age: int, 
            arrival: datetime, color: str,
            cageType: bool):
        super().__init__(name, weight, 
            size, sex, age, arrival, 1, "cuicui")
        self.color = color
        self.cageType = cageType