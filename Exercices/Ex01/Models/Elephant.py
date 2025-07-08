class Elephant:
    name = 'Elephant'
    appetit = 50
    satisfaction = 100
    en_vie = True
    soigneur = None

    def manger(self):
        print(f'{self.name} mange')
        self.appetit = 100

    def afficher_info(self):
        print(f'{self.name} | {self.appetit} | {self.en_vie} | {self.satisfaction}')

    def reset(self):
        self.appetit = 0
        self.satisfaction = 0
