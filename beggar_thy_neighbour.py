# Beggar Thy Neighbour

# Beggar Thy Neighbour is a card game taught to me by my parents when I was a small child, and is a game I like to play with my young kids today.
#
# In this kata you will be given two player hands to be played. And must return the index of the player who will win.
#
# Rules of the game
# Special cards are: Jacks, Queens, Kings and Aces
# The object of the game is to win all the cards.
# Any player that cannot play a card is out of the game.
# To start:
#
# The 52 cards in a standard deck are shuffled.
# The cards are dealt equally between all players.
# To play:
#
# - The first player turns over and plays the top card from their hand into a common pile.
# - If the card is not special - then the second player plays their next card onto the pile, and play continues
#   back to the first player.
# - If the card is a Jack, Queen, King or Ace, the other player must play 1, 2, 3 or 4 penalty cards respectively.
# _ If no special cards are played during a penalty, then the player that played the special card, takes the common pile.
# - If a special card is played during a penalty, then the penalty moves back to the previous player immediately with
#  the size of the new penalty defined by the new special card. It is possible for this process to repeat several times
#  in one play. Whoever played the last special card, wins the common pile.
# - The winner of the common pile, places it on the bottom of their hand, and then starts the next common pile.
#  It is theorised that an initial deal may never end, though so far all of my games have ended! For that reason,
#  if 10,000 cards are played and no one has won, return None.
#
# Card Encoding
# Cards are represented with a two character code. The first characater will be one of A23456789TJQK representing Ace, 2 though 9, Ten, Jack, Queen, King respectively. The second character is the suit, 'S', 'H', 'C', or 'D' representing Spades, Hearts, Clubs and Diamonds respectively.
#
# For example a hand of ["TD", "AC", "5H"] would represent 10 of Diamonds, Ace of Clubs, and 5 of hearts.
#
# Mini Example Game
# Given the following hands:
#
# Player 1: [9C, JC, 2H, QC], Player 2: [TD, JH, 6H, 9S]
#
# Play would flow as follows:
#
# Start   - P1: [9C, JC, 2H, QC],   P2: [TD, JH, 6H, 9S],           Common: []
# Turn  1 - P1: [JC, 2H, QC],       P2: [TD, JH, 6H, 9S],           Common: [9C]
# Turn  2 - P1: [JC, 2H, QC],       P2: [JH, 6H, 9S],               Common: [9C, TD]
# Turn  3 - P1: [2H, QC],           P2: [JH, 6H, 9S],               Common: [9C, TD, JC]
# Player 1 plays a Jack, player 2 pays 1 penalty
#
# Turn  4 - P1: [2H, QC],           P2: [6H, 9S],                   Common: [9C, TD, JC, JH]
# Player 2 plays a Jack, player 1 pays 1 penalty
#
# Turn  5 - P1: [QC],               P2: [6H, 9S],                   Common: [9C, TD, JC, JH, 2H]
# Player 2 wins the common pool and starts the next game
#
# Turn  6 - P1: [QC],               P2: [9S, 9C, TD, JC, JH, 2H],   Common: [6H]
# Turn  7 - P1: [],                 P2: [9S, 9C, TD, JC, JH, 2H],   Common: [6H, QC]
# Player 1 plays a Queen, player 2 pays 2 penalties
#
# Turn  8 - P1: [],                 P2: [9C, TD, JC, JH, 2H],       Common: [6H, QC, 9S]
# Turn  9 - P1: [],                 P2: [TD, JC, JH, 2H],           Common: [6H, QC, 9S, 9C]
# Player 1 wins the common pool and starts the next game
#
# Turn 10 - P1: [QC, 9S, 9C],       P2: [TD, JC, JH, 2H],           Common: [6H]
# And so on... with player 2 eventually winning.
#
# Good luck!


