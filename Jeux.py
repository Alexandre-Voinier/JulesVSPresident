from Jules import *
from Macron import *
from Trump import *
from Putin import *
class Jeux:
    def __init__(self):
        self.jules = Jules()

    def nextRound(self, ennemi):
        print()
        self.jules.competence()
        print("Que veux tu faire:\n")
        userInput = int(input())
        print()
        self.jules.choose(userInput, ennemi)

    def loose(self, ennemi):
        print("{0} vous a battu".format(ennemi.pseudo))
        print("Game Over!")

    def status(self, ennemi):
        print("Jules: " + str(self.jules.health)  + "HP\n" + ennemi.pseudo  +":" + str(ennemi.health) + "HP\n")

    def main(self):
        print("Bienvenue dans Jules contre les présidents")
        print("Dans ce jeu vous incarnez Jules un élève d'EPITA qui part en guerre contre les présidents ! \n\n")

        # Premier combat contre Macron
        print("Votre premier adversaire est Macron")
        macron = Macron()
        macron.describe()

        while (macron.isAlive() and self.jules.isAlive()):
            self.status(macron)
            self.nextRound(macron)
            if (macron.isAlive()):
                print("Macron: ", end="")
                macron.nextRound(self.jules)
        
        if (self.jules.isAlive()):
            print("\nBravo vous avez conquis l'Europe !\n")
            self.jules.health = 100
        else:
            self.loose(macron)
            return
        
        # Combat contre Trump
        trump = Trump()
        trump.describe()

        while (trump.isAlive() and self.jules.isAlive()):
            self.status(trump)
            self.nextRound(trump)
            if (trump.isAlive()):
                print("Trump: ", end="")
                trump.nextRound(self.jules)
        
        if (self.jules.isAlive()):
            print("\nBravo vous avez conquis les USA !\n")
            self.jules.health = 500
        else:
            self.loose(trump)
            return
        
        # Combat contre Putin
        putin = Putin()
        putin.describe()
        
        while (putin.isAlive() and self.jules.isAlive()):
            self.status(putin)
            self.nextRound(putin)
            if (putin.isAlive()):
                print("Putin: ", end="")
                putin.nextRound(self.jules)

        if (self.jules.isAlive()):
            print("\nFélicitation vous avez gagné la partie !\n")
            return
        else:
            self.loose(putin)
            return



        
