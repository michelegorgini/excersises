# Michele: exercise 3, my Solution works and I think I followed the teacher's instructions.


def prepareCheck(T, number):
    rowTotal = len(T[0])
    row = 0
    while T[row][0:rowTotal]:
        # print(T[row][0:rowTotal-minus])
        minus = checkValue(T[row][0:rowTotal], row, number, rowTotal)
        # print(minus, 'minus', rowTotal, 'len new row')
        if not minus:
            row+= 1
            continue
        else:
            row += 1
            rowTotal = rowTotal - minus





def checkValue(L, row,  number, rowTotal):
    # print(L, "Enter in Check", number)
    for col in range(len(L)):
        if L[col] == number:
            print('Number: ', number, 'is in position: row = ', row, ' col = ', col)
            exit()
        elif L[col] > number:
            return rowTotal-col
        else:
            continue
    return False


T=[[1,4,7,11,15],
   [2,5,8,12,19],
   [3,6,9,16,22],
   [10,13,14,17,24],
   [18,21,23,26,30]]

prepareCheck(T, 13)



