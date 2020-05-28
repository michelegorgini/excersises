# Codewar . Rail Fence Cipher: Encoding and Decoding

# Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode
# a string by placing each character successively in a diagonal along a set of "rails". First start off moving
# diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the
# top rail. Continue until you reach the end of the string. Each "rail" is then read left to right to derive
# the encoded string.
#
# For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:
#
# W       E       C       R       L       T       E
#   E   R   D   S   O   E   E   F   E   A   O   C
#     A       I       V       D       E       N
# The encoded string would be:
#
# WECRLTEERDSOEEFEAOCAIVDEN
# Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.
#
# Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns
# the DECODED string.
#
# For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an
# empty string.
#
# Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests
# that include punctuation. Don't filter out punctuation as they are a part of the string.


def encode_rail_fence_cipher(string, n):
    input = string
    # print(input, n)
    num_row = n
    num_col = len(input)
    cipher = build_race_fence_cipher(num_row, num_col)
    cipher_position = find_position_cipher(num_row, num_col)
    cipher_letter_position = letter_position_cipher(cipher_position, input)
    for letter, position in cipher_letter_position:
        cipher[position[0]][position[1]] = letter
    result = ''
    for row in range(num_row):
        for col in range(num_col):
            if cipher[row][col] != '':
                result += cipher[row][col]
    # print(result)
    return result


def decode_rail_fence_cipher(string, n):
    input = string
    # print(input, n)
    num_row = n
    num_col = len(input)
    cipher = build_race_fence_cipher(num_row, num_col)
    cipher_position = find_position_cipher(num_row, num_col)
    sorted_cipher_position = sorted(cipher_position, key=lambda elem: elem[0])
    cipher_letter_position = letter_position_cipher(sorted_cipher_position, input)
    for letter, position in cipher_letter_position:
        cipher[position[0]][position[1]] = letter
    result = ''
    for coordinate in cipher_position:
        if cipher[coordinate[0]][coordinate[1]] != '':
            result += cipher[coordinate[0]][coordinate[1]]
    # print(result)
    return result


def find_position_cipher(row, col):
    letter_steps = []
    j = 0
    while j < col:
        for i in range(0, row):
            if j < col:
                letter_steps.append((i, j))
                j += 1
        for i2 in reversed(range(1, row-1)):
            if j < col:
                letter_steps.append((i2, j))
                j += 1
    return letter_steps


def letter_position_cipher(cipher_coordinate, input):
    letter_position_steps = []
    for ind, coordinate in enumerate(cipher_coordinate):
        letter_position_steps.append((input[ind], (coordinate[0], coordinate[1])))
    return letter_position_steps


def build_race_fence_cipher(num_row, num_col):
    gridline = []
    for i in range(num_col):
        gridline.append('')
    grid = []
    for i in range(num_row):
        grid.append(list(gridline))
    return grid



# # best Solution --> really nice
#
# from itertools import chain
#
# def fencer(what, n):
#     print(what)
#     lst = [[] for _ in range(n)]
#     x,dx = 0,1
#     for c in what:
#         lst[x].append(c)
#         print(x,dx)
#         print(lst)
#         if x==n-1 and dx>0 or x==0 and dx<0: dx *= -1
#         x += dx
#     return chain.from_iterable(lst)
#
#
# def encode_rail_fence_cipher(s, n): return ''.join(fencer(s,n))
#
# def decode_rail_fence_cipher(s, n):
#     print(s)
#     lst = ['']*len(s)
#     print(len(s))
#     print(lst)
#     for c,i in zip(s, fencer(range(len(s)), n)):
#         lst[i] = c
#         print("="*5)
#         print(lst)
#     return ''.join(lst)







print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3) == "WECRLTEERDSOEEFEAOCAIVDEN")
print(encode_rail_fence_cipher("Hello, World!", 3) == "Hoo!el,Wrdl l")
print(encode_rail_fence_cipher("Hello, World!", 4) == "H !e,Wdloollr")
print(encode_rail_fence_cipher("", 3) == "")

print(decode_rail_fence_cipher("H !e,Wdloollr", 4)== "Hello, World!")
print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3) == "WEAREDISCOVEREDFLEEATONCE")
print(decode_rail_fence_cipher("", 3) == "")



