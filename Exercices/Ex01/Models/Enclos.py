class Enclos:
    nom = ''
    max_capacity = 10
    size = 50
    animals = []

    def ajouter_animal(self, animal):
        self.animals.append(animal)

    def remover_animal(self, animal):
        self.animals.remove(animal)

    def afficher_animal(self):
        print("Animaux dans l'enclos : ")
        for animal in self.animals:
            print(animal.name)