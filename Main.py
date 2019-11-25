from Card import Card
from Minion import Minion

def main():
    # create the townCrier Card
    # cost = 1 and name = 'Town Crier'
    # instantiate an object called townCrier
    # creating an instance of the class
    townCrier = Minion(1, 'Town Crier', 1, 2)


    # create an instance of the class called redbandWasp or redband_wasp
    # attributes cost = 2 and name = 'RedBand Wasp'
    redbandWasp = Minion(2, 'Redband Wasp', 1, 3)

    # create the warpath card
    # name = 'warpath' cost = 2
    warpath = Card(2, 'Warpath')

    # show player details of the card
    townCrier.printCardInfo()
    townCrier.printMinionInfo()

    

    redbandWasp.printCardInfo()
    warpath.printCardInfo()

if __name__=="__main__":
    main()