from Models.Bird import Bird
from Models.Cat import Cat
from Models.Dog import Dog
from Models.Animal import Animal
from random import randrange
from utils.input_utils import *

class Rescue():
    def __init__(self) -> None:
        self.animals = []
        self.cat_count = 0
        self.dog_count = 0
        self.bird_count = 0

    def add_animal(self):
        choice = 0
        while not choice in [1, 2, 3]:
            choice = read_int("entrez \n1 -> chat \n2-> chien \n3 -> oiseau")
        
        name = read_str("Entrez le nom : ")
        poids = read_int("Entrez le poids : ")
        taille = read_int("Entrez la talle : ")
        age = read_int("Entrez l'age : ")
        sex = read_bool("Entrez le sex : ")
        arrivalDate = read_date("Entrez la date d'arrivée : ")
        
        animal = None

        if(choice == 1):
            caracter = read_str("Entrez le caractère : ")
            claws = read_bool("Entrez si les griffes sont coupées : ")
            furType = read_bool("Type de fourrure : ")
            animal = Cat(name, poids, taille, 
                        sex, age, arrivalDate,
                        caracter, claws, furType)
            self.cat_count += 1

        elif(choice == 2):
            colar = read_str("Couleur du colier : ")
            trained = read_bool("Est dressé : ")
            race = read_str("Race : ")

            animal = Dog(name, poids, taille, 
                        sex, age, arrivalDate,
                        colar, trained, race)

            self.dog_count += 1
        elif(choice == 3):
            color = read_str("Couleur : ")
            cageType = read_bool("Type de cage : ")  

            animal = Bird(name, poids, taille, 
                        sex, age, arrivalDate,
                        color, cageType)

            self.bird_count += 1

        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(animal)

    def show_stats(self):
        print(f"cats: {self.cat_count} dogs: {self.dog_count} birds: {self.bird_count}")

    def night(self):
        animal: Animal
        for animal in self.animals:
            if(animal.death_prob > randrange(100)):
                print(f"{animal.name} is dead :(")
                self.animals.remove(animal)

                if(isinstance(animal, Cat)):
                    self.cat_count -= 1
                elif(isinstance(animal, Dog)):
                    self.dog_count -= 1
                else:
                    self.bird_count -= 1
            
    