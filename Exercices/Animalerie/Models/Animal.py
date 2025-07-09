from datetime import datetime
from enums.sex_enum import Sex

class Animal():
    def __init__(self, name: str, weight: int, 
            size: int, sex: bool, age: int, 
            arrival: datetime, death_prob: float, sound: str):
        self.name = name
        self.weight = weight
        self.size = size
        self.sex = sex
        self.age = age
        self.arrival = arrival
        self.death_prob = death_prob
        self.sound = sound

    def cry(self) -> None:
        print(self.sound)

    def __str__(self):
        return f"{self.name} {self.weight} {self.age}"