# Michele: I add an argument (quadList) to recursiveTile function to know in during the print in which mini-board I am.


#Programming for the Puzzled -- Srini Devadas
#Tile that Courtyard, Please
#Given n in a 2^n x 2^n checkyard with a missing square at position (r, c), 
#find tiling of yard with trominoes (L-shaped dominoes).
#This version works directly on the given grid, and does NOT make copies
#of the grid for recursive calls.

EMPTYPIECE = -1



#This procedure is the main engine of recursive algorithm
#nextPiece is the number of next available tromino piece
#The origin coordinates of the yard are given by originR and originC
def recursiveTile(yard, size, originR, originC, rMiss, cMiss, nextPiece, quadList):

    #quadrant of missing square: 0 (upper left), 1 (upper right),
    #                            2 (lower left), 3 (lower right)
    # Michele: 2*True = 2 , 2*False = 0, I DON'T KNOW. IMPORTANT TO REMEMBER
    print(quadList)

    quadMiss = 2*(rMiss >= size//2) + (cMiss >= size//2)

    print(size,'Board Dimension - ', quadList, 'which mini board? - ', rMiss, 'Row miss - ', cMiss, 'Column miss - ', nextPiece, 'value to fix')

    #base case of 2x2 yard
    if size == 2:
        piecePos = [(0,0), (0,1), (1,0), (1,1)]
        piecePos.pop(quadMiss)
        for (r, c) in piecePos:
            yard[originR + r][originC + c] = nextPiece
        print( 'board value ', nextPiece, ' - ',size, 'dimension - ')
        nextPiece = nextPiece + 1

        return nextPiece

    #recurse on each quadrant

    for quad in range(4):
        #Each quadrant has a different origin
        #Quadrant 0 has origin (0, 0), Quadrant 1 has origin (0, size//2)
        #Quadrant 2 has origin (size//2, 0), Quadrant 3 has origin (size//2, size//2)
        # Michele: we need to add shiftR, shiftC to originR, originC -> for new origins

        # Michele: I created and insert in the recursive function quadList to understand which mini-board I am working
        # on [first element = dimension, second element = quadrant of dimension]

        if quadList[-1][0] == size//2:
            quadList.pop(-1)
            quadList.append([size//2, quad])
        elif quadList[-1][0] < size//2:
            quadList = [quadList[0]]
            quadList.append([size//2, quad])
        else:
            quadList.append([size//2, quad])

        shiftR = size//2 * (quad >= 2)
        shiftC = size//2 * (quad % 2 == 1)
        if quad == quadMiss:
            #Pass the new origin and the shifted rMiss and cMiss
            nextPiece = recursiveTile(yard, size//2, originR + shiftR,\
                originC + shiftC, rMiss - shiftR, cMiss - shiftC, nextPiece, quadList)

        else:
            #The missing square is different for each of the other 3 quadrants
            newrMiss = (size//2 - 1) * (quad < 2)
            newcMiss = (size//2 - 1) * (quad % 2 == 0)
            nextPiece = recursiveTile(yard, size//2, originR + shiftR,\
                            originC + shiftC, newrMiss, newcMiss, nextPiece, quadList)


    #place center tromino
    print('- Start center tile for dimension', size)
    centerPos = [(r + size//2 - 1, c + size//2 - 1)
                 for (r,c) in [(0,0), (0,1), (1,0), (1,1)]]
    centerPos.pop(quadMiss)
    print(centerPos, 'Place center tromino', quadMiss, 'quadrant with miss tile')
    for (r,c) in centerPos: # assign tile to 3 center squares
        yard[originR + r][originC + c] = nextPiece
        print( 'board value end function ', nextPiece, ' - ',size//2, 'dimension - ')
    nextPiece = nextPiece + 1

    print(nextPiece, ' nextPiece Return function')
    return nextPiece  # Great idea! we can update nextPiece for the call to recursive function not close

#This procedure is a wrapper for recursiveTile that does all the work
def tileMissingYard(n, rMiss, cMiss):
    #Initialize yard, this is the only memory that will be modified!
    yard = [[EMPTYPIECE for i in range(2**n)]
            for j in range(2**n)]
    print('Before recursiveTile', *yard, sep='\n')
    quadMiss = 2*(rMiss >= 2**n//2) + (cMiss >= 2**n//2)
    recursiveTile(yard, 2**n, 0, 0, rMiss, cMiss, 0, [[2**n, quadMiss]])
    print('After recursiveTile', *yard, sep='\n')
    return yard

#This procedure prints a given tiled yard using letters for tiles
def printYard(yard):
    for i in range(len(yard)):
        row = ''
        for j in range(len(yard[0])):
            if yard[i][j] != EMPTYPIECE:
                row += chr((yard[i][j] % 26) + ord('A'))     # 26 lettters of alphabet
            else:
                row += ' '
        print (row)


printYard(tileMissingYard(3, 4, 6))
# printYard(tileMissingYard(4, 5, 7))



# def convertToDecimal(r=2, d=5, rep=[1, 4, 7, 11, 15]):
#     number = 0
#     for i in range(d-1):
#         number = (number + rep[i]) * r
#         print(number)
#     number += rep[d-1]
#     print('='*20)
#     print(number)
#
#     return number
