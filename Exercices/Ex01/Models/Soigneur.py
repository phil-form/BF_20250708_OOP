class Soigneur:
    name = ''
    date_naissance = ''
    experience = 0
    nombre_animaux = 0

    def nourrir(self, animal):
        animal.manger()

    def entretenir(self, animal):
        animal.satisfaction = 100

    def ajouter_animal(self):
        self.nombre_animaux += 1