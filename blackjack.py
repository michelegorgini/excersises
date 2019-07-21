# We are gonna carry on working with Tkinter to produce a very simple card game now there's a couple of things that we
# haven't fully explored with functions yet and as I mentioned earlier there's another reason why IntelliJ warns about
# shadowing variables in the outer scope this game is gonna give us a way to look at that in more detail.

import random

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'ppm'  # not "png" because I have TKVersion >= 8.6 but I downloaded  only "ppm" extension
    else:
        extension = 'ppm'


    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # add the image to a Label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list.
    # Only one ace can have the value 11, and this will be reduce to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")

    #
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there is an ace and subtract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")
    # print(locals())


mainWindow = tkinter.Tk()

# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)
# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# load cards
cards = []
load_images(cards)
print(cards)
# Create a new deck of cards and shuffle them
deck = list(cards)

random.shuffle(deck)

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

deal_player()
dealer_hand.append(deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

mainWindow.mainloop()



# VERY IMPORTANT CONCEPT:
# So when you use the name of a global variable in a function Python assumes that you want to use the global variable
# and will happily let you until you try to change its value that's the key point there so soon as you assign a new
# value to a global variable within a function Python then creates a local variable with the same name and your code
# no longer refers to the global variable so once you understand behavior it actually does make sense. This is the case
# of the two variable : player_score and player_ace in the function (def deal_player():) --> local variable. but we use
# the same name in the general program after the comment (# embedded frame to hold the card images) in this case they
# are general variable. IntelliJ warns only about player_score because in the function (def deal_player():) we change
# the value only at player_score not at player_ace. And for the same reason if we delete the code (player_score = 0)
# inside the function (def deal_player():) we get an error, because in the same function we use the code
# (player_score -= 10) but we are inside the function so Python don't check outside the function if there is the same
# variable because it considers this variable as local so it says us: " You need to initialize this variable).
#
# But if we write inside the function (global player_score) and (global player_ace) the error disappears because we say
# to python that these variable are global.
#
# OTHER CONSIDERATION ABOUT GLOBAL E LOCAL VARIABLES:
# One final comment about global variables you probably sick about it now but we are harping on about it because it's
# really important that you understand this and get it to the right mind set about how to use them so you are aware of
# the limitations you might be wondering why the variables player_hand and dealer_hand are not triggering warnings
# about a local variable shadowing the global ones because both the deal_player function if we go back and have a look
# at that as you can see the deal_player function on line 83 and the deal_dealer function on line 65 they are both
# appending new cards to the corresponding list so wouldn't that count as modifying the global variable in which make
# them local because we talked about that in previous videos. Well the answer is that neither variable is modified
# their initialized as lists if you go down and have a look we got player_hand and dealer_hand is initialization as you
# can see here in line 157 and 158 and continue to reference the same lists as long as the program runs so adding items
# to list or removing items from it is not modifying the list variable it always has the same value which is a list and
# the contents of a list can change now adding items to a global list is still a side effect but its not considered as
# dangerous as changing the list of the variable holds for example lists exists to have items added and removed and so
# consequently this is acceptable behavior and that's why IntelliJ is not actually warning of us of that so it would
# still probably better to pass the lists arguments to the functions but as we can't provide parameters to functions
# that are used as button commands we really don't have any choice here but to use global list so that of course why
# we went ahead and did that ok.