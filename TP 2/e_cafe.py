from abc import ABC, abstractmethod
from dataclasses import dataclass

class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass
    
    @abstractmethod
    def description(self):
        pass
    
    def __add__(self, other):
        return BoissonCombinee(self, other)
    
class Cafe(Boisson):
    def cout(self):
        return 2.0
    
    def description(self):
        return "Café simple"
    
class The(Boisson):
    def cout(self):
        return 1.5
    
    def description(self):
        return "Thé"

class decorateurBoisson(Boisson):
    def __init__(self, boisson):
        self._boisson = boisson
        
class Lait(decorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.5
    
    def description(self):
        return self._boisson.description() + " , lait"
    
class Sucre(decorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.2
    
    def description(self):
        return self._boisson.description() + " , sucre"
    
class Caramel(decorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.6
    
    def description(self):
        return self._boisson.description() + " , caramel"    
    
class Chocolat(decorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.8
    
    def description(self):
        return self._boisson.description() + " , chocolat"

class BoissonCombinee(Boisson):
    def __init__(self, boisson1, boisson2):
        self._boisson1 = boisson1
        self._boisson2 = boisson2
        
    def cout(self):
        return self._boisson1.cout() + self._boisson2.cout()
    
    def description(self):
        return self._boisson1.description() + " + " + self._boisson2.description()

@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0
    
class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []
        
    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)
        
    def total(self):
        total =0
        for b in self.boissons:
            total += b.cout()
        return total
    
    def afficher(self):
        print("Commande :")
        for b in self.boissons:
            print((b.description()) + ",")
        print("Prix : " + str(self.total()))

class CommandeSurPlace(Commande):

    def afficher(self):
        print("Commande SUR PLACE")
        super().afficher()
        
class CommandeEmporter(Commande):

    def afficher(self):
        print("Commande A EMPORTER")
        super().afficher()
        
class Fidelite:
        
    def ajouter_points(self, client, p):
        points =int(p)
        client.points_fidelite += points
        
class CommandeFidelite(Commande, Fidelite):

    def valider(self):
        points = int(self.total())
        self.ajouter_points(self.client, points)
        
Client("chemseddine", 1958)

boisson1 = Cafe()
boisson2 = The()
boisson3 = boisson1 + boisson2
boisson1 = Lait(boisson1)
boisson1 = Chocolat(boisson1)
boisson2 = Sucre(boisson2)

Cmd = CommandeFidelite(Client("chemseddine", 1958))
Cmd.ajouter_boisson(boisson1)
Cmd.ajouter_boisson(boisson2)
Cmd.ajouter_boisson(boisson3)
Cmd.afficher()
Cmd.valider()
print("Points de fidélité : " + str(Cmd.client.points_fidelite))