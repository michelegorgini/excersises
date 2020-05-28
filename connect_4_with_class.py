class Board(object):
    def __init__(self, number_of_rows, number_of_columns):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.rows = []

    def build(self):
        for i in range(0, self.number_of_rows):
            row = []
            for j in range(0, self.number_of_columns):
                row.append(None)
            self.rows.append(row)
            
    
        
    def __str__(self):
        output = ''
        for row in self.rows:
            line = ''
            for column in row:
                if column is None:
                    line += ' |'
                else:
                    line += column.symbol + '|'
            line += '\n'
            output += line
        return output
    


    def show(self):
        print(self)

    def drop(self, coin, chosen_column):
        for i in range(self.number_of_rows - 1, 0, -1):
            if self.rows[i][chosen_column] is None:
                self.rows[i][chosen_column] = coin
                coin.y = i
                coin.x = chosen_column
                break

        pass

    def check_for_winner(self, coin):
        winner = False
        #horizontal check
        array_to_check = self.rows[coin.y]
        winner = self.check_connected_coins(coin, array_to_check)
        if winner:
            return True

        # vertical check
        array_to_check = []
        for row in self.rows:
            array_to_check.append(row[coin.x])

        winner = self.check_connected_coins(coin, array_to_check)
        if winner:
            return True

        #diagonal check_left
        array_to_check = []

        #diagonal_check_right


        pass

    def check_connected_coins(self, coin, array):

        consecutive_coins = 0

        for item in array:
            if item is None:
                consecutive_coins = 0
            elif item.symbol == coin.symbol:
                consecutive_coins += 1
                if consecutive_coins == 4:
                    return True
        pass


class Coin(object):
    def __init__(self, symbol):
        self.symbol = symbol
        self.x = None
        self.y = None
    pass

    def __str__(self):
        return "position x: {0}, y: {1}".format(self.x, self.y)


class Connect4():

    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.active_player = None
        self.number_of_rows = 6
        self.number_of_columns = 7
        self.board = Board(self.number_of_rows, self.number_of_columns)

    def setup(self):
        self.board.build()
        self.board.show()
        self.player1 = Player("Jonne", "X")
        self.player2 = Player("Michele", "O")
        self.choose_starting_player()

    def choose_starting_player(self):
        self.active_player = self.player1
        pass

    def start(self):
        chosen_column_input = ('Choose your column {0} a number from 1 to {1}:'.format(self.active_player.name, self.number_of_columns))
        try:
            coin = Coin(self.active_player.symbol)
            chosen_column = int(input(chosen_column_input)) - 1
            self.board.drop(coin, chosen_column)
            self.board.show()
            if self.board.check_for_winner(coin):
                print("{0} won the game".format(self.active_player.name))
                return

            self.next_turn()
            # print("you chose column {0}".format(chosen_column))
        except ValueError:
            print('invalid input!')
        pass

    def next_turn(self):
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1
        self.start()
        pass


class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


game = Connect4()
game.setup()
game.start()
