from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def manger(self):
        pass

    @abstractmethod
    def observer(self):
        pass

    @abstractmethod
    def faire_une_sieste(self):
        pass

    @abstractmethod
    def proba_deces(self):
        pass

    @abstractmethod
    def diminuer_rassasier(self):
        pass

    @abstractmethod
    def diminuer_bonheur(self):
        pass

