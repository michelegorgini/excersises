# codewar Phone Directory

# John keeps a backup of his old personal phone book as a text file. On each line of the file he can find the
# phone number (formated as +X-abc-def-ghij where X stands for one or two digits), the corresponding name
# between < and > and the address.
#
# Unfortunately everything is mixed, things are not always in the same order; parts of lines are cluttered with
# non-alpha-numeric characters (except inside phone number and name).
# Examples of John's phone book lines:
# - "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"
# - " 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
# - "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"
#
# Could you help John with a program that, given the lines of his phone book and a phone number returns a string
# for this number : "Phone => num, Name => name, Address => adress"
#
# Examples:
# s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
# phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
# It can happen that, for a few phone numbers, there are many people for a phone number -say nb- , then
# return : "Error => Too many people: nb"  or it can happen that the number nb is not in the phone book, in that case
# return: "Error => Not found: nb"
#
# You can see other examples in the test cases.  JavaScript random tests completed by @matt c
#
# Note
# Codewars stdout doesn't print part of a string when between < and >

# My  first solution

# def phone(strng, num):
#     print(num)
#     my_list = clean_string(strng)
#
#     my_final_phone = phone_clean_list(my_list)
#     my_final_name = name_clean_list(my_list)
#     my_final_address = address_clean_list(my_list)
#
#     result = ''
#     index_phone = 0
#     count = 0
#     for i in range(len(my_final_phone)):
#         if my_final_phone[i] == num:
#             count += 1
#             index_phone = i
#
#     if count == 0:
#         result += 'Error => Not found: ' + num
#         # print(result)
#         return result
#     elif count > 1:
#         result += 'Error => Too many people: ' + num
#         # print(result)
#         return result
#     elif count == 1:
#         result += 'Phone => ' + my_final_phone[index_phone] + ', Name => ' + my_final_name[index_phone] + \
#                   ', Address => ' + my_final_address[index_phone]
#         # print(result)
#         return result
#
#
# def clean_string(strng):
#     remove_characters = "/;?:$!*,"
#     insert_space = "_"
#     for character in remove_characters:
#         strng = strng.replace(character, '')
#     for char in insert_space:
#         strng = strng.replace(char, ' ')
#     strng = strng.replace('  ', ' ')
#     new_string = [element.lstrip() for element in strng.split('\n') if element]
#     return new_string
#
#
# def phone_clean_list(my_list):
#     my_phone = []
#     for elem in my_list:
#         n_phone = [fields.replace('+', '') for fields in elem.split() if fields[0] == '+']
#         my_phone.append(n_phone)
#     final_phone = []
#     phone_digit = ''
#     for pho in my_phone:
#         for n in pho:
#             phone_digit += n
#         final_phone.append(phone_digit)
#         phone_digit = ''
#     return final_phone
#
#
# def name_clean_list(my_list):
#     my_name = []
#     for elem in my_list:
#         n_name = [fields.replace('<', '').replace('>', '') for fields in elem.split()
#                   if fields[0] == '<' or fields[-1] == '>']
#         my_name.append(n_name)
#     final_name = []
#     nominative = ''
#     for name in my_name:
#         for n in name:
#             nominative += n + ' '
#         nominative = nominative[:-1]
#         final_name.append(nominative)
#         nominative = ''
#     return final_name
#
#
# def address_clean_list(my_list):
#     my_address = []
#     for elem in my_list:
#         n_address = [fields for fields in elem.split() if fields[0] != '<' and fields[0] != '+' and fields[-1] != '>']
#         my_address.append(n_address)
#     final_address = []
#     street = ''
#     for addr in my_address:
#         for ad in addr:
#             street += ad + ' '
#         street = street[:-1]
#         final_address.append(street)
#         street = ''
#     return final_address





# Improving first solutuion (I create immediately a list of string (before It was a list of list that
# I unpack in list of string)


