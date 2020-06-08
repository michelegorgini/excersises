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

    # Exercise 2
    # location = [-1, -1, 4, -1, -1, -1, -1, 0, -1, 5]   # with the teacher's input works
    location = [-1, -1, 4, -1, -1, -1, -1, -1, -1, 9]   # works also with two consecutive queen fixed
    # location = [-1, -1, 4, -1, -1, -1, -1, 0, 5, -1]  # No find solution or the program has a bug??????
    # location = [-1, -1, 4, -1, -1, -1, -1, 0, 3, 5]    # It works

    # board = [-1] * size
    board = list(location)     # Exercise 3
    print(board, 'Start')
    # Exercise 3:I create a new list with only the queen positions already fixed -> value different by -1
    queenFixed = []
    for q in range(len(location)):
        if location[q] != -1:
            queenFixed.append(q)

    if rQueens(location, board, 0, size, queenFixed):
        printBoard(size, board)
    else:
        print('No Solution Found')


    # print(board, 'Result')


#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current, n):
    for i in range(n):
        if i == current or board[i] == -1:
            continue
        else:
            if (board[i] == board[current]):
                return False
            if (abs(current - i) == abs(board[current] - board[i])):   # Exercise 3
                return False
    return True 


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(location, board, current, size, queenFixed):
    if (current == size):
        return True
    else:
        for i in range(size):
            print(board, 'For Loop',i, current)
            # # Exercise 3: every time I come back one position (p-1) I re-fix the right position (p+1:size) with
            # the start (location)
            if current < size-1:
                board[current+1:size] = location[current+1:size]
            # # Exercise 3: Increment the Queen row starting from 0 (i) only if I found -1 in location same position
            if location[current] == -1:
                board[current] = i
                print(board, 'before noConflict', i, current)
            if (noConflicts(board, current, size)):
                # # Exercise 3: I jump fixed Queen Position (current + 1 become next)
                next = current + 1
                for i in range(len(queenFixed)):
                    if queenFixed[i] == next:
                        next += 1
                done = rQueens(location, board, next, size, queenFixed)
                if (done):
                    return True

        return False

def printBoard(n,  boardlist):
    print(boardlist)
    board = [['.'] * n for i in range(n)]   # Display: Why when I print the board I have '.' instead of .
    print('='*20)

    for i in range(n):
        board [boardlist[i]][i] = 'Q'
    print('Final Resul',*board, sep='\n')

#board = [[8] * n for i in range(n)]     # code from file=shortest_knight_path.py -- For better visualization !!!
#print(*board, sep='\n')

nQueens(10)
