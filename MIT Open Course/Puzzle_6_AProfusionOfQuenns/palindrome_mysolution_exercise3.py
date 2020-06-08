# # Example of recursive function
# #Programming for the Puzzled -- Srini Devadas
# #A Profusion of Queens
#
#
# def iGcd(m, n):
#     """Calculate the Greatest Common Divisor of m and n.
#
#     Unless n==0, the result will have the same sign as n (so that when
#     n is divided by it, the result comes out positive).
#     """
#     while n > 0:
#         m, n = n, m % n
#         print(m,n)
#     print(m, 'result')
#     return m
#
#
# #This procedure recursively computes the gcd of two numbers
# def rGcd(m, n):
#     print (m, n)
#     if m % n == 0:
#         print(n, 'return n')
#         # when we get n, n became the result of previous call line 27 (gcd = rGcd(n, m % n) -> 14 = rGcd(28, 14) ->
#         # 14 = rGcd(658, 28) -> 14 = rGcd(1344, 658) ->
#         return n
#     else:
#         gcd = rGcd(n, m % n)
#         print(gcd, 'Result', n, 'm number', m % n, 'n number')
#         return gcd
#
# iGcd(2002, 1344)
#
# rGcd(2002, 1344)






# Exercecise 3

def isPalindrone(word, index, palindrome):
    word_noSpaces = word.upper().replace(" ", "")    # Every letters in uppercase and no spaces between words
    if word_noSpaces == palindrome:
        return print(word, 'is a palindrome, if you start from the end we get same word')
    else:
        if abs(index) <= len(word_noSpaces):
            palindrome += word_noSpaces[index]
            # print(palindrome, '***')
            isPalindrone(word, index-1, palindrome)
        else:
            return print(word, 'is NOT palindrome')


isPalindrone('I noti piedi dei pitoni', -1, '')  # index needs to start from -1


# Found better function on Interner

def isPalindromePrint(word):
    if isPalindromeInternet(word):
        print(word, ' IS a palindrome')
    else:
        print(word, ' IS NOT a palindrome')



def isPalindromeInternet (word):
    word = word.upper().replace(" ", "")    # Every letters in uppercase and no spaces between words
    lenght = len(word)
    # print(word[1:-1], lenght)
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return isPalindromeInternet(word[1:lenght-1])


isPalindromePrint('I noti piedi dei pitoni')



