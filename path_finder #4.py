# codewar Hey, Path Finder, where are you?

# no description Kata


def i_am_here(path):
    print(path)
    my_list_decimal = []
    for char in path:
        my_list_decimal.append(ord(char))
    print(my_list_decimal)
    for digit in my_list_decimal:
        print(digit)






a = 'R68R28rlrl31R'

# R68R28rlrl31R: None should equal [394, 120]

i_am_here(a) # == [394, 120]

# def where_are_you(path, result):
#     test.assert_equals(i_am_here(path), result, path)
#
# where_are_you('',       [0, 0])
# where_are_you('RLrl',   [0, 0])
# where_are_you('r5L2l4', [4, 3])






