# codeWar Create Phone Number

def create_phone_number(n):
    # print(tuple(n))
    final_phone_number = '('
    for prefix in  n[:3]:
        final_phone_number += str(prefix)
    final_phone_number += ') '
    # print(final_phone_number)
    for first_part in n[3:6]:
        final_phone_number += str(first_part)
    final_phone_number += '-'
    # print(final_phone_number)
    for second_part in n[6:10]:
        final_phone_number += str(second_part)
    print(final_phone_number)
    # return final_phone_number

# def create_phone_number(n):
#     print(*n)
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(tuple(n))






create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])== "(123) 456-7890")
# Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
# Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
# Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
# Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(
# 000) 000-0000")

# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

