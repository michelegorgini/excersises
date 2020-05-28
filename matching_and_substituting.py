# code war Matching And Substituting

# I got lots of files beginning like this:
#
# Program title: Primes
# Author: Kern
# Corporation: Gold
# Phone: +1-503-555-0091
# Date: Tues April 9, 2005
# Version: 6.7
# Level: Alpha

# Here we will work with strings like the string data above and not with files.
#
# The function change(s, prog, version) given:
# s=data, prog="Ladder" , version="1.1" will return:
# "Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1"

# Rules:
# - The date should always be "2019-01-01".
# - The author should always be "g964".
# - Replace the current "Program Title" with the prog argument supplied to your function. Also remove "Title", so
#   in the example case "Program Title: Primes" becomes "Program: Ladder".
# - Remove the lines containing "Corporation" and "Level" completely.
# - Phone numbers and versions must be in valid formats.
#
# A valid version in the given string data is one or more digits followed by a dot, followed by one or more digits.
# So 0.6, 5.4, 14.275 and 1.99 are all valid, but versions like .6, 5, 14.2.7 and 1.9.9 are invalid.
# A valid phone format is +1-xxx-xxx-xxxx, where each x is a digit:
# - If the phone or version format is not valid, return "ERROR: VERSION or PHONE".
# - If the version format is valid and the version is anything other than 2.0, replace it with the version parameter
#   supplied to your function. If it’s 2.0, don’t modify it.
# - If the phone number is valid, replace it with "+1-503-555-0090".
#
# Note:
# You can see other examples in the "Sample tests"

# My Solution


def change(s, prog, version):
    print(prog)
    print(version)
    result = ''
    my_list_order = ['Program', 'Author', 'Phone', 'Date', 'Version']   # To put in correct order the result
    print(s)
    my_dict = dict(element.split(': ') for element in s.split('\n'))
    my_dict['Program'] = my_dict.pop('Program title')
    my_dict['Program'] = prog
    my_dict['Author'] = 'g964'
    my_dict['Date'] = '2019-01-01'
    del my_dict['Corporation']
    del my_dict['Level']

    if my_dict['Version'] != '2.0':
        if validversion(my_dict['Version']):
            my_dict['Version'] = version
        else:
            # return 'ERROR: VERSION or PHONE'
            print('ERROR: VERSION or PHONE')

    if validphone(my_dict['Phone']):
        my_dict['Phone'] = '+1-503-555-0090'
        tuple_my_dict = tuple(my_dict.items())
        for key_output in my_list_order:
            for elem in tuple_my_dict:
                key, description = elem
                if key_output == key:
                    result += key_output + ': ' + description + ' '
        result = result[:-1]
        # return result
        print(result)
    else:
        # return 'ERROR: VERSION or PHONE'
        print('ERROR: VERSION or PHONE')
        print("{phone "*20)


def validphone(phone_number):
    if len(phone_number) != 15:
        return False
    for i in range(15):
        if i == 0:
            if phone_number[0] != '+':
                return False
        elif i == 1:
            if phone_number[1] != '1':
                return False
        elif i in [2, 6, 10]:
            if phone_number[i] != '-':
                return False
        elif not phone_number[i].isnumeric():
            return False
    return True


def validversion(version_number):
    count_dot = 0
    for i in range(len(version_number)):
        if i == 0:
            print(version_number[0])
            if not version_number[i].isnumeric():   # It worked on line 89, here no. Why?
            # if not version_number[0] and version_number[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # if version_number[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                return False
                # print("False why "*20)
        elif version_number[i] == '.':
            count_dot += 1
    if count_dot == 1:
        return True
    else:
        return False





# @Test.describe('change')
# def ch()
#     #@Test.it('Basic tests 1')
#     def ch_bt1():
s1 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0091\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'
# s11 = 'Program title: Hammer\nAuthor: Tolkien\nCorporation: IB\nPhone: +1-503-555-0090\nDate: Tues March 29, 2017\nVersion: 2.0\nLevel: Release'
# s12 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-009\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'
# s22 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0097\nDate: Tues April 9, 2005\nVersion: 0.2\nLevel: Alpha'

change(s1, 'Ladder', '1.1')
# change(s11, 'Balance', '1.5.6')
# change(s12, 'Ladder', '1.1')
# change(s22, 'N', 6)

# Test.assert_equals(change(s1, 'Ldder', '1.1'), 'Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1')
# Test.assert_equals(change(s11, 'Balance', '1.5.6'), 'Program: Balance Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 2.0')
# Test.assert_equals(change(s12, 'Ladder', '1.1'), 'ERROR: VERSION or PHONE')

