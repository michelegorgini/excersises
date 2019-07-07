
# 1 Exercise
# def final_grade(exam, projects):
#     if exam > 90 or projects > 10:
#         return(100)
#     elif (exam >75 and exam <90) or (projects > 5):
#         return (90)
#     elif (exam >50 and exam <75) or (projects > 2):
#         return (75)
#     else:
#         return(0)
#
#
#
#     return # final grade
#
# result = final_grade(100, 12)
# print(result)
# # projects.
# #
# # This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed
# projects (from 0 and above);
# #
# # This function should return a number (final grade). There are four types of final grades:
# #
# # 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# # 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# # 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# # 0, in other cases
#========================================
# 2 Exercise

# def digital_root(n):
#     result=0
#     while n > 0:
#         d = n%10
#         n = n//10
#         result += d
#         if (n==0) and (result >9):
#             n = result
#             result=0
#     return(result)
#
# result = digital_root(669)
# print(result)
#
# x=66%10
# print(x)
#
# r=66//10
# print(r)


# In this kata, you must create a digital root function.
#
# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that
# value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only
# applicable to the natural numbers.
#
# Here's how it works:
#
# digital_root(16)
# => 1 + 6
# => 7
#
# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6
#
# digital_root(132189)
# => 1 + 3 + 2 + 1 + 8 + 9
# => 24 ...
# => 2 + 4
# => 6
#
# digital_root(493193)
# => 4 + 9 + 3 + 1 + 9 + 3
# => 29 ...
# => 2 + 9
# => 11 ...
# => 1 + 1
# => 2
#============================================================

# 3 Exercise

# def unique_in_order(iterable):
#     output =[]
#     word=''
#     pos=''
#     for i in iterable:
#         if (i != word) and (iterable.index(i) != pos):
#             output.append(i)
#             word = i
#             pos = iterable.index(i)
#     return(output)
#
# iterable = 'AAAABBBCCDAABBB'
# output = unique_in_order(iterable)
# print(output)

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
# elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

#============================================================

# 4 Exercise - Equal Sides Of An Array

# My solution!!!
# def find_even_index(arr):
#     n=0
#     sum_left = 0
#     sum_right = 0
#     pos_left = -1
#     tot_pos = len(arr)
#     pos_right = tot_pos
#     for z in reversed (arr):
#         sum_right+=z
#         pos_right -=1
#         if (sum_right == 0 and pos_right == 1) or (tot_pos == 1):
#             n = 0
#             return(n)
#             break
#         else:
#             continue
#     for i in arr:
#         sum_left+=i
#         pos_left +=1
#         sum_right =0
#         pos_right = tot_pos
#         if sum_left == 0 and tot_pos - pos_left == 2:
#             n= pos_left+1
#             return(n)
#             break
#         for j in reversed(arr):
#             sum_right+=j
#             pos_right -=1
#             if pos_right- pos_left == 2 and (sum_left == sum_right):
#                 n = pos_left+1
#                 return(n)
#                 break
#     n = -1
#     return(n)
#     print(n)

#
# # Best Solution!!!!
# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             print(arr[:i])
#             print(arr[i+1:])
#             return i
#     print(arr[:i])
#     print(arr[i+1:])
#     return -1



# arr = range(-100,-1:
# for i in arr:
#     print(i)
# arr = range(-100,-1)
# n = find_even_index(arr)
# print(n)


# arr = [1, 2, 3, 4, 3, 2, 1]
# sum_left = 0
# pos_left = 0
# for i in reversed(arr):
#     sum_left+=i
#     pos_left = arr.index(i)
#     print(sum_left)
#     print(pos_left)



# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
# the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would
# make this happen, return -1.
#
# For example:
#
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index
# ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
#
# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index
# ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
#
# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.
#
# Note: Please remember that in most programming/scripting languages the index of an array starts at 0.
#
# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.
#
# Output:
# The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.
#
# Note:
# If you are given an array with multiple answers, return the lowest correct index.






