# Exercise: Are they the "same"?
array1 = [10000001, 100000000]
array2 = [100000000000000, 10000000000000000]

# if array1 == [] or array2 == []:
#     result = False
# elif len(array1) != len (array2):
#     result = False
# else:
#     a = sorted(array1)
#     b = sorted(array2)
#     for i in range (len(a)):
#         num = a[i]
#         if a[i]*a[i] == b[i]:
#             result = True
#         else:
#             result = False
#             break
# print(result)



def comp(array1, array2):
    if (array1 == [] and array2 != []) or (array1 != [] and array2 == []):
        result = False
    elif  array1 == [] and array2 == []:
        result = True
    elif len(array1) != len (array2):
        result = False
    else:
        a = sorted(array1)
        b = sorted(array2)
        for i in range (len(a)):
            num = a[i]
            if a[i]*a[i] == b[i]:
                result = True
            else:
                result = False
                break
    return(result)

result = comp(array1, array2)
print(result)


# Best Solutions

# - 1 Best Solutions
# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False

# - 2 Best Solutions
# def comp(a1, a2):
#     return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

# - 3 Best Solutions
# def comp(a1, a2):
#     return None not in (a1, a2) and all(x**2 == y for x, y in zip(sorted(a1), sorted(a2)))  --> zip function??

# - 4 Best Solutions
# from collections import Counter as c   # I didn't understand this passage
# def comp(a1, a2):
#     return a1 != None and a2 != None and c(a2) == c( elt**2 for elt in a1 )

# - 5 Best Solutions  --> with enumerate
# def comp(l1, l2):
#     if l1 == None or l2 == None: return False
#     l2.sort()
#     return all(x == l2[i] for i, x in enumerate(v * v for v in sorted(l1)))  --> all function??

# - 6 Best Solutions  --> with map(lambda
# def comp(array1, array2):
# # your code
# if array1 == None or array2 == None:
#     return False
# array1.sort()
# array2.sort()
# return map(lambda i:i*i, array1) == array2


# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
#
# Examples
# Valid arrays
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# Invalid arrays
# If we change the first number to something else, comp may not return true anymore:
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 132 is not the square of any number of a.
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 36100 is not the square of any number of a.
#
# Remarks
# a or b might be [] (all languages except R, Shell). a or b might be nil or null or None or nothing (except in Haskell, Elixir, C++, Rust, R, Shell, PureScript).
#
# If a or b are nil (or null or None), the problem doesn't make sense so return false.
#
# If a or b are empty then the result is self-evident.
#
#     a or b are empty or not empty lists.