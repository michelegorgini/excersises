# Codewar = Connect 4

class Connect4():

    def __init__(self, player1 = "1", player2="2"):
        self.input_col = 10
        self.player1 = player1
        self.player2 = player2
        self.colum = 7
        self.row = 6
        self.coin = 1
        self.player_in_action = player1
        self.grids = []
        self.grids = self.draw_grid()
        self.won = True

    def draw_grid(self): # Method to build the grid
        gridline = []
        for i in range(self.colum):
            gridline.append(0)
        grid = []
        for i in range(self.row):
            grid.append(list(gridline))
        return grid

    def print_grid(self,grids): # Method to print the grid
        print('Current Grid:')
        print(*grids, sep='\n')
        return

    def play(self, col): # Method to chose the colon for the coin
        if self.won:
            coin_col = col
            # incoin = ('Choose your colon {0} a number from 0 to 6 :'.format(game.player_in_action))
            result = ''
            if self.grids[0][col - 1] != 0:
                result = ('Column full!')
                # print(result)
                return result
            else:
                coin_row = self.fix_coin_place(coin_col)
                if coin_row or coin_row == 0 :
                    winner = self.check_winner(coin_col, coin_row)
                    return winner
                else:
                    # print('Column full!')
                    return 'Column full!'
        # print("Game has finished!")
        return "Game has finished!"
        # while True:
        #     try:
        #         coin_col = int(col)
        #     except ValueError:
        #         result = ('Player {} has a turn'.format(game.coin))
        #         # print(result)
        #         return result
        #         continue
        #     if (coin_col < 0) or (coin_col > col-1):
        #         result = ('Player {} has a turn'.format(game.coin))
        #         # print(result)
        #         return result
        #     elif grids[0][coin_col - 1] != 0:
        #         result = ('Column full!')
        #         # print(result)
        #         return result
        #     else:
        #         result = ('Player {} has a turn'.format(game.coin))
        #         # print(result)
        #         return result

    def fix_coin_place(self, coin_col): # Method to fix the coin on the grid and get the row
        for i in range((self.row-1), -1,-1):  #start from 5(self.row-1), -1 decrease, -1 decrease of 1
            if self.grids[i][coin_col] == 0:
                self.grids[i][coin_col] = game.coin
                # print(i)
                # print()
                return i

    def check_horizontal(self, coin_row): # Method to check horizontal four
        check=0
        for line in self.grids[coin_row]:
            if line == game.coin:
                check+=1
                if check == 4:
                    return True
                    break
                else:
                    continue
            else:
                check =0
        return False

    def check_vertical(self, coin_col): # Method to check vertical four
        check=0
        for i in range(self.row):
            if (self.grids[i][coin_col])== self.coin:
                check+=1
                if check == 4:
                    return True
                    break
                else:
                    continue
            else:
                check =0
        return False

    def check_diagonal_row_left(self,coin_col,coin_row): # Method to check diagonal=I need: start_row,start_col,end_row
        check=0                                           # 1
        if coin_row == 0 or coin_col == 0:                #   1
            start_row = coin_row                          #     1
            start_col = coin_col                          #       1
        else:
            diff = coin_row - coin_col
            if diff <= 0:
                start_row = 0
                start_col = coin_col - coin_row
            else:
                start_col = 0
                start_row = coin_row - coin_col
        diff_col = (self.colum - 1) - start_col
        if diff_col > 4:
            end_row = self.row
        else:
            end_row = diff_col+1
        for i in range(start_row,end_row):
            if (self.grids[i][start_col])== self.coin:
                check+=1
                start_col +=1
                if check == 4:
                    return True
                    break
                else:
                    continue
            else:
                start_col +=1
                check =0
        return False

    def check_diagonal_row_right(self, coin_col, coin_row ): #Method check diagonal=I need: start_row,start_col,end_row
        check=0                                                  #           1
        if coin_row == 0 or coin_col == (self.colum - 1):        #         1
            start_row = coin_row                                 #       1
            start_col = coin_col                                 #     1
        else:
            add = coin_col + coin_row
            if add <= self.colum-1:
                start_row = 0
                start_col = add
            else:
                start_col = self.colum - 1
                diff_col = start_col - coin_col
                start_row = coin_row - diff_col
        add_start = start_row + start_col
        if add_start <= self.row-1:
            end_row = add_start+1
        else:
            end_row = self.row
        for i in range(start_row,end_row):
            if (self.grids[i][start_col])== self.coin:
                check+=1
                start_col -=1
                if check == 4:
                    return True
                    break
                else:
                    continue
            else:
                check =0
                start_col -=1
        return False

    def check_winner(self, coin_col, coin_row): # Final Check method
        result = ''
        if (self.check_horizontal(coin_row) == True or
                self.check_vertical(coin_col) == True or
                self.check_diagonal_row_left(coin_col, coin_row) == True or
                self.check_diagonal_row_right(coin_col, coin_row) == True):
            result = ("Player {} wins!".format(self.coin))
            print(result)
            self.won = False
            return result
        else:
            coin_old = self.coin  #
            if self.coin == 1:
                self.coin = 2
                self.player_in_action = self.player2
            else:
                self.coin = 1
                self.player_in_action = self.player1
            result = ('Player {} has a turn'.format(coin_old))
            print(result)
            return result

    def __str__(self):
        return "Player 1: {0.player1} \nPlayer 2: {0.player2}".format(self)




