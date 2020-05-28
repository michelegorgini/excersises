# Codewar = Connect 4

class Connect4():

    def __init__(self, player1 = "Jonne", player2 = "Michele"):
        self.player1 = player1
        self.player2 = player2
        self.col = 7
        self.row = 6
        self.coin = 1
        self.player_in_action = player1
        self.grids = []


    def draw_grid(self): # Method to build the grid
        gridline = []
        for i in range(self.col):
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
        incoin = ('Choose your colon {0} a number from 1 to {1}:'.format(game.player_in_action, col))
        result =''
        while True:
            try:
                coin_col = int(input(incoin))
            except ValueError:
                result = ('Player {} has a turn'.format(game.coin))
                print(result)
                #return result
                continue
            if (coin_col <= 0) or (coin_col > col) :
                result = ('Player {} has a turn'.format(game.coin))
                print(result)
                #return result
            elif grids[0][coin_col - 1] != 0:
                result = ('Column full!')
                print(result)
                #return result
            else:
                return coin_col - 1

    def fix_coin_place(self, coin_col): # Method to fix the coin on the grid and get the row
        for i in range((self.row-1), -1,-1):  #start from 5(self.row-1), -1 decrease, -1 decrease of 1
            if grids[i][coin_col] == 0:
                grids[i][coin_col] = game.coin
                return i


    def check_horizontal(self,coin_row): # Method to check horizontal four
        check=0
        for line in grids[coin_row]:
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
            if (grids[i][coin_col])== game.coin:
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
        diff_col = (self.col-1) - start_col
        if diff_col > 4:
            end_row = self.row
        else:
            end_row = diff_col+1
        # print(start_row)
        # print(start_col)
        # print(end_row)
        for i in range(start_row,end_row):
            if (grids[i][start_col])== game.coin:
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
        check=0                                              #           1
        if coin_row == 0 or coin_col == (self.col-1):        #         1
            start_row = coin_row                             #       1
            start_col = coin_col                             #     1
        else:
            add = coin_col + coin_row
            if add <= self.col-1:
                start_row = 0
                start_col = add
            else:
                start_col = self.col-1
                diff_col = start_col - coin_col
                start_row = coin_row - diff_col
        add_start = start_row + start_col
        if add_start <= self.row-1:
            end_row = add_start+1
        else:
            end_row = self.row
        # print(start_row)
        # print(start_col)
        # print(end_row)
        for i in range(start_row,end_row):
            if (grids[i][start_col])== game.coin:
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

    def check_winner(self, coin_pos, coin_row): # Final Check method
        result = ''
        if (game.check_horizontal(coin_row) == True or
                game.check_vertical(coin_col) == True or
                game.check_diagonal_row_left(coin_col, coin_row) == True or
                game.check_diagonal_row_right(coin_col, coin_row) == True):
            result = ("Player {} wins!".format(game.coin))
            print(result)
            return result
        else:
            if game.coin == 1:
                game.coin = 2
                game.player_in_action = self.player2
            else:
                game.coin = 1
                game.player_in_action = self.player1


    def __str__(self):
        return "Player 1: {0.player1} \nPlayer 2: {0.player2}".format(self)


game = Connect4()
print(game)
grids = game.draw_grid()
game.print_grid(grids)
won = True
while True:
    coin_col = game.play(game.col)
    coin_row = game.fix_coin_place(coin_col)
    game.print_grid(grids)
    check_winner = game.check_winner(coin_col,coin_row)
    if check_winner == ("Player 1 wins!") or check_winner == ("Player 2 wins!"):
        won = False
        break