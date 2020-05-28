# Codewar : Snail Sort

def snail(array):
    inputs = array
    result = []
    print(len(inputs))
    if len(inputs)<= 1:
        for input in inputs:
            return input
    else:
        i = 0
        start_i = 0
        start_j = 0
        end_i = len(inputs)
        end_j = len(inputs)
        while len(result) != len(inputs)*len(inputs):
            for j in range(start_j, end_j):
                result.append(inputs[i][j])
            start_i += 1
            for i in range(start_i, end_i):
                result.append(inputs[i][j])
            end_j -= 1
            for j in reversed(range(start_j, end_j)):
                result.append(inputs[i][j])
            end_i -= 1
            for i in reversed(range(start_i, end_i)):
                result.append(inputs[i][j])
            start_j += 1
        print(result)
        return result



array = [[1]]
expected = [1]
print(snail(array)== expected)






array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array)== expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array) == expected)