# So moving on now the challenge and its going to be quite a simple one the challenges is to add a new button to the
# program with the text new game now the button should call a function that clears the cards from the screen it resets
# the players and dealers hands and then starts a new game now the easiest way to clear the contents of a frame is to
# destroy the frame and create a new one with the same name and in fact that's why the program has a player_card_frame
# and dealer_card_frame inside the card frame itself so that's it go away and create a new button with the text new
# game and again the functionality clear the cards from the Screen reset the player and dealers hands and then start a
# new game so pause the video go away and see if you can come up with a solution and when you're ready to see our
# version of it come back and and I'll go through that with you pause the video now.....

# NOT ABLE TO SOLVE!!!!!
# I was not able to solve the challenge I copy tim solution in a new Python file

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
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)# I created variable with the filename of the card
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card():
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # and add it to back of the pack
    deck.append(next_card)

    # now return the card's face value
    return next_card


# def score_hand(hand):
#     # Calculate the total score of all cards in the list.
#     # Only one ace can have the value 11, and this will be reduce to 1 if the hand would bust.
#     score = 0
#     ace = False
#     for next_card in hand:
#         card_value = next_card[0]
#         if card_value == 1 and not ace:
#             ace = True
#             card_value = 11
#         score += card_value
#         # if we would bust, check if there is an ace and subtract 10
#         if score > 21 and ace:
#             score -= 10
#             ace = False
#     return score

def deal(player_name):
    active_player = players[player_name]
    card = deal_card()
    card_value = card[0]
    if card[0] == 1 and not active_player['ace']:
        card_value = 11
        active_player['ace'] = True
    active_player['score'] += card_value
    # if we would bust, check if there is an ace and subtract 10
    if active_player['score'] > 21 and active_player['ace']:
        active_player['score'] -= 10
        active_player['ace'] = False


    if player_name == 'player':
        player_1 = active_player
        player_2 = players['dealer']
    else:
        player_1 = players['player']
        player_2 = active_player

    compare_scores(player_1, player_2)

    active_player['hand'].append(card)

    tkinter.Label(active_player['frame'], image=card[1], relief='raised').pack(side='left') # where ???
    active_player['score_label'].set(active_player['score'])

    # if players make 21 I disable players button
    if(active_player['score'] == 21) and active_player['finished'] == False :
        stop(player_name)

    print(active_player)
    print("#"*20)


def compare_scores(player_1, player_2):

    global player_gamewon # this 3 variable need to count the game already won
    global dealer_gamewon
    global player_gamedraw



    # I check if a player overtake 21 without finished == True
    if(player_1['score'] > 21) and player_1['finished'] == False:
        result_text.set("{} Won2! ".format(player_2['name']))
        dealer_gamewon += 1
        disable('player')
        disable('dealer')
        dealer_gamewon_label.set(dealer_gamewon)

    # I compare result when player has finished
    if(player_1['finished'] and (player_2['score'] > 21)):
        result_text.set("{} Won1! ".format(player_1['name']))
        player_gamewon += 1
        disable('dealer')
        player_gamewon_label.set(player_gamewon)
    elif(player_1['finished'] and player_2['score'] > player_1['score']):
        result_text.set("{} Won3! ".format(player_2['name']))
        dealer_gamewon += 1
        # code below: If dealer win i disable botton dealer
        disable('dealer')
        dealer_gamewon_label.set(dealer_gamewon)
    elif(player_1['finished'] and player_2['score'] == 21 and player_1['score'] == 21):
        result_text.set("draw")
        player_gamedraw += 1
        disable('dealer')
        player_gamedraw_label.set(player_gamedraw)

    # I compare result when player and dealer have finished
    if(player_1['finished'] and player_2['finished']):
        if(player_2['score'] > player_1['score']):
            result_text.set("{} Won5! ".format(player_2['name']))
            dealer_gamewon += 1
            dealer_gamewon_label.set(dealer_gamewon)
        elif (player_2['score'] < player_1['score']):
            result_text.set("{} Won6! ".format(player_1['name']))
            player_gamewon += 1
            player_gamewon_label.set(player_gamewon)
        else:
            result_text.set("Draw")
            player_gamedraw += 1
            player_gamedraw_label.set(player_gamedraw)



    print(player_1)
    print("^"*20)
    print(player_2)
    print("+"*20)
    # if(players['player']['score'] > 21) and players['player']['finished'] == False:
    #     result_text.set("{} Won2! ".format(players['dealer']['name']))
    #     dealer_gamewon += 1
    #     disable('player')
    #     disable('dealer')
    #
    # # I compare result when player has finished
    # if(players['player']['finished'] and (players['dealer']['score'] > 21)):
    #     result_text.set("{} Won1! ".format(players['player']['name']))
    #     player_gamewon += 1
    #     disable('dealer')
    # elif(players['player']['finished'] and players['dealer']['score'] > players['player']['score']):
    #     result_text.set("{} Won3! ".format(players['dealer']['name']))
    #     dealer_gamewon += 1
    #     # code below: If dealer win i disable botton dealer
    #     disable('dealer')
    # elif(players['player']['finished'] and players['dealer']['score'] == 21 and players['player']['score'] == 21):
    #     result_text.set("draw")
    #     player_gamedraw += 1
    #     disable('dealer')
    #
    # # I compare result when player and dealer has finished
    # if(players['dealer']['finished'] and players['dealer']['finished']):
    #     if(players['dealer']['score'] > players['player']['score']):
    #         result_text.set("{} Won5! ".format(players['dealer']['name']))
    #         dealer_gamewon += 1
    #     elif (players['dealer']['score'] < players['player']['score']):
    #         result_text.set("{} Won6! ".format(players['player']['name']))
    #         player_gamewon += 1
    #     else:
    #         result_text.set("Draw")
    #         player_gamedraw += 1
    #
    # # tO count how many game won the players or they draw
    # games_won(dealer_gamewon,player_gamewon,player_gamedraw)

    return(result_text)


