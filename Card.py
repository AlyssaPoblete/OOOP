# Card class is blueprint of the Card object
# Parent Class - base Class
class Card:

    # initializer to create the attributes of every class object
    # constructor
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
    # attributes describes the object - argument parameter
        # give the card a cost attribute
        # give the card a name attribute

    # behaviors - methods - functions
    def printCardInfo(self):
        print('The card cost: ' + str(self.cost))
        print('The card name: ' + self.name)

