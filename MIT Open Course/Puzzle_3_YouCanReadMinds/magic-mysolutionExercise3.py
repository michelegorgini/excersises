# Exercise 3: I Implemented my solution Exercise 2.

#Programming for the Puzzled -- Srini Devadas
#You Can Read Minds (With a Little Calibration)
#Five random cards are chosen and one of them is hidden.
#Given four cards in a particular order, you can figure out what the fifth card is!

#Exercise 1: Make sure 5 distinct cards are "randomly" generated.

#Deck is are a list of strings, each string is a card
#The order of cards in the list matters.
deck = ['A_C','2_C','3_C','4_C','5_C','6_C','7_C','8_C','9_C','10_C','J_C','Q_C','K_C',
        'A_D','2_D','3_D','4_D','5_D','6_D','7_D','8_D','9_D','10_D','J_D','Q_D','K_D',
        'A_H','2_H','3_H','4_H','5_H','6_H','7_H','8_H','9_H','10_H','J_H','Q_H','K_H',
        'A_S','2_S','3_S','4_S','5_S','6_S','7_S','8_S','9_S','10_S','J_S','Q_S','K_S']


#This procedure figures out which card should be hidden based on the distance
#between the two cards that have the same suit.
#It returns the hidden card, the first exposed card, and the distance
# Michele-> Changed fuction for Exercise 2.
def outputFirstCard(numbers, oneTwoThree, cards):  # I changed this function because we can have 3 cards with same suit
    #print(len(oneTwoThree))                       # and to solve Exercise 2; two pair of cards with same suit
    min_encode = 99
    for index in range(0, len(oneTwoThree)):
        for ind in range(0, len(oneTwoThree[index])-1):
            print('$'*5)
            print(oneTwoThree[index])
            for i in range(ind+1, len(oneTwoThree[index])):
                encode = (numbers[oneTwoThree[index][ind]] - numbers[oneTwoThree[index][i]]) % 13
                if encode > 0 and encode <= 6:
                    if encode < min_encode:
                        min_encode = encode
                        hidden = oneTwoThree[index][ind]
                        other = oneTwoThree[index][i]
                else:
                    encode = (numbers[oneTwoThree[index][i]] - numbers[oneTwoThree[index][ind]]) % 13
                    if encode < min_encode:
                        min_encode = encode
                        hidden = oneTwoThree[index][i]
                        other = oneTwoThree[index][ind]



    ##    #The following print statement is just for debugging!
    ##    print ('Hidden card is:', cards[hidden], 'and need to encode', encode)
    print('First card is:', cards[other])

    return hidden, other, min_encode


#This procedure orders three cards depending on the number "code" that
#needs to be encoded. 
def outputNext3Cards(code, ind):
    
    if code == 1:
        second, third, fourth = ind[0], ind[1], ind[2]
    elif code == 2:
        second, third, fourth = ind[0], ind[2], ind[1]
    elif code == 3:
        second, third, fourth = ind[1], ind[0], ind[2]       
    elif code == 4:
        second, third, fourth = ind[1], ind[2], ind[0]
    elif code == 5:
        second, third, fourth = ind[2], ind[0], ind[1]
    else:
        second, third, fourth = ind[2], ind[1], ind[0]

    print ('Second card is:', deck[second])
    print ('Third card is:', deck[third])
    print ('Fourth card is:', deck[fourth])

    
#Sorts elements in tlist in ascending order.
def sortList(tlist):
    for index in range(0, len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            if tlist[ismall] > tlist[i]:
                ismall = i
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]
    
    return


#This procedure is similar to AssistantOrdersCards() except it
#takes in a large number and "randomly" generates five cards.
def ComputerAssistant():

    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = 0
    while number < 99999:
        number = int(input('Please give random number of at least 6 digits:'))


    #Generate five "random" numbers from the input number
    clist = []
    i = 0
    while len(clist) < 5:
        number = number * (i + 1) // (i + 2)
        n = number % 52
        i += 1
        if not n in clist:
            clist.append(n)

    print (clist)

    for i in range(5):
        n = clist[i]
        #print(n)
        cards.append(deck[n])
        cind.append(n)
        cardsuits.append(n // 13)
        cnumbers.append(n % 13)
        numsuits[n // 13] += 1


    # Exercise 2:
    cardh = []
    for index in range(0, len(numsuits)):
        if numsuits[index] > 1:
            pairsuit = index
            step_cardh = []
            for i in range(0, len(cardsuits)):                   # This loop give us a list with the position from cardsuits where the cards have
                if cardsuits[i] == pairsuit:                     # same suit. 2 elements = only 2 cards same suit, 3 elements = 3 cards same suit.
                    step_cardh.append(i)                         # If we have 2 pair of cards with the same suit we have 2 array
            cardh.append(step_cardh)

    print('-'*20)
    print(cards, ' cards = card symbol')
    print(cind, ' cind = index in desk list')
    print(cardsuits, ' cardsuits = suit card of 5 extraction, 0=C, 1=D, 2=H, 3=S')
    print(cnumbers, ' cnumbers = number in the card - 1')
    print('+'*20)
    print(numsuits, ' numsuits = list 4 element with default suit position 0=C, 1=D, 2=H, 3=S, content number repetition')
    print('='*20)
    print(cardh, 'cardh = indeces of card with same suit, 2 element = 2 suit repetition, 3 element = 3 suit repetition')


    hidden, other, encode = outputFirstCard(cnumbers, cardh, cards)

    remindices = []
    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])
    print(remindices, 'remindices = indices from cind list of the cards that are not the first(other) and the hidden ')

    sortList(remindices)
    print(remindices, 'remindices sorted = indices from cind list of the cards that are not the first(other) and the hidden ')

    outputNext3Cards(encode, remindices)

    #print(cards[hidden])
    guess = input('What is the hidden card?')
    if guess == cards[hidden]:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed!')

    return

ComputerAssistant()
