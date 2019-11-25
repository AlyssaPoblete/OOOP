# This class needs to inherit the attributes and behaviors of the Card class
# A Minion object is a Card
# a child Class - derived Class
from Card import Card

class Minion(Card):
    # attribute cost and name
    # inherits cost and name from parent class Card
    def __init__(self, cost, name, damage, life):
        Card.__init__(self, cost, name)
        # assign parameters to the onject
        self.damage = damage
        self.life = life

    def printMinionInfo(self):
        print('The card cost: ' + str(self.cost))
        print('The card name: ' + self.name)
        print('Damage: ' + str(self.damage))
        print('Life: ' + str(self.life))
