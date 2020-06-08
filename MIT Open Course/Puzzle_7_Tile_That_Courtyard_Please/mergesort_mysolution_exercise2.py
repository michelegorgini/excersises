# Michele: exercise 2, my solution works but I don't understand if I followed teacher's instructions. I used the
# mergersort program because in both cases I enter in 'mergeSort' with and array that has a number of elements
# multiple of 4. If my row = 1, col = 2 and the number to find is 7 -> doesn't work.
def checkValue(T, row, col, number):

    numberknew = T[row][col]
    rowTotal = len(T[0])
    colTotal = rowTotal
    positionNumberT= []
    for i in range(rowTotal):
        for j in range (colTotal):
            if T[i][j]== number:
                positionNumberT.append([T[i][j], [i, j]])

    # case when number is <= of value in position [row][col]
    if numberknew >= number:
        leftUpperT = []
        for indrow in range(0, rowTotal-row):
            for indcol in range(0, colTotal-col):
                print(T[row][col],T[indrow][indcol], 'check')
                if T[row][col] != T[indrow][indcol]:
                    leftUpperT.append(T[indrow][indcol])
                else:
                    continue
        if len(leftUpperT)% 4 == 0:
            results = mergeSort(leftUpperT)
            for index in range(len(results)):
                if results[index] == positionNumberT[0][0]:
                    print('Number: ', number, 'is in position: ',positionNumberT[0][1])
                    return positionNumberT[0][1]
        else:
            exit('No Solution, array L in mergeSort has not multiple of 4 elements')

    # case when number is > of value in position [row][col]
    if numberknew < number:
        otherT = []
        for indrow in range(0, rowTotal):
            for indcol in range(0, rowTotal):
                if indrow > row and indcol <= col:
                    otherT.append(T[indrow][indcol])
                elif indrow <= row and indcol > col:
                    otherT.append(T[indrow][indcol])
                elif indrow > row and indcol > col:
                    otherT.append(T[indrow][indcol])
                else:
                    continue
        if len(otherT)% 4 == 0:
            results = mergeSort(otherT)
            for index in range(len(results)):
                if results[index] == positionNumberT[0][0]:
                    print('Number: ', number, 'is in position: ',positionNumberT[0][1])
                    return positionNumberT[0][1]
        else:
            exit('No Solution, array L in mergeSort has not multiple of 4 elements')



def mergeSort(L):
    print(L, 'Recursive step', len(L), 'num element')

    if len(L) == 2:
        print('2 Elements Ordered')
        if L[0] <= L[1]:
            return [L[0], L[1]]
        else:
            return [L[1], L[0]]
    else:
        middle = len(L)//2
        print('Start Left')
        left = mergeSort(L[:middle])
        print('Start Right')
        right = mergeSort(L[middle:])
        return merge(left, right)



def merge(left, right):
    print(left, 'Left', right, 'Right')
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print(result, "Final Result")
    return result

T=[[1,4,7,11,15],
   [2,5,8,12,19],
   [3,6,9,16,22],
   [10,13,14,17,24],
   [18,21,23,26,30]]

checkValue(T, 3, 3, 21)



