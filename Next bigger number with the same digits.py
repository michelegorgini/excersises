#Exercise - Next bigger number with the same digits

#def next_bigger(n):
#your code here

# n = 2071
# print(n)
# s = str(n)
# ListDigit_right = []
# bigger = n
# Ind_FromRight = next(( x+1) for x,v in enumerate(s[::-1]) if v > s[x+1])
# print(Ind_FromRight)
# ind_Fromleft = ((len(s)-1)- Ind_FromRight)
# new_s = s[ind_Fromleft:]
# print(s[ind_Fromleft])
# print(new_s)
# Next_DigitBig = next((v) for x,v in enumerate(new_s[::-1]) if v > new_s[x+1] and v > s[ind_Fromleft])
# for i in new_s:
#     ListDigit_right.append(i)
# ListDigit_right.remove(Next_DigitBig)
# ListDigit_right = sorted(ListDigit_right)
# Next_DigitBig +=''.join(map(str, ListDigit_right))
# num = int(s[:(ind_Fromleft)] + Next_DigitBig )
# if (num > bigger):
#     bigger = num
# else:
#     bigger = -1
# print(bigger)



# def next_bigger(n):
#     print(n)
#     s = str(n)
#     ListDigit_right = []
#     bigger = n
#     Ind_FromRight = next(( x+1) for x,v in enumerate(s[::-1]) if v > s[x+1])
#     ind_Fromleft = ((len(s)-1)- Ind_FromRight)
#     new_s = s[ind_Fromleft:]
#     Next_DigitBig = next((v) for x,v in enumerate(new_s[::-1]) if v > new_s[x+1] and v > s[ind_Fromleft])
#     for i in new_s:
#         ListDigit_right.append(i)
#     ListDigit_right.remove(Next_DigitBig)
#     ListDigit_right = sorted(ListDigit_right)
#     Next_DigitBig +=''.join(map(str, ListDigit_right))
#     num = int(s[:(ind_Fromleft)] + Next_DigitBig )
#     if (num > bigger):
#         bigger = num
#     else:
#         bigger = -1
#     return(bigger)

# 59884848459853
# 59884848485953
# 59884848483559
# 59884848485953

# 7385661
# It should work for random inputs too: 7386561 should equal 7386156



# n = 12
# def next_bigger(n):
#     print(n)
#     s = str(n)
#     len_s = len(s)
#     ListBigger = []
#     bigger = n
#     for i in range(len(s)):
#         removed = s[:i] + s[i+1:]
#         for j in range(len(removed)+1):
#             num = int(removed[:j] + s[i] + removed[j:])
#             if (num > bigger):
#                 ListBigger.append(num)
#     if ListBigger == []:
#         bigger = -1
#     else:
#         tmp_bigger = min(ListBigger)
#     str_bigger = str(tmp_bigger)
#     print(str_bigger)
#     print("/"*20)
#     for i in range(len(s)):
#         if s[i] != str_bigger[i]:
#             Difference = str_bigger[i:]
#             break
#         else:
#             continue
#     if (tmp_bigger - n) > 9:
#         lastDigit = ''.join(sorted(Difference[1:]))
#         bigger = int(str_bigger[:i] + lastDigit)
#     else:
#         bigger = tmp_bigger
#     return(bigger)
#
# result =(next_bigger(n))
# print(result)



n = 9
print(n)
s = str(n)
len_s = len(s)
ListBigger = []
bigger = n
for i in range(len(s)):
    removed = s[:i] + s[i+1:]
    for j in range(len(removed)+1):
        num = int(removed[:j] + s[i] + removed[j:])
        if (num > bigger):
            ListBigger.append(num)
if ListBigger == []:
    bigger = -1
else:
    tmp_bigger = min(ListBigger)
    str_bigger = str(tmp_bigger)
    print(str_bigger)
    print("/"*20)
    for i in range(len(s)):
        if s[i] != str_bigger[i]:
            Difference = str_bigger[i:]
            break
        else:
            continue
    lastDigit = ''.join(sorted(Difference[1:]))
    print(lastDigit)
    bigger = int(str_bigger[:i+1] + lastDigit)
print(bigger)

print()
# 2175057886
# 2175058768
# 2175058678

#2175058768 should equal 2175058678













# You have to create a function that takes a positive integer number and returns the next bigger number formed by
# the same digits:
#
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# If no bigger number can be composed using those digits, return -1:
#
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1