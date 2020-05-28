# code war Shortest Knight Path

# Given two different positions on a chess board, find the least number of moves it would take a knight to get from
# one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.
#
# The knight is not allowed to move off the board. The board is 8x8.
#
# For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29
#
# For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29
#
# (Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input,
# output, and expected output; please post them.)

# col_letter = {'a': 0,
#               'b': 1,
#               'c': 2,
#               'd': 3,
#               'e': 4,
#               'f': 5,
#               'g': 6,
#               'h': 7}


class ChessBoard:

    def __init__(self, start, finish):
        self.input_start = start
        self.input_finish = finish
        self.col = 8
        self.row = 8
        self.move = [[+2, +1], [+2, -1], [-2, +1], [-2, -1], [+1, +2], [+1, -2], [-1, +2], [-1, -2]]
        self.letter_col = {'a': 0,
                           'b': 1,
                           'c': 2,
                           'd': 3,
                           'e': 4,
                           'f': 5,
                           'g': 6,
                           'h': 7}

        self.board = [[False] * 8 for i in range(8)]
        print(*self.board, sep='\n')
        self.start = self.calculate_position(start)
        self.finish = self.calculate_position(finish)
        self.open_set = []
        self.open_set.append(self.start)
        self.start_col = self.start[0]
        self.start_row = self.start[1]
        self.finish_col = self.finish[0]
        self.finish_row = self.finish[1]

    def calculate_position(self, position_string):
        return [self.letter_col[position_string[0]], int(position_string[1]) - 1]

    def calculateShortestPath(self, moves):
        # caluclate all the possible paths from start to finish and select the shortest one
        best_path = []
        if moves:
            count_move = moves
        else:
            count_move = 0
        temp_new_open_set = []
        new_open_set = []
        # if not best_path:
        for i in range(len(self.open_set)):
            x = self.open_set[i][0]
            y = self.open_set[i][1]
            if x == self.finish_col and y == self.finish_row:
                return count_move
            else:
                temp_new_open_set = [[x+i[0], y+i[1]] for i in self.move
                                     if x + i[0] >= 0 and  x + i[0] < self.col
                                     if y + i[1] >= 0 and  y + i[1] < self.row]
                for field in temp_new_open_set:
                    new_open_set.append(field)
                temp_new_open_set = []
        count_move += 1
        self.open_set = new_open_set
        return self.calculateShortestPath(count_move)


def knight(p1, p2):
    board = ChessBoard(p1, p2)
    result = board.calculateShortestPath(0)
    print(result)
    return result


knight('a1', 'h8')

# arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
# for x in arr:
#     z = knight(x[0], x[1])
#     Test.expect(z == x[2], "{} to {}: expected {}, got {}".format(x[0], x[1], x[2], z))


