from random import shuffle

handOfCards = []

def createDeck():
    decklist = []
    suits = ['Hearts','Spades','Diamonds','Clubs']
    values = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
    for suit in suits:
        for value in values:
            decklist.append(value + ' of ' + suit)
    return decklist

def endProgram():
    exit()

def viewHand():
    global handOfCards
    if(len(handOfCards) > 0):
        print('You have the following cards in your hand:')
        for card in handOfCards:
            print(card)
        main()
    else:
        print('You currently have no cards in your hand')
        main()
        

def drawHand():
    global handOfCards
    deckOfCards = createDeck()
    shuffle(deckOfCards)
    handOfCards.clear()
    for card in range(7):
        drawnCard = deckOfCards.pop()
        handOfCards.append(drawnCard)
    print('You have drawn seven new cards!')
    main()

def main():
    print("Please select an option below by typing the number:")
    print("[1] Draw a new hand of seven cards")
    print("[2] View your hand")
    print("[3] Exit the Program")
    chosenOption = input()

    if(chosenOption == '1'):
        drawHand()
    elif(chosenOption == '2'):
        viewHand()
    elif(chosenOption == '3'):
        endProgram()
    else:
        print("Error: That is not a valid option")
        main()

if __name__ == "__main__":
    main()