def stop(player_name):
    active_player = players[player_name]
    active_player['finished'] = True
    print(active_player)

    if player_name == 'player':
        disable(player_name)  # I disable player botton
    elif player_name == 'dealer':
        disable(player_name)  # I disable dealer botton
        compare_scores(players['player'],players['dealer'])


def disable(player_name):
    if player_name == 'player':
        player_button = tkinter.Button(button_frame, text="Player", state = 'disable', command=lambda: deal('player'))
        player_button.grid(row=0, column=1)
    elif player_name == 'dealer':
        dealer_button = tkinter.Button(button_frame, text="Dealer", state = 'disable',command=lambda: deal('dealer'))
        dealer_button.grid(row=0, column=0)


def active_botton():
    player_button = tkinter.Button(button_frame, text="Player", state = 'normal', command=lambda: deal('player'))
    player_button.grid(row=0, column=1)

    dealer_button = tkinter.Button(button_frame, text="Dealer", state = 'normal',command=lambda: deal('dealer'))
    dealer_button.grid(row=0, column=0)



def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    global players


    active_botton() # I put normal (or active) the botton Dealer and Player

    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    dealer_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
    tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    player_score_label = tkinter.IntVar()
    tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
    tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)


    players = {
        'dealer' : {
            'name': 'dealer Jonne',
            'score': 0,
            'hand': [],
            'frame': dealer_card_frame,
            'score_label': dealer_score_label,
            'finished': False,
            'ace' : False
        },
        'player': {
            'name': 'player Michele',
            'score': 0,
            'hand': [],
            'frame': player_card_frame,
            'score_label': player_score_label,
            'finished': False,
            'ace' : False
        }
    }

    result_text.set("")

    # # Create the list to store the dealer's and player's hands
    # dealer_hand = []
    # player_hand = []

    # With the code below I put automatically on the table 2 cards for player and 1 card dealer????
    deal('player')
    deal('dealer')
    deal('player')


def shuffle():
    random.shuffle(deck)

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

dealer_gamewon_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer Games Won", background="green", fg='white').grid(row=5, column=0)
tkinter.Label(card_frame, textvariable=dealer_gamewon_label, background="green", fg="white").grid(row=6, column=0)

player_gamewon_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player Games Won", background="green", fg='white').grid(row=5, column=2)
tkinter.Label(card_frame, textvariable=player_gamewon_label, background="green", fg="white").grid(row=6, column=2)

player_gamedraw_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Games Draw", background="green", fg='white').grid(row=5, column=1)
tkinter.Label(card_frame, textvariable=player_gamedraw_label, background="green", fg="white").grid(row=6, column=1)

# embedded frame to hold the card images
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=lambda: deal('dealer'))
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=lambda: deal('player'))
player_button.grid(row=0, column=1)

stop_player_button = tkinter.Button(button_frame, text="Player-Stop", command=lambda: stop('player') )
stop_player_button.grid(row=1, column=1)

stop_dealer_button = tkinter.Button(button_frame, text="Dealer-Stop", command=lambda: stop('dealer'))
stop_dealer_button.grid(row=1, column=0)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

# load cards
cards = []
load_images(cards)
# Create a new deck of cards and shuffle them
deck = list(cards) + list(cards) + list(cards) # case with three deck
shuffle()

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

#create variable to count the match won by dealer - player or draw
dealer_gamewon= 0
player_gamewon = 0
player_gamedraw = 0

# create
new_game()


mainWindow.mainloop()
