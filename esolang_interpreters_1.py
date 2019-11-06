# Codewar

## My solution

def my_first_interpreter(code):
    # Make your esolang interpreter here
    count_code = []
    number_plus = 0
    number_point = 0
    for plus in code:   # this loop creates a list of tuple with (number consecutive '+' , number consecutive '.' )
        if plus == '+' and number_point == 0:    # How create a comprehension with this loop.  Ask to Jonne????
            number_plus += 1
        elif plus == '.':
            number_point += 1
        elif plus == '+' and number_point != 0:
            count_code.append([number_plus, number_point])
            number_plus = 1
            number_point = 0
    count_code.append((number_plus, number_point))   # Checking count_code I can understand the logic (because if find
    print(count_code)                                # number_point > 1 --> double letter to print
    my_result = ''
    count_dec_ascii = 0
    for dec_ascii, number_print_letter in count_code:
        count_dec_ascii += dec_ascii
        if number_print_letter == 1:
            my_result += chr(count_dec_ascii % 256)
        else:
            for print_letter in range(0, number_print_letter):  # for loop to find double letter to print
                my_result+= chr(count_dec_ascii % 256)
    print (my_result)
    return my_result





# # One best solution that I want to understand
# def my_first_interpreter(code):
#     for e in code:
#         if e in '.+':
#             print(e)
#     cell, out = 0, ''
#     for c in [e for e in code if e in "'.','+'"]:  # in '.+'  works? I thought in "'.','+'"
#         cell, out = (0 if cell == 255 else cell + 1, out) if c == '+' else (cell, out + chr(cell))
#     print(out)
#     return out


# def my_first_interpreter2(code):
#     print()
#     ret = [s.count('+') for s in code.split('.')]
#     print(ret)
#     for i in range(1, len(ret)):
#         rr = ret[:i]
#         print(rr)
#         r = sum(ret[:i])
#         print(r)
#         m = r % 256
#         print(m)
#         pass
#     return ''.join(chr(sum(ret[:i]) % 256) for i in range(1, len(ret)))




# solution2 = my_first_interpreter2
solution = my_first_interpreter
code = (solution('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.'), 'Hello, World!')

# code = (solution2('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.'), 'Hello, World!')

code = (solution('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.'
                '+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#
# print("space" + chr(45))



# # I LIKE this solution
# def normalize(x):
#     return x % 256
#
# def generator(code):
#     current = 0
#     for op in code:
#         if op == "+":
#             current += 1
#         elif op == ".":
#             yield current
#
# def my_first_interpreter(code):
#     return "".join(map(chr, map(normalize, generator(code))))