# class Beggar:
#
#     def __init__(self, h1, h2):
#         self.dict_special_cards = {'JS': 1,
#                                    'JH': 1,
#                                    'JC': 1,
#                                    'JD': 1,
#                                    'QS': 2,
#                                    'QH': 2,
#                                    'QC': 2,
#                                    'QD': 2,
#                                    'KS': 3,
#                                    'KH': 3,
#                                    'KC': 3,
#                                    'KD': 3,
#                                    'AS': 4,
#                                    'AH': 4,
#                                    'AC': 4,
#                                    'AD': 4}
#
#         self.common_deck = []
#         self.sorted_hand1 = self.sorted_hand_penalty(h1)
#         self.sorted_hand2 = self.sorted_hand_penalty(h2)
#         self.hand_sorted_player_in_action = self.sorted_hand1
#         self.player_in_action = 1
#         self.won = True
#         self.old_penalty = 0
#
#     def sorted_hand_penalty(self, hand):
#         tmp_hand_to_sort = []
#         for card in hand:
#             if card not in self.dict_special_cards.keys():
#                 tmp_hand_to_sort.append((card, 0))
#             else:
#                 tmp_hand_to_sort.append((card, self.dict_special_cards[card]))
#         sorted_hand_player_in_action = sorted(tmp_hand_to_sort, key=lambda x: x[1])
#         return sorted_hand_player_in_action
#
#     def game_turn(self):
#         while self.hand_sorted_player_in_action:
#             print(self.hand_sorted_player_in_action)
#             print(self.common_deck)
#             print(self.player_in_action)
#             print("="*20)
#             card_remain = len(self.hand_sorted_player_in_action)
#             if self.common_deck:
#                 if self.old_penalty == 0:
#                     self.old_penalty = self.play_card()
#                     self.change_turn()
#                 elif self.old_penalty == 1:
#                     new_penalty = self.play_special_card()
#                     card_remain -= 1
#                     if new_penalty == 0:
#                         if card_remain == 0:
#                             if self.player_in_action == 1:
#                                 result = 1
#                             else:
#                                 result = 0
#                             return result
#                         else:
#                             self.old_penalty = self.play_card()
#                             self.takeDeck_and_changeTurn()
#                     else:
#                         self.old_penalty = new_penalty
#                         self.change_turn()
#                 elif self.old_penalty > 1:
#                     new_penalty = self.play_special_card()
#                     self.old_penalty -= 1
#                     card_remain -= 1
#                     while self.old_penalty:
#                         if new_penalty == 0:
#                             if card_remain == 0:
#                                 if self.player_in_action == 1:
#                                     result = 1
#                                 else:
#                                     result = 0
#                                 return result
#                             else:
#                                 new_penalty = self.play_card()
#                                 self.old_penalty -= 1
#                                 card_remain -= 1
#                         else:
#                             self.old_penalty = new_penalty
#                             self.change_turn()
#                     self.old_penalty = new_penalty
#                     self.takeDeck_and_changeTurn()
#             else:
#                 self.old_penalty = self.play_card()
#                 self.change_turn()
#         if self.player_in_action == 1:
#             result = 1
#         else:
#             result = 0
#         return result
#
#     def play_card(self):
#         self.common_deck.append(self.hand_sorted_player_in_action[0])
#         del self.hand_sorted_player_in_action[0]
#         return self.common_deck[-1][1]
#
#     def play_special_card(self):
#         for ind, val in enumerate(self.hand_sorted_player_in_action):
#             if val[1] > 0:
#                 self.common_deck.append(self.hand_sorted_player_in_action[ind])
#                 del self.hand_sorted_player_in_action[ind]
#                 return self.common_deck[-1][1]
#         self.play_card()
#
#     def change_turn(self):
#         if self.player_in_action == 1:
#             self.sorted_hand1 = self.hand_sorted_player_in_action
#             self.hand_sorted_player_in_action = self.sorted_hand2
#             self.player_in_action = 2
#         else:
#             self.sorted_hand2 =self.hand_sorted_player_in_action
#             self.hand_sorted_player_in_action = self.sorted_hand1
#             self.player_in_action = 1
#
#     def takeDeck_and_changeTurn (self):
#         if self.player_in_action == 1:
#             self.sorted_hand2.append(self.common_deck)
#             self.sorted_hand1 = self.hand_sorted_player_in_action
#             self.hand_sorted_player_in_action = self.sorted_hand2
#             self.common_deck = []
#             self.player_in_action = 2
#         else:
#             self.sorted_hand1.append(self.common_deck)
#             self.sorted_hand2 =self.hand_sorted_player_in_action
#             self.hand_sorted_player_in_action = self.sorted_hand1
#             self.common_deck = []
#             self.player_in_action = 1


# Try new solution with better performance

