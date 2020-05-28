# codewar How many numbers III?

# We want to generate all the numbers of three digits where:
# -  the sum of their digits is equal to 10.
# - their digits are in increasing order (the numbers may have two or more equal contiguous digits)
#
# The numbers that fulfill the two above constraints are: 118, 127, 136, 145, 226, 235, 244, 334
#
# Make a function that receives two arguments:
# - the sum of digits value
# - the desired number of digits for the numbers
#
# The function should output an array with three values: [1,2,3]
# 1 - the total number of possible numbers
# 2 - the minimum number
# 3 - the maximum number
#
# The example given above should be:
# findAll(10, 3) => [8, "118", "334"]
#
# If we have only one possible number as a solution, it should output a result like the one below:
# findAll(27, 3) => [1, "999", "999"]
#
# If there are no possible numbers, the function should output the empty array.
# findAll(84, 4) => []

# The number of solutions climbs up when the number of digits increases.
# findAll(35, 6) => [123, '116999', '566666']


# def find_all(sum_dig, digs):
#     #print(sum_dig, digs)
#     max_range_number = 1
#     for i in range(digs):
#         max_range_number = max_range_number * 10
#     min_range_number = max_range_number//10
#     print(min_range_number)
#     min_number = max_range_number
#     max_number = min_range_number
#     total_number_ok = 0
#     # print(min_range_number, max_range_number)
#     my_list_result = []
#     print(len('100'))
#     # my_list_number = [number for number in range(int(min_range_number), int(max_range_number))
#     #                   for i, val in enumerate(str(number))
#     #                   if i < (len(str(number)) - 1)
#     #                   if int(str(number)[i+1]) >= int(val)]
#     # print(my_list_number)
#
#     for number in range(int(min_range_number), int(max_range_number)):
#         check = True
#         print(number)
#         for i, val in enumerate(str(number)):
#             if check:
#                 print(i, val)
#                 print()
#                 if i+1 < (len(str(number))) and int(str(number)[i+1]) >= int(val):
#                     print(int(str(number)[i+1]))
#                     print("len "*5)
#                     print(int(val))
#                     print()
#                 else:
#                     check = False
#             if check == True:
#                 print(number)
#                print("="*5)




# old Solution

# def find_all(sum_dig, digs):
#     #print(sum_dig, digs)
#     max_range_number = 1
#     for i in range(digs):
#         max_range_number = max_range_number * 10
#     min_range_number = max_range_number//10
#     print(min_range_number)
#     min_number = max_range_number
#     max_number = min_range_number
#     total_number_ok = 0
#     my_list_result = []
#     for number in range(min_range_number, max_range_number):
#     # for num in my_list_number:
#         old_digit = 0
#         count_sum_digit = 0
#         for digit in str(number):
#             if int(digit) >= old_digit:
#                 count_sum_digit += int(digit)
#                 old_digit = int(digit)
#             else:
#                 old_digit = 10
#                 count_sum_digit = 0
#         if count_sum_digit == sum_dig:
#             if number < min_number:
#                 min_number = number
#             if number > max_number:
#                 max_number = number
#             total_number_ok += 1
#     if total_number_ok:
#         my_list_result.append(total_number_ok)
#         my_list_result.append(min_number)
#         my_list_result.append(max_number)
#     # print(my_list_result)
#     return my_list_result



# # New Solution
#
# ##
#
# def find_all(sum_dig, number_of_digits):
#     digits = range(1, 10)
#     results = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9)]
#     possible_numbers = build_numbers(results, number_of_digits - 1, sum_dig)
#     if(possible_numbers):
#         print(len(possible_numbers), int(possible_numbers[0][0]), int(possible_numbers[-1][0]))
#         return [len(possible_numbers), int(possible_numbers[0][0]), int(possible_numbers[-1][0])]
#     return []
#
# def build_numbers(incoming_results, number_of_digits, sum_dig):
#     print(number_of_digits)
#     print("St "*2)
#     if number_of_digits > 0:
#         results = []
#         for result in incoming_results:
#             print(result)
#             print(int(result[0][-1]))
#             print("*"*10)
#             for digit in range(int(result[0][-1]), 10):
#                 if number_of_digits == 2 and int(result[0]) > 9:  # To avoid to do it when you enter in the method
#                     if digit == sum_dig - result[1]:              # the first time with number_of_digits == 2
#                         results.append((result[0] + str(digit), result[1] + digit))
#                 if number_of_digits == 1:
#                     result_check = (result[0] + str(digit), result[1] + digit)
#                     if result_check[1] == sum_dig:
#                         results.append(result_check)
#                 else:
#                     if result[1] + digit < sum_dig:        # enter in results only record with new sum < sum_dig
#                         results.append((result[0] + str(digit), result[1] + digit))
#             print(results)
#             print("restart "*2)
#         print(results)
#         print(number_of_digits)
#         print("R "*5)
#         print()
#         return build_numbers(results, number_of_digits - 1, sum_dig)
#
#     return incoming_results



# Best Solution

from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1, 10)), digs)
    for comb in combs:
        print(comb)
    target = [''.join(str (x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]


# print(find_all(10, 3))
print(find_all(10, 3) == [8, 118, 334])
# print(find_all(27, 3) == [1, 999, 999])
# print(find_all(84, 4) == [])
# print(find_all(35, 6) == [123, 116999, 566666])