def phone(strng, num):
    print(num)
    my_list = clean_string(strng)
    # print(my_list)
    my_final_phone = phone_clean_list(my_list)
    my_final_name = name_clean_list(my_list)
    my_final_address = address_clean_list(my_list)

    result = ''
    index_phone = 0
    count = 0
    for i in range(len(my_final_phone)):
        if my_final_phone[i] == num:
            count += 1
            index_phone = i

    if count == 0:
        result += 'Error => Not found: ' + num
        # print(result)
        return "Error => Not found: nb"
    elif count > 1:
        result += 'Error => Too many people: ' + num
        # print(result)
        return "Error => Too many people: nb"
    elif count == 1:
        result += 'Phone => ' + num + ', Name => ' + my_final_name[index_phone] + \
                  ', Address => ' + my_final_address[index_phone]
        # print(result)
        return result


def clean_string(strng):
    remove_characters = "/;?:$!*,"
    insert_space = "_"
    for character in remove_characters:
        strng = strng.replace(character, '')
    for char in insert_space:
        strng = strng.replace(char, ' ')
    strng = strng.replace('  ', ' ')
    new_string = [element.lstrip() for element in strng.split('\n') if element]
    return new_string


def phone_clean_list(my_list):
    my_phone = []
    for elem in my_list:
        n_phone = ''.join(fields.replace('+', '') for fields in elem.split() if fields[0] == '+')
        my_phone.append(n_phone)
    print(my_phone)
    return my_phone


def name_clean_list(my_list):
    my_name = []
    for elem in my_list:
        n_name = ' '.join(fields.replace('<', '').replace('>', '') for fields in elem.split()
                         if fields[0] == '<' or fields[-1] == '>')
        my_name.append(n_name)
    print(my_name)
    return my_name


def address_clean_list(my_list):
    my_address = []
    for elem in my_list:
        n_address = ' '.join(fields for fields in elem.split()
                            if fields[0] != '<' and fields[0] != '+' and fields[-1] != '>')
        my_address.append(n_address)
    print(my_address)
    return my_address


# # Best Practise Solution:
#
# from re import sub
#
# def phone(dir, num):
#     if dir.count("+" + num) == 0:
#         return "Error => Not found: " + num
#
#     if dir.count("+" + num) > 1:
#         return "Error => Too many people: " + num
#
#     for line in dir.splitlines():
#         if "+" + num in line:
#             name = sub(".*<(.*)>.*", "\g<1>", line)
#             line = sub("<" + name + ">|\+" + num, "", line)
#             address = " ".join(sub("[^a-zA-Z0-9\.-]", " ", line).split())
#             return "Phone => %s, Name => %s, Address => %s" % (num, name, address)


dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
      "+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
      "+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
      "+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
      "<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
      "<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
      "<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
      "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
      "<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
      "+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
      "<P Salinge> Main Street, +1-098-512-2222, Denve\n")

# def testing(actual, expected):
#     Test.assert_equals(actual, expected)


# phone(dr, "48-421-674-8974")
# phone(dr, "1-921-512-2222")
# phone(dr, "1-908-512-2222")
# phone(dr, "1-098-512-2222")
phone(dr, "5-555-555-5555")

# testing(phone(dr, "48-421-674-8974"), "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma")
# testing(phone(dr, "1-921-512-2222"), "Phone => 1-921-512-2222, Name => Wilfrid Stevens, Address => Wild Street AA-67209")
# testing(phone(dr, "1-908-512-2222"), "Phone => 1-908-512-2222, Name => Peter O'Brien, Address => High Street CC-47209")
# testing(phone(dr, "1-541-754-3010"), "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St.")
# testing(phone(dr, "1-121-504-8974"), "Phone => 1-121-504-8974, Name => Arthur Clarke, Address => San Antonio TT-45120")
# testing(phone(dr, "1-498-512-2222"), "Phone => 1-498-512-2222, Name => Bernard Deltheil, Address => Mount Av. Eldorado")
# testing(phone(dr, "1-098-512-2222"), "Error => Too many people: 1-098-512-2222")
# testing(phone(dr, "5-555-555-5555"), "Error => Not found: 5-555-555-5555")