class Beggar:

    def __init__(self, h1, h2):
        self.dict_special_cards = {'JS': 1,
                                   'JH': 1,
                                   'JC': 1,
                                   'JD': 1,
                                   'QS': 2,
                                   'QH': 2,
                                   'QC': 2,
                                   'QD': 2,
                                   'KS': 3,
                                   'KH': 3,
                                   'KC': 3,
                                   'KD': 3,
                                   'AS': 4,
                                   'AH': 4,
                                   'AC': 4,
                                   'AD': 4}

        self.common_deck = []
        self.hand1_with_penalty = self.hand_with_penalty(h1)
        self.hand2_with_penalty = self.hand_with_penalty(h2)
        self.hand_with_penalty_player_in_action = self.hand1_with_penalty
        self.player_in_action = 1
        self.old_penalty = 0

    def hand_with_penalty(self, hand):
        tmp_hand_with_penalty = []
        for card in hand:
            if card not in self.dict_special_cards.keys():
                tmp_hand_with_penalty.append((card, 0))
            else:
                tmp_hand_with_penalty.append((card, self.dict_special_cards[card]))
        return tmp_hand_with_penalty

    def game_turn(self):
        while self.hand_with_penalty_player_in_action:
            card_remain = len(self.hand_with_penalty_player_in_action)
            if self.common_deck:
                if self.old_penalty == 0:                # Normal card
                    self.old_penalty = self.play_card()
                    self.change_turn()
                elif self.old_penalty == 1:              # Special card Jack
                    new_penalty = self.play_card()
                    card_remain -= 1
                    if new_penalty == 0:
                        if card_remain == 0:
                            return self.check_win()
                        else:
                            self.takeDeck_and_changeTurn()
                    else:
                        self.old_penalty = new_penalty
                        self.change_turn()
                else:                                     # All Special card without Jack
                    check_penalty = self.old_penalty
                    new_penalty = self.play_card()
                    check_penalty -= 1
                    card_remain -= 1
                    while check_penalty:
                        if new_penalty == 0:
                            if card_remain == 0:
                                return self.check_win()
                            else:
                                new_penalty = self.play_card()
                                check_penalty -= 1
                                card_remain -= 1
                        else:
                            check_penalty = 0
                    self.old_penalty = new_penalty
                    if new_penalty:
                        self.change_turn()
                    else:
                        self.takeDeck_and_changeTurn()
            else:
                self.old_penalty = self.play_card()
                self.change_turn()
        return self.check_win()

    def play_card(self):
        self.common_deck.append(self.hand_with_penalty_player_in_action[0])
        del self.hand_with_penalty_player_in_action[0]
        return self.common_deck[-1][1]

    def change_turn(self):
        if self.player_in_action == 1:
            self.hand1_with_penalty = self.hand_with_penalty_player_in_action
            self.hand_with_penalty_player_in_action = self.hand2_with_penalty
            self.player_in_action = 2
        else:
            self.hand2_with_penalty =self.hand_with_penalty_player_in_action
            self.hand_with_penalty_player_in_action = self.hand1_with_penalty
            self.player_in_action = 1

    def takeDeck_and_changeTurn (self):
        if self.player_in_action == 1:
            for ind in range(len(self.common_deck)):
                self.hand2_with_penalty.append(self.common_deck[ind])
            self.hand1_with_penalty = self.hand_with_penalty_player_in_action
            self.hand_with_penalty_player_in_action = self.hand2_with_penalty
            self.common_deck = []
            self.player_in_action = 2
        else:
            for ind in range(len(self.common_deck)):
                self.hand1_with_penalty.append(self.common_deck[ind])
            self.hand2_with_penalty =self.hand_with_penalty_player_in_action
            self.hand_with_penalty_player_in_action = self.hand1_with_penalty
            self.common_deck = []
            self.player_in_action = 1

    def check_win(self):
         if self.player_in_action == 1:
             result = 1
         else:
             result = 0
         return result


def who_wins_beggar_thy_neighbour(h1, h2):
    game = Beggar(h1, h2)
    final_result = game.game_turn()
    print(final_result)
    return final_result

# who_wins_beggar_thy_neighbour(['9C', 'JC', '2H', 'QC'], ['TD', 'JH', '6H', '9S'])

h1, h2 = ['9C', 'JC', '2H', 'QC'], ['TD', 'JH', '6H', '9S']

# h1, h2 = ['2C', '6D', '9D', '5C', '6C', '6H', '9C', '4C', '5S', 'QD', 'QH', '8D', 'JH', 'KD', '7C', '5D', 'JS',
#           '3S', '9S', '9H', 'TS', 'TH', 'AC', '3D', '6S', 'JC'],['8C', '4D', '4S', '8S', '5H', 'AS', '3H', 'KH',
#                                                                  '3C', 'KC', '2H', 'AD', 'AH', '7H', 'TD', 'QC',
#                                                                  'JD', 'QS', '4H', '7D', 'KS', '7S', '2D', '2S',
#                                                                  'TC', '8H']

who_wins_beggar_thy_neighbour(h1, h2)




# h1 = ['9C', 'JC', '2H', 'QC']
# h2 = ['TD', 'JH', '6H', '9S']
#print(who_wins_beggar_thy_neighbour(h1, h2) == 1) # , "Player at index 1 should win.")


