class Personnage:
    def __init__(self):
        self.health = 10
        self.attack = 2
        self.armor = 1
        self.popularity = 100
        self.pseudo = ""
    
    def attack(self, ennemi):
        ennemie.health -= attack
    
    def nuke(self, ennemi):
        ennemi.health = 0

    def takeDamage(self, damage):
        self.health -= damage

    def describe(self):
        print("Bonjour je suis " + pseudo + " je suis un template")

    def isAlive(self):
        if (self.health > 0):
            return True
        return False
