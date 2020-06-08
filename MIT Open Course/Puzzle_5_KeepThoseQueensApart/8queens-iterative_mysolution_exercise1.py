#Programming for the Puzzled -- Srini Devadas
#Keep Those Queens Apart
#Given a 8 x 8 chess board, figure out how to place 8 Queens such that
#no Queen attacks another queen.
#This code uses a single-dimensional list to represent Queen positions


#This procedure checks that the most recently placed queen on the board on column
#current does not conflict with existing queens.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        #We have two diagonals hence need the abs()
        # If we have the same different between colomns "current - i" and rows "abs(board[current] - board[i])"
        # the Quenns are on the same diagonal. Mathematics Theorem. Really Nice.
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places 8 Queens on a board so they don't conflict.
#It assumes n = 8 and won't work with other n!
def EightQueens(n, n_solution):
    count_solution = 0
    board = [-1] * n
    print('$'*20)
    print(board)
    #print(*board, sep='\n')
    print('$'*20)
    for i in range(n):
        board[0] = i
        print(board, 'Start 1 step')
        for j in range(n):
            board[1] = j
            print(board, 'Start 2 step')
            if not noConflicts(board, 1):
                    continue
            for k in range(n):
                board[2] = k
                print(board, 'Start 3 step')
                if not noConflicts(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    print(board, 'Start 4 step')
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        print(board, 'Start 5 step')
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            print(board, 'Start 6 step')
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                print(board, 'Start 7 step')
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    print(board, 'Start 8 step')
                                    if noConflicts(board, 7):
                                        count_solution += 1                 # Exercise : solution from this line
                                        if count_solution <= n_solution:
                                            print(board, 'final result')
                                        else:
                                            exit(print('You get your: ', n_solution, ' Solution'))

    return


EightQueens(8, 10)

