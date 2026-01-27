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

################
################
################
################
################
################
################
################
################
################
################
################
################

def create_players():                                                      1
    num = int(input("How many players? (2-4): "))
    while 2 <= num <= 4:
        print("Please enter 2, 3, or 4.")
        num = int(input("How many players? (2-4): "))

    players = [None]*num        
    for i in range(num):
        players[i] = Player("P"+str(i+1))

    return players

players = create_players()


current_turn = 0
skip_next = set(currentPlayer)

while True:
    currentPlayer = players[current_turn]
    if currentPlayer in skip_next:
        skip_next.remove(currentPlayer)

    else:
        if currentPlayer.getPosition() == 13:
        skip_next.add(currentPlayer)
    current_turn = (current_turn + 1) % len(players)






def pickDeck(currentPlayer):
    
    print(deck[headPointer].getTextToDisplay())
    playersTotal = currentPlayer.getMoney() + deck[headPointer].getAmount()
    currentPlayer.setMoney(playersTotal)
    
    headPointer=headPointer+1
    if headPointer == len(deck):
        headPointer = 0


def checkanimal(curentPlayer):
    animal = board[currentPlayer].getboardPosition()
    if animal.getOwned == 'free':
        print("Would you like to buy a" + str(animal.getName()) + "for " + str(animal.getCost) + "?")
        input("Please Type: 'yes' or 'no':")


def playerMove(currentPlayer):                                          2
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

################
################
################
################
################
################
################
################
################
################


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


def menu_choice(choice):                             3
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
    print("               ")S
    choice = input("Enter your choice: ")
    print("               ")
    print("===============")
    checkanimal(currentPlayer)
    running = menu_choice(choice)

















