# game = Connect4()
# print(game)
# grids = game.draw_grid()
# game.print_grid(grids)
# won = True
# while True:
#     coin_col = game.play(game.col)
#     print(coin_col)
#     coin_row = game.fix_coin_place(coin_col)
#     if coin_row == "Column full!":
#         print("Column full!")
#         coin_row = game.fix_coin_place(coin_col)
#     else:
#         game.print_grid(grids)
#         check_winner = game.check_winner(coin_col,coin_row)
#         if check_winner == "Player 1 wins!" or check_winner == "Player 2 wins!":
#             won = False
# print ('Game has finished!')



# game = Connect4()
# test.it("Should return: Player 1 has a turn")
# coin_col = game.play(game.col)
# game.play(0)
# test.it("Should return: Player 2 has a turn")
# game.play(0)    #, "Player 2 has a turn")

# game = Connect4()
# # test.it("Should return: Player 1 has a turn")
# game.play(4) #, "Player 1 has a turn")
# #test.it("Should return: Player 2 has a turn")
# game.play(4) #, "Player 2 has a turn")
# #test.it("Should return: Player 1 has a turn")
# game.play(4) #, "Player 1 has a turn")
# #test.it("Should return: Player 2 has a turn")
# game.play(4) #, "Player 2 has a turn")
# #test.it("Should return: Player 1 has a turn")
# game.play(4) #, "Player 1 has a turn")
# #test.it("Should return: Player 2 has a turn")
# game.play(4) #, "Player 2 has a turn")
# #test.it("Should return: Column full!")
# game.play(4)  #, "Column full!")


game = Connect4()
# test.it("Should return: Player 1 has a turn")
game.play(1) #, "Player 1 has a turn")
#test.it("Should return: Player 2 has a turn")
game.play(1) #, "Player 2 has a turn")
#test.it("Should return: Player 1 has a turn")
game.play(2) #, "Player 1 has a turn")
#test.it("Should return: Player 2 has a turn")
game.play(2) #, "Player 2 has a turn")
#test.it("Should return: Player 1 has a turn")
game.play(3) # , "Player 1 has a turn")
#test.it("Should return: Player 2 has a turn")
game.play(3) #, "Player 2 has a turn")
#test.it("Should return: Player 1 wins!")
game.play(4) #, "Player 1 wins!")
#test.it("Should return: Game has finished!")
game.play(4) #, "Game has finished!")