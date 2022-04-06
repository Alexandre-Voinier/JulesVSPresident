from Personnage import *
class Jules(Personnage):
    def __init__(self):
        self.health = 62
        self.attack = 13
        self.armor = 58
        self.popularity = 100
        self.pseudo = "Jules"
        
 
    def describe(self):
        print("Bonjour je suis " + pseudo + " je suis un étudiant d'EPITA")

    def competence(self):
        print("Jules: Voici mes compétences :")
        print("1 : Excellent codeur en C")
        print("2 : Capable de pirater le Pentagone")
        print("3 : Est inconnu des services du FSB, FBI & DGSI")
        print("4 : Capable de vivre la nuit")

    def codeenC(self):
        print("Jules: Et j'importe MALLOC.H !\n")
        self.health+=10
        self.armor+=10

    def pentagone(self, ennemi):
        print("Jules: Gniark j'ai piraté le Pentagone !\n")
        ennemi.takeDamage(20)
        self.popularity+=50

    def discret(self, ennemi):
        print("Jules J'ai des compétences particulières me permettant d'être invisible\n")
        self.health += 100
        ennemi.armor -= 100

    def tard(self, ennemi):
        print("Jules: Et voici mon attaque à 5h du mat !\n")
        ennemi.armor -= 50
        ennemi.takeDamage(100)
        self.attack += 10

    def choose(self, r, ennemi):
        if (r == 1):
            self.codeenC()
        elif(r == 2):
            self.pentagone(ennemi)
        elif(r == 3):
            self.discret(ennemi)
        elif(r == 4):
            self.tard(ennemi)
    

    
