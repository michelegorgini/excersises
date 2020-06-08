# Michele: I add an argument (quadList) to recursiveTile function to know in during the print in which mini-board I am.
# My Solution is integrated in the algorithm the teacher's solution give us only a procedure, it's not integrated
# it doesn't give us the printed solution. My solution gives it.

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
def recursiveTile(yard, size, originR, originC, rMiss, cMiss, nextPiece, quadList, tromPos):

    #quadrant of missing square: 0 (upper left), 1 (upper right),
    #                            2 (lower left), 3 (lower right)
    # Michele: 2*(True) = 2 , 2*(False) = 0, I DON'T KNOW. IMPORTANT TO REMEMBER

    tmp_tromPos = []
    quadMiss = 2*(rMiss >= size//2) + (cMiss >= size//2)

    print(size,'Board Dimension - ', quadList, 'which mini board? - ', rMiss, 'Row miss - ', cMiss, 'Column miss - ', nextPiece, 'value to fix')

    #base case of 2x2 yard
    if size == 2:
        piecePos = [(0,0), (0,1), (1,0), (1,1)]
        piecePos.pop(quadMiss)
        for (r, c) in piecePos:
            yard[originR + r][originC + c] = nextPiece
            tmp_tromPos.append([originR + r,originC + c])
        tromPos.append(tmp_tromPos)
        # print(tmp_tromPos,'last', tromPos, 'Check content')
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

        #print(quadList[-1][0])
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
                originC + shiftC, rMiss - shiftR, cMiss - shiftC, nextPiece, quadList, tromPos)

        else:
            #The missing square is different for each of the other 3 quadrants
            newrMiss = (size//2 - 1) * (quad < 2)
            newcMiss = (size//2 - 1) * (quad % 2 == 0)
            #print('New position miss', newrMiss, newcMiss)
            nextPiece = recursiveTile(yard, size//2, originR + shiftR,\
                            originC + shiftC, newrMiss, newcMiss, nextPiece, quadList, tromPos)


    #place center tromino
    centerPos = [(r + size//2 - 1, c + size//2 - 1)
                 for (r,c) in [(0,0), (0,1), (1,0), (1,1)]]
    centerPos.pop(quadMiss)
    print(centerPos, 'Place center tromino', quadMiss, 'quadrant with miss tile')
    for (r,c) in centerPos: # assign tile to 3 center squares
        yard[originR + r][originC + c] = nextPiece
        tmp_tromPos.append([originR + r,originC + c])
        print( 'board value ', nextPiece, ' - ',size//2, 'dimension - ')
    tromPos.append(tmp_tromPos)
    nextPiece = nextPiece + 1


    return nextPiece

def checkConditions(yard, size, originR, originC, missList, nextPiece, quadList, tromPos):

    missList = sorted(missList, key= lambda  x:(x[0], x[1])) # Sort missList by first element
    # print(missList, 'Sorted')

    quadMissList = []     # number elements == number different quadrants
    quadPosition = []     # first= number of miss tile with same quadrant, second = position single element

    for i in range(len(missList)):
        rMiss = missList[i][0]
        cMiss = missList[i][1]
        quadMiss= 2*(rMiss >= size//2) + (cMiss >= size//2)
        if quadMiss not in quadMissList:
            quadMissList.append(quadMiss)
        countSamequad = 0
        for j in range(len(missList)):
            rMiss = missList[j][0]
            cMiss = missList[j][1]
            next_quadMiss= 2*(rMiss >= size//2) + (cMiss >= size//2)
            if quadMiss == next_quadMiss:
                countSamequad+=1
        quadPosition.append((countSamequad, missList[i]))

    # Check four different quadrants
    if len(quadMissList) == 4:    # 4 different quadrants. I enter in recursive function with size = 4 . Remember this!
        for ind in range(len(missList)):
            rMiss = missList[ind][0]
            cMiss = missList[ind][1]
            # I determine the origin position and missing position for every quadrants
            quadMiss = 2*(rMiss >= size//4) + (cMiss >= size//4)
            quadList = [[size//2, quadMiss]]
            if rMiss >= 4  and cMiss >= 4:
                originR = 4
                originC = 4
                rMiss = rMiss -originR
                cMiss = cMiss - originC
            elif rMiss >= 4  and cMiss < 4:
                originR = 4
                originC = 0
                rMiss = rMiss -originR
            elif rMiss < 4  and cMiss >= 4:
                originR = 0
                originC = 4
                cMiss = cMiss - originC
            nextPiece = recursiveTile(yard, size//2, originR , originC , rMiss, cMiss, nextPiece, quadList, tromPos)
        return yard



    # Check possible right position of tronomio
    if len(quadMissList) == 2:     # 2 different quadrants, so 3 tiles same quadrants
        positionMiss = []          # Position element stays alone in quadrant
        positionTrinomios = []     # Position 3 elements stays together in same quadrants
        for index in range(len(quadPosition)):
            if quadPosition[index][0] == 1:
                positionMiss.append(quadPosition[index][1])
            elif quadPosition[index][0] == 3:
                positionTrinomios.append(quadPosition[index][1])
        rMiss = positionMiss[0][0]
        cMiss = positionMiss[0][1]
        quadMiss = 2*(rMiss >= size//2) + (cMiss >= size//2)
        quadList = [[size, quadMiss]]
        recursiveTile(yard, size, originR, originC, rMiss, cMiss, 0, quadList, tromPos)
        # we check if our 'positionTrinomios' is present in a lists of the tromPos list (where we have all the
        # combinations of 3 elements we have already signed with a numbers.
        for k in range(len(tromPos)):
            checkTrinomio = 0
            for z in range(0, 3):
                for x in range(len(positionTrinomios)):
                    if tromPos[k][z] ==  positionTrinomios[x]:
                        # print(tromPos[k], positionTrinomios[x], '????????')
                        checkTrinomio += 1
            if checkTrinomio == 3:
                return yard
    exit('No possible Solution')


#This procedure is a wrapper for recursiveTile that does all the work
def tileMissingYard(n, missList):
    #Initialize yard, this is the only memory that will be modified!

    yard = [[EMPTYPIECE for i in range(2**n)]
            for j in range(2**n)]
    print('Before recursiveTile', *yard, sep='\n')
    # recursiveTile(yard, 2**n, 0, 0,  missList, 0, [])
    checkConditions(yard, 2**n, 0, 0,  missList, 0, [], [])
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


# printYard(tileMissingYard(3, [[6, 0], [7, 0], [7, 1], [0, 2]]))
# printYard(tileMissingYard(3, [[6, 1], [7, 0], [7, 1], [0, 2]]))
printYard(tileMissingYard(3, [[5, 5], [7, 0], [2, 6], [0, 2]]))
# printYard(tileMissingYard(4, 5, 7))



