#Programming for the Puzzled -- Srini Devadas
#Tile that Courtyard, Please

#mergeSort: Recursive Divide-and-Conquer algorithm.

#This procedure assumes left and right are sorted lists in ascending order,
#and merges them to produce a sorted list in ascending order.
#This procedure returns a new sorted list containing the same elements as L.
#L is not modified.
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
    print('Left', left, 'Right', right)
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


inp = [23, 3, 45, 7, 6, 11, 14, 12]
mergeSort(inp)




