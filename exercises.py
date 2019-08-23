
# # CodeWar Exercise

# codewar = You only need one - Beginner
# Description:
    # You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
    #
    # Array can contain numbers or strings. X can be either.
    #
    # Return true if the array contains the value, false if not.

# My Solution
# def check(seq, elem):
#     print(seq, elem)
#     checked = False
#     for x in seq:
#         if x == elem and not checked:
#             checked = True
#             break
#     print(checked)
#
# check ((66, "codewars", 11, "alex loves pushups"), "alex loves pushups")

# codewar = Meeting
# Description:
    # John has invited some friends. His list is:
    #
    # s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
    # Could you make a program that
    #
    # makes this string uppercase
    # gives it sorted in alphabetical order by last name.
    # When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.
    #
    # So the result of function meeting(s) will be:
    #
    # "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
    # It can happen that in two distinct families with the same family name two people have the same first name too.


# My Solution

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
# #def meeting(s):
# first_name = []
# family_name =[]
# capital_name=[]
# person =''
# result= ''
# for letter in s:
#     if letter != ';' and letter != ':':
#        person += letter
#     elif letter == ':':
#         first_name.append(person)
#         person = ''
#     elif  letter == ';' :
#         family_name.append(person)
#         person = ''
# family_name.append(person)
# for i in range (len(first_name)):
#     capital_name.append(family_name[i].upper()+', '+ first_name[i].upper())
# capital_ordered =sorted(capital_name)
# for people in capital_ordered:
#     result+='('
#     result+= people
#     result+=')'
# result += ''
# print(result)


# # Best Solution 1
# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
# s = s.upper()
# print(s)
# s = s.split(';') # If you split ':' s became a tuple --> I try but I was not able to do it
# print(s)
# array = []
# string = ""
# for i in s:
#     i = i.split(':')
#     string = '('+i[1]+', '+i[0]+')'
#     array.append(string)
# array.sort()
# output = ""
# for j in array:
#     output += j
# print(output)
#
# # # Best Solution 2 --> same logic Solution above
# # def meeting(s):
# #     names = s.upper().split(';')
# #     return ''.join(sorted('({1}, {0})'.format(*(n.split(':'))) for n in names))
#
# # # Best Solution 3 --> Not able to understand
# # meeting=lambda s:''.join(sorted('(%s, %s)'%tuple(e.split(':')[::-1])for e in s.upper().split(';')))

gridline = []
for i in range(7):
    gridline.append(0)
grids = []
for i in range(6):
    grids.append(list(gridline))

print('Current Grid:')
print(*grids, sep='\n')

for line in grids[5]:
    print(line)


# codewar = Greed is Good
