class Animal:
    name = 'asdf'
    # la bonne pratique est de faire des variables static constantes
    # Si celles-ci sont accessible de l'extérieur
    CONSTANT_VAR = 'asdf'

    # si non on les passe en privé
    __private_var = 'qwer'


obj = Animal()
# Accède à Animal.name
print(obj.name)
# Accède à Animal.name
print(Animal.name)

# je créé la propriété name dans l'objet obj
obj.name = 'qwer'
# est égale à 'qwer'
print(obj.name)
# reste égale à 'asdf'
print(Animal.name)

Animal.name = 'zxcv'
print(Animal.name)

# La bonne manière d'accéder aux membres abstrait est :
print(Animal.name) # Lecture
Animal.name = 'zxcv' # Écriture
