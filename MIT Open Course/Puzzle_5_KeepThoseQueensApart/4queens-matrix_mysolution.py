# Michele: It's not my solution but I put a lot of print -> command to understand every steps


#Programming for the Puzzled -- Srini Devadas
#Keep Those Queens Apart
#Given a 4 x 4 "chess" board, figure out how to place 4 Queens such that
#no Queen attacks another queen.
#This code uses a two-dimensional list or matrix data structure

#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current, qindex, n = 4):
    
##    #We do not need this check given how we call noConflicts()
##    #Check that there is a single 1 in the current column
##    ones = 0
##    for i in range(n):
##        if board[i][current] == 1:
##            ones += 1
##            qindex = i
##    if ones > 1:
##        return False



    #check that the row on which the current queen is only has one queen on it
    # INPUT --> current = column board:    qindex= row board
    for j in range(current):
        if board[qindex][j] == 1:
            return False

    #Check the two diagonals from the current queen
    #The first loop is for the diagonal /
    #The second loop is for the diagonal \
    k = 1
    while qindex - k >= 0 and current - k >= 0:
        if board[qindex - k][current - k] == 1:
            return False
        k += 1
    k = 1
    while qindex + k < n and current - k >= 0:
        if board[qindex + k][current - k] == 1:
            return False
        k += 1

    return True 


#This procedure places 4 Queens on a board so they don't conflict
#It assumes n = 4 and won't work with other n!
def FourQueens(n):

    board = [[8] * n for i in range(n)]     # code from file=shortest_knight_path.py -- For better visualization !!!
    #print(*board, sep='\n')

    #Initialize the board to be empty
    # board = [ [9, 9, 9, 9],
    #           [9, 9, 9, 9],
    #           [9, 9, 9, 9],
    #           [9, 9, 9, 9] ]

    #print(board[1][0])

    #Place a queen a column at a time beginning with leftmost column
    for i in range(n):                                               # Loop for 1 Queen in column 0 row ?
        board[i][0] = 1
        print('1 Queen column 0 row:', i)
        print(*board, sep='\n')
        print('='*20)
        for j in range(n):                                           # Loop for 2 Queen in column 1 row ?
            board[j][1] = 1
            print('2 Queen Try column 1 row:', j)
            print(*board, sep='\n')
            if noConflicts(board, 1, j, n):
                print('===== 2 Queen Good')
                for k in range(n):                                   # Loop for 3 Queen in column 2 row ?
                    board[k][2] = 1
                    print('3 Queen Try column 2 row:', k)
                    print(*board, sep='\n')
                    if noConflicts(board, 2, k, n):
                        print('===== 3 Queen Good')
                        for m in range(n):
                            board[m][3] = 1
                            print('4 Queen Try column 3 row:', m)    # Loop for 4 Queen in column 3 row ?
                            print(*board, sep='\n')
                            if noConflicts(board, 3, m, n):
                                print('Final result')
                                print(*board, sep='\n')
                            board[m][3] = 0
                            print('*'*20)
                            print('= 4 Queen Try Failed!!!','colon: ', 3, 'row: ', m)
                        print('No Position for 4 Queen -> Re-check 3 Queen')
                    board[k][2] = 0
                    print('-'*20)
                    print('= 3 Queen Try Failed!!!','colon: ', 2, 'row: ', k)
                print('No Position for 3 Queen -> Re-check 2 Queen')
            board[j][1] = 0
            print('+'*20)
            print('= 2 Queen Try Failed!!!','colon: ', 1, 'row: ', j)
        print('No Position for 2 Queen -> Re-check 1 Queen')
        print('\=/'*20)
        print('= 1 Queen Try Failed!!!','colon: ', 0, 'row: ', i)
        board[i][0] = 0

    return


FourQueens(4)
