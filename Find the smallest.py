# 6 Exercise - Find the smallest

# # My soluction
# n = 9045863254479
# def smallest(n):
#     print(n)
#     n_str = (str(n))
#     result = []
#     minimum = min(str(n))
#     ind_minimum = n_str.index(minimum)
#     if ind_minimum == 0:# case when lower digit is in position 0
#         result = (smallest_ind_min_left(n))
#         return (result)
#     elif ind_minimum == 1:# case when lower digit is in position 1
#         result = (smallest_ind_position_one(n))
#         return(result)
#     else:# all other case when lower digit is not in position 0 and 1
#         result = (smallest_ind_min_right(n))
#         return(result)
#
# def consecutive_lower_rightPosition (n): #I call this function in: "def smallest_ind_min_right(n):"
#     n_str = (str(n))
#     minimum = min(str(n))
#     ind_minimum = n_str.index(minimum)
#     from0 = n_str.rfind(minimum)
#     while n_str[from0-1] == minimum: # find, if there is consecutive minimun, I find the minimum in left position
#         from0 -= 1
#     return (from0)
#
# def smallest_ind_min_right(n):# case when lower digit is not in position 0 or 1 and destination "to0" always 0
#     n_str = (str(n))
#     minimum = min(str(n))
#     ind_minimum = n_str.index(minimum)
#     ind_min_right = ind_minimum
#     ind_min_right = n_str.rfind(minimum)#rfind --> find(from the right) last minimum
#     removed = n_str[:ind_min_right] + n_str[ind_min_right+1:]
#     small_right = int(n_str[ind_min_right]+removed)
#     from0 = consecutive_lower_rightPosition (n)
#     to0 = 0
#     return[small_right, from0, to0]
#
# def smallest_ind_min_left(n):# case when lower digit is in position 0 (Ex.158974269--> new minimun "2" or 158974169 --> same minimun "1"
#     n_str = (str(n))
#     ind_min_left = 0
#     minimum = min(str(n))
#     ind_minimum = n_str.index(minimum)
#     minimum2 = minimum
#     ind_minimum2 = ind_minimum
#     ind_min_left = next( x for x,v in enumerate(n_str) if v != minimum)#n starts with lower digit (11185623). I find first position no minimun(position digit 8) to find second minimum (=2)
#     if ind_min_left > 0:
#         minimum2 = min(n_str[ind_min_left:])
#         ind_minimum2 = n_str.rfind(minimum2)#rfind --> find another right last minimum
#         while n_str[ind_minimum2-1] == minimum2: # find, if there is consecutive minimun2, I take the left minimun2
#             ind_minimum2 -= 1
#     if minimum == minimum2: # we are in the case of: "def smallest_ind_min_right(n):"
#         result = (smallest_ind_min_right(n))
#         return(result)
#     else:
#         removed = n_str[:ind_minimum2] + n_str[ind_minimum2+1:]
#         small_left = int(removed[:ind_min_left]+n_str[ind_minimum2]+removed[ind_min_left:])
#         from0 = ind_minimum2
#         to0 = ind_min_left
#         return[small_left, from0, to0]
#
# def smallest_ind_position_one(n): # case when lower digit is in position 1: we can move the first digit on the right until we find a digit higher
#     n_str = (str(n))              # and check the result with "def smallest_ind_min_right(n):" to find the smallest number
#     minimum = min(str(n))
#     ind_minimum = n_str.index(minimum)
#     to0 = next(((x) for x,v in enumerate(n_str) if n_str[0] < n_str[x]),len(n_str))##find position to create the smallest number - default len(n_str) (if numbert start e finish with 9)
#     print(to0)
#     removed = n_str[ind_minimum] + n_str[ind_minimum+1:]
#     small_pos1 = (removed[:to0-1]+n_str[0]+ removed[to0-1:])
#     while small_pos1[to0-1] ==  n_str[0]: # find, if there is consecutive minimun, I find the minimum in left position (Ex: 20229917 -->  small_pos1 = 022 2 9917 but the position is 1 not 3)
#         to0 -= 1
#     small_pos1 = int(small_pos1)
#     from0 = 0
#     result=smallest_ind_min_right(n)
#     small_pos1_str = str(small_pos1)
#     if small_pos1 <= result[0]: #I compare number(small_pos1) with the number with smallest_ind_min_right(n)
#         return[small_pos1, from0, to0]
#     else:
#         result = (smallest_ind_min_right(n))
#         return(result)
# result = smallest(n)
# print(result)

# #How manage a default value if the list is empy in min() function
# print("="*20)
# mylist = []
# minimum = min((mylist),default=2)
# print(minimum)


# #Best Solution (this solution trying every single digit calculating a new number that will be comparate with the previus smallest number)
# def smallest(n):
#     s = str(n)
#     min1, from1, to1 = n, 0, 0
#     #print(min1)
#     for i in range(len(s)):
#         part_one = s[:i]
#         part_two = s[i+1:]
#         part_three = s[-(i+1):]
#         part_four = s[:-i]
#         removed = s[:i] + s[i+1:]
#         #print(removed)
#         for j in range(len(removed)+1):
#             sec_one = removed[:j]
#             sec_two = removed[j:]
#             num = int(removed[:j] + s[i] + removed[j:]) #with j==0 --> remove[:j} == '' and remove[:j] == '09917'????
#             #print(num)
#             if (num < min1):
#                 min1, from1, to1 = num, i, j
#     return [min1, from1, to1]




