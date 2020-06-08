# Michele: I try to improve exercixe 2 lines 128-142

#Programming for the Puzzled -- Srini Devadas
#Keep Those Queens Apart
#Given a 8 x 8 chess board, figure out how to place 8 Queens such that
#no Queen attacks another queen.
#This code uses a single-dimensional list to represent Queen positions


#This procedure checks that the most recently placed queen on the board on column
#current does not conflict with existing queens.
# Michele: in this case I need to check all the values present in the board because I have already one or more Quenn
# with the row position pre-fix
def noConflicts(board, current, n):
    for i in range(n):
        if i == current or board[i] == -1:
            continue
        else:
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
    results = []
    location = [-1, 4, -1, -1, -1, -1, -1, 0]      # Exercise 2
    count_solution = 0
    #board = [-1] * n
    board = list(location)
    #print(*board, sep='\n')
    print(location, 'Location')
    print('$'*20)
    print(board, 'board')
    print('$'*20)
    for i in range(n):
        if board[1] != location[1]:
            board[1] = location[1]
        if location[0] == -1:
            board[0] = i
            # print(board, 'Start 1 step')
            if not noConflicts(board, 0, n):
                if location[0] == -1:
                    continue
                else:
                    break
        #print(board, 'finish 1 step')
        for j in range(n):
            if board[2] != location[2]:
                board[2] = location[2]
            if location[1] == -1:
                board[1] = j
                # print(board, 'Start 2 step')
                if not noConflicts(board, 1, n):
                    if location[1] == -1:
                        continue
                    else:
                        break
            for k in range(n):
                if board[3] != location[3]:
                    board[3] = location[3]
                if location[2] == -1:
                    board[2] = k
                    # print(board, 'Start 3 step')
                    if not noConflicts(board, 2, n):
                        if location[2] == -1:
                            continue
                        else:
                            break
                for l in range(n):
                    if board[4] != location[4]:
                        board[4] = location[4]
                    if location[3] == -1:
                        board[3] = l
                        # print(board, 'Start 4 step')
                        if not noConflicts(board, 3, n):
                            if location[3] == -1:
                                continue
                            else:
                                break
                    for m in range(n):
                        if board[5] != location[5]:
                            board[5] = location[5]
                        if location[4] == -1:
                            board[4] = m
                            # print(board, 'Start 5 step')
                        if not noConflicts(board, 4, n):
                            if location[4] == -1:
                                continue
                            else:
                                break
                        for o in range(n):
                            if board[6] != location[6]:
                                board[6] = location[6]
                            if location[5] == -1:
                                board[5] = o
                                # print(board, 'Start 6 step')
                                if not noConflicts(board, 5, n):
                                    if location[5] == -1:
                                        continue
                                    else:
                                        break
                            for p in range(n):
                                if board[7] != location[7]:
                                    board[7] = location[7]
                                if location[6] == -1:
                                    board[6] = p
                                    # print(board, 'Start 7 step')
                                    if not noConflicts(board, 6, n):
                                        if location[6] == -1:
                                            continue
                                        else:
                                            break
                                for q in range(n):
                                    if location[7] == -1:
                                        board[7] = q
                                    #print(board, 'Start 8 steps')
                                    if noConflicts(board, 7, n):
                                        # I use list results because in this case I can get the same solution more times
                                        # print(board, 'board', results, 'results before append')
                                        tmp_board = list(board)             # If I use board instead tmp_board I insert
                                        if not tmp_board in results:        # the same record a lot of times
                                            results.append(tmp_board)
                                        break
                                    else:
                                        continue

    for result in results:
        print(result, 'Final Result')

    return


EightQueens(8, 2)

