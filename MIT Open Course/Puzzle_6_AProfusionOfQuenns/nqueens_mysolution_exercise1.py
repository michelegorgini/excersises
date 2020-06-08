# Michele: It's not my solution but I add some code to print out some result and unserstand the logic

#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens
#Given the dimension of a square "chess" board, call it N, find a placement
#of N queens such that no two Queens attack each other using recursive search

#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
def nQueens(size):

    #board = [[8] * n for i in range(n)]     # code from file=shortest_knight_path.py -- For better visualization !!!
    #print(*board, sep='\n')

    board = [-1] * size
    print(board, 'Start')
    rQueens(board, 0, size)
    # ?? In the line above we don't have if (rQueens(board, 0, size)) so if True get on, but the behaviour is the same

    print(board, 'Result')
    printBoard(size, board)

#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(board, current, size):
    if (current == size):
        return True
    else:
        for i in range(size):
            board[current] = i
            if (noConflicts(board, current)):
                done = rQueens(board, current + 1, size)
                if (done):
                    return True
        return False

def printBoard(n,  boardlist):

    board = [['.'] * n for i in range(n)]   # Display: Why when I print the board I have '.' instead of .
    # board = ('. ' * n for i in range(n))      # I solved the below question. With the Teacher's code but I can't use
    #                                           # the follow loop to fix the Queen because I don't have more a list
    print('='*20)
    # print(*board, sep='\n')

    for i in range(n):
        board[boardlist[i]][i] = 'Q'
    print(*board, sep='\n')

#board = [[8] * n for i in range(n)]     # code from file=shortest_knight_path.py -- For better visualization !!!
#print(*board, sep='\n')

nQueens(20)
