class Player():
    def __init__(self, thePlayerID):
        self.playerID = thePlayerID
        self.boardPosition = 0
        self.money = 2000
    
    def getPosition(self):
        return self.boardPosition
    
    def setPosition(self, position):
        self.boardPosition = position

    def getMoney(self):
        return self.money
    
    def setMoney(self, amount):
        self.money = amount

class Animal():
    def __init__(self, theName, theCost, 
                 theL0, theL1, theL2, theL3, 
                 theImageLink, theSetSquare, theOwned):
        self.name = theName
        self.cost = theCost
        self.L0 = theL0
        self.L1 = theL1
        self.L2 = theL2
        self.L3 = theL3
        self.imageLink = theImageLink
        self.setSquare = theSetSquare
        self.owned = theOwned
        self.currentLevel = 0

    def getCost(self):
        return self.cost

    def getCurrentLevel(self):
        return self.currentLevel
    
    def setOwned(self, player):
        self.owned = player

    def getOwned(self):
        return self.owned
    
    def getName(self):
        return self.name
    
    ''' These need thinking about'''
    def upgrade(self, player):
        return None 

     # LOs need to be checked against player 
    def getAmountToCharge(self):
        return None
    
class Card():
    # private textToDisplay String
    # private amount Integer

    # constructor
    def __init__(self, theTextToDisplay, theAmount):
        self.textToDisplay = theTextToDisplay
        self.amount = theAmount

    def getTextToDisplay(self):
        return self.textToDisplay
    
    def getAmount(self):
        return self.amount

'''
- then complete class methods for an animal
- then consider how the menu system could be used to complete the game itself. 

'''


import random
###########################################################

# MAIN GAME # 

# setup the board

board = [None]*26 # setup an empty board of type None

# manually change each value so that the board is now of type Animal with 2 strings for the empty squares. 

board[0] = Animal("-START-", None, None, None, None, None, None, None, None)
board[1] = Animal("mouse", 600, 5, 25, 50, 100, "mouse.bmp", 1, "free")
board[2] = Animal("rabbit", 800, 8, 40, 80, 160, "rabbit.bmp", 2, "free")
board[3] = Animal("hedgehog", 900, 9, 45, 90, 180, "hedgehog.bmp", 3, "free")
board[4] = Animal("fox", 1200, 12, 60, 120, 240, "fox.bmp", 4, "free")
board[5] = Animal("badger", 1400, 14, 70, 140, 280, "badger.bmp", 5, "free")
board[6] = Animal("squirrel", 1000, 10, 50, 100, 500, "squirrel.bmp", 6, "free")
board[7] = Animal("owl", 1600, 16, 80, 160, 320, "owl.bmp", 7, "free")
board[8] = Animal("deer", 1800, 18, 90, 180, 360, "deer.bmp", 8, "free")
board[9] = Animal("boar", 2000, 20, 100, 200, 400, "boar.bmp", 9, "free")
board[10] = Animal("wolf", 2200, 22, 110, 220, 440, "wolf.bmp", 10, "free")
board[11] = Animal("lynx", 2400, 24, 120, 240, 480, "lynx.bmp", 11, "free")
board[12] = Animal("bear", 2600, 26, 130, 260, 520, "bear.bmp", 12, "free")
board[13] = Animal("-SPECIAL-", None, None, None, None, None, None, None, None)
board[14] = Animal("penguin", 1800, 18, 90, 180, 360, "penguin.bmp", 14, "free")
board[15] = Animal("seal", 2000, 20, 100, 200, 400, "seal.bmp", 15, "free")
board[16] = Animal("dolphin", 2400, 24, 120, 240, 480, "dolphin.bmp", 16, "free")
board[17] = Animal("shark", 2800, 28, 140, 280, 560, "shark.bmp", 17, "free")
board[18] = Animal("tiger", 3000, 30, 150, 300, 600, "tiger.bmp", 18, "free")
board[19] = Animal("elephant", 3500, 35, 175, 350, 700, "elephant.bmp", 19, "free")
board[20] = Animal("zebra", 2800, 28, 140, 280, 560, "zebra.bmp", 20, "free")
board[21] = Animal("giraffe", 3000, 30, 150, 300, 600, "giraffe.bmp", 21, "free")
board[22] = Animal("rhino", 3200, 32, 160, 320, 640, "rhino.bmp", 22, "free")
board[23] = Animal("hippo", 3400, 34, 170, 340, 680, "hippo.bmp", 23, "free")
board[24] = Animal("lion", 3600, 36, 180, 360, 720, "lion.bmp", 24, "free")
board[25] = Animal("gorilla", 3800, 38, 190, 380, 760, "gorilla.bmp", 25, "free")

# setup up to 4 players (this might need adapting if the game doesn't always have 4 players)

def create_players():
    num = int(input("How many players? (2-4): "))
    while not(2 <= num <= 4):
        print("Please enter 2, 3, or 4.")
        num = int(input("How many players? (2-4): "))

    players = [None]*num
    for i in range(num):
        players[i] = Player("P"+str(i+1))

    return players

players = create_players()

