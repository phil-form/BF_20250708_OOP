import datetime

from Models.Enclos import Enclos
from Models.Soigneur import Soigneur
from Models.Elephant import Elephant

elephant1 = Elephant()
elephant1.name = "Dumbo"
soigneur1 = Soigneur()
soigneur1.name = "jean"
enclos1 = Enclos()
enclos1.name = "Elephants"
enclos1.add_animal(elephant1)
enclos1.list_animals()

for i in range(7):
    print("Début de journée", i + 1)
    print(elephant1.info)
    elephant1.reset()
    print(elephant1.info)

    soigneur1.nourrir(elephant1)
    soigneur1.pet(elephant1)
    print("fin de journée")
    print(elephant1.info)