#Other Best Soluction



#def smallest(n):
n= 2099752
smallest = n
takenIndex = 0
placedIndex = 0
numList = [int(x) for x in str(n)]
for i in range(0, len(numList)):
    currentNum = numList[i]
    for j in range(0, len(numList)):
         #move i to j, see if smallest
         testList = list(numList)
         print(testList)
         testList.pop(i)
         print(testList)
         testList.insert(j, currentNum)
         print(testList)
         print("="*20)
         testNum = int(''.join(map(str,testList)))
         print(testNum)
         testTest = int(''.join(str(testList))) #to understand the function above: maybe we need to use map function because we are inside at for loop(iteration)
                                                # maybe in this case we have a list of 'str" function so we need to use map????
         print(testTest)
         print("/"*20)
         if testNum < smallest:
            smallest = testNum
            takenIndex = i
            placedIndex = j
    #return [smallest, takenIndex, placedIndex]


#
# print(n)
# print(numList)
# #result = smallest(n)
# #print(result)
# print(smallest)
# print(takenIndex)
# print(placedIndex)


# n = 1234567
# print(n)
# s = str(n)
# reversed = s[::-1]
# iD = next(((index,value) for index,value in enumerate(reversed) if value > (reversed[index+1])))
# #iD2 = next(((x,v) for x,v in enumerate (reversed(s)) if v > (s[x+1]) #or (x+1 <= len(s)-1)))   # first non increasing digit - My duplication
# print(iD)
# #print(iD2)

# #def smallest(n):
# s = str(n)
# iD = next( (x) for x,v in enumerate(s) if v > s[x+1] )                # first non increasing digit
# print(iD)                                                           # Example: n = 9009460129
# minD = min(s[iD:])
# print(minD)
# # Why it doen't calculate the minimum with(min(s))
#
# i = s.rfind(minD)                                                   # rightmost minimal digit in "s except the first increasing part"
# print(i)                                                            # Try this part with n = 12345970054
# print("*"*20)
# while s[i-1] == minD:
#     i -= 1                                                          # if several consecutive min digits, step backward to minimize i
# print(i)
# j = next( x for x in range(i) if s[x] >= minD )                     # find the first digit from the beginnning whose the value is "minD"
# print("="*20)
# print(j)
# print("+"*20)
# ans = [ [int(s[:j] + s[i] + s[j:i] + s[i+1:]), i, j] ]              # store the first answer. we work this case taking the right lower digit
# print(n)
#
# j = next( (x for x in range(iD+1,len(s)) if s[x] > s[iD]), len(s))  # seek the place where the first non increasing digit could be placed (search the next digit that is strictly bigger)
# print(j)
# while j > 0 and s[j-1] == s[iD]:
#     j -= 1                                                          # if the previous digit is/are equal to s[iD], step backward to minimize j
#     print(j)
# ans.append([ int(s[:iD] + s[iD+1:j] + s[iD] + s[j:]), iD, j-1 ])    # store the datas. We work this case moving the digit in position 0 to right until we found a digit higher as lower difit position 1
# print(ans)                                                          # when we are not in the case od lower digit is position 0. we create a number really hitg so it is better the previous solution
# #return min(ans)                                                     # pick the good one...



# def smallest(n):
#     s = str(n)
#     iD = next( x for x,v in enumerate(s) if v > s[x+1] )                # first non increasing digit
#     minD = min(s[iD:])
#
#     i = s.rfind(minD)                                                   # rightmost minimal digit in "s except the first increasing part"
#     while s[i-1] == minD: i -= 1                                        # if several consecutive min digits, step backward to minimize i
#     j = next( x for x in range(i) if s[x] >= minD )                     # find the first digit from the beginnning whose the value is "minD"
#     ans = [ [int(s[:j] + s[i] + s[j:i] + s[i+1:]), i, j] ]              # store the first answer
#
#     j = next( (x for x in range(iD+1,len(s)) if s[x] > s[iD]), len(s))  # seek the place where the first non increasing digit could be placed (search the next digit that is strictly bigger)
#     while j > 0 and s[j-1] == s[iD]: j -= 1                             # if the previous digit is/are equal to s[iD], step backward to minimize j
#     ans.append([ int(s[:iD] + s[iD+1:j] + s[iD] + s[j:]), iD, j-1 ])    # store the datas
#
#     return min(ans)                                                     # pick the good one...



# You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in
# the number, remove this digit at that index and insert it back to another or at the same place in the number in order
# to find the smallest number you can get.
#
# #Task: Return an array or a tuple or a string depending on the language (see "Sample Tests") with
#
# 1) the smallest number you got
# 2) the index i of the digit d you took, i as small as possible
# 3) the index j (as small as possible) where you insert this digit d to have the smallest number.
# Example:
#
# smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
# 126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0
#
# smallest(209917) --> [29917, 0, 1] or ...
#
# [29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than
# index `i` in [29917, 0, 1].
# 29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is
# the number 29917.
#
# smallest(1000000) --> [1, 0, 6] or ...
# Note
# Have a look at "Sample Tests" to see the input and output in each language