# setup the deck - this assumes they are always in this order, in we might shuffle - randomise. 
deck = [
    Card("WIN: You have won the zoo lottery", 1000000),
    Card("FINE: You are double parked while visiting the zoo", -200),
    Card("WIN: Your panda enclosure is a huge success", 500),
    Card("FINE: You must pay for emergency vet treatment", -400),
    Card("WIN: A famous wildlife photographer features your zoo", 300),
    Card("FINE: You forgot to lock the reptile house", -250),
    Card("WIN: School trip bookings increase profits", 350),
    Card("FINE: You must repair damaged fencing", -300),
    Card("WIN: Your zoo café has record sales", 200),
    Card("FINE: Health and safety inspection fine", -350),
    Card("WIN: A rare animal is donated to your zoo", 600),
    Card("FINE: Food supplies spoiled due to power cut", -200),
    Card("WIN: You receive a conservation grant", 500),
    Card("FINE: Animal escape causes bad publicity", -450),
    Card("WIN: Your zoo wins 'Best Family Attraction'", 400),
    Card("FINE: You must refund unhappy visitors", -150),
    Card("WIN: Sponsorship deal with wildlife charity", 700),
    Card("FINE: Extra staff wages during busy weekend", -250),
    Card("WIN: TV documentary filmed at your zoo", 800),
    Card("FINE: Unexpected enclosure maintenance", -300),
    Card("WIN: Successful breeding programme", 650),
    Card("FINE: Vet bills higher than expected", -350),
    Card("WIN: You host a sold-out night safari", 450),
    Card("FINE: Storm damage to outdoor enclosures", -500),
    Card("WIN: Gift shop profits exceed expectations", 250),
    Card("FINE: You lose income due to bad weather", -200),
    Card("WIN: Social media campaign boosts visitors", 300),
    Card("FINE: Animal food costs increase", -150),
    Card("WIN: You receive a donation from a benefactor", 1000),
    Card("FINE: You must upgrade security systems", -400),
    Card("WIN: Zoo anniversary celebration brings crowds", 550),
    Card("FINE: Cleaning costs after school holidays", -180),
    Card("WIN: New attraction opens successfully", 600),
    Card("FINE: Marketing campaign fails", -220),
    Card("WIN: Volunteers help reduce running costs", 200),
    Card("FINE: Parking fines from delivery vehicles", -120),
    Card("WIN: Endangered species funding approved", 750),
    Card("FINE: Insurance excess payment required", -300)
]

# this variable will point to the first item in queue of cards in the deck
headPointer = 0

####################################################################################
# functions to allow the game to be played
####################################################################################

def pickDeck(currentPlayer):
    
    print(deck[headPointer].getTextToDisplay())
    playersTotal = currentPlayer.getMoney() + deck[headPointer].getAmount()
    currentPlayer.setMoney(playersTotal)
    
    headPointer=headPointer+1
    if headPointer == len(deck):
        headPointer = 0

#def missAGo(currentPlayer):
    #position = 
    #if position = 
        

def checkanimal(currentPlayer):
    animal = board[currentPlayer].getboardPosition()
    if animal.getOwned == 'free':
        print("Would you like to buy a" + str(animal.getName()) + "for " + str(animal.getCost) + "?")
        input("Please Type: 'yes' or 'no':")


def playerMove(currentPlayer):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    position = currentPlayer.getPosition()+ dice1 + dice2
    if dice1 == dice2:
        pickDeck(currentPlayer)
    if position > 25:
        currentPlayer.setMoney(currentPlayer.getMoney()) + 500
        position = position - 26
    if position == 13:
        missAGo(currentPlayer)
    elif position != 0:
        checkAnimal(currentPlayer)
    return position
  
# complete this function based upon the exam question you completed, you may need to alter the function name and paramters. 

# WHAT OTHER FUNCTIONS ARE NEEDED? 

# what happens if you land on an occupied square
    # buy animal
    # get fined

# when is it your go? how might we track this? think queue again

# when is the game over? do we even know? 

    
####################################################################################
# menu system for the game itself
####################################################################################

'''
This wont work and likely doesnt have everything that we want. 
It shows how a menu can be made, it will need to be adapted for the game we are creating. 
'''

def output_board(theBoard):
    for i in range(len(board)):
        print(str(i)+" "+str(theBoard[i].getName()))
    print("===============")

def show_menu():
    print("\n=== Zoo Game Menu ===")
    print("1. View animals")
    print("2. Buy animal")
    print("3. Upgrade animal")
    print("4. End turn") 
    print("5. Veiw board")
    print("6. Quit Game")


def menu_choice(choice):
    match choice:
        case "1":
            print("You chose to view animals")
            # view animals code here

        case "2":
            print("You chose to buy an animal")
            # buy animal code here

        case "3":
            print("You chose to upgrade an animal")
            # upgrade animal code here

        case "4":
            print("Turn ended")
            # end turn code here

        case "5":
            return output_board(board)
            
        case "6":
            print("Game quitting...")
            return False

        case _:
            print("Invalid choice, try again")

    return True


# Main menu loop
running = True
while running:
    show_menu()
    print("===============")
    print("               ")
    choice = input("Enter your choice: ")
    print("               ")
    print("===============")
    checkanimal(currentPlayer)
    running = menu_choice(choice)