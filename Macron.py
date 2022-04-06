import random
from Personnage import *

class Macron(Personnage):
    def __init__(self):
        self.health = 62
        self.attack = 13
        self.armor = 58
        self.popularity = 100
        self.pseudo = "Macron"
 
    def describe(self):
        print("Bonjour je suis " + self.pseudo + " je suis le président français pour encore quelques semaines minimum")
        self.print_ascii()

    def gilejone(self):
        print("Oh non, une manifestation de gilets jaunes je cours me cacher\n")
        self.health -= 20
        self.popularity -= 20

    def cocorico(self, ennemi):
        print("Macron lance un coq sur l'ennemi, ce n'est pas très efficace\n")
        self.popularity += 1
        ennemi.takeDamage(2)

    def championdumonde(self, ennemi):
        print("Nouvelle étoile sur le maillot, le blason français est sur le devant de la scène\n")
        self.health += 30
        ennemi.takeDamage(30)

    def baguette(self, ennemi):
        print("Du bon pain français !\n")
        ennemi.takeDamage(20)
        self.attack += 10
    
    def nextRound(self, ennemi):
        r = random.randint(1, 4)
        if (r == 1):
            self.gilejone()
        elif(r == 2):
            self.cocorico(ennemi)
        elif(r == 3):
            self.championdumonde(ennemi)
        elif(r == 4):
            self.baguette(ennemi)       


    def print_ascii(self):
        print("  __                           \n / _|                          \n| |_ _ __ __ _ _ __   ___ ___ \n|  _| '__/ _` | '_ \ / __/ _ \\\n| | | | | (_| | | | | (_|  __/\n|_| |_|  \__,_|_| |_|___\___|\n")
