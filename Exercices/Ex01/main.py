from Models.Enclos import Enclos
from Models.Soigneur import Soigneur
from Models.Elephant import Elephant

elephant1 = Elephant()
elephant1.name = "Dumbo"
soigneur1 = Soigneur()
soigneur1.name = "jean"
soigneur1.ajouter_animal()
enclos1 = Enclos()
enclos1.name = "Elephants"
enclos1.ajouter_animal(elephant1)
enclos1.afficher_animal()

for i in range(7):
    print("Début de journée", i + 1)
    elephant1.afficher_info()
    elephant1.reset()
    elephant1.afficher_info()

    soigneur1.nourrir(elephant1)
    soigneur1.entretenir(elephant1)
    print("fin de journée")
    elephant1.afficher_info()
