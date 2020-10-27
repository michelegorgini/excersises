from collections import Counter


originalList = (1,2,3,4,3,5,6,6,7,3,4,1,2,3,4,5,5,5,6,4,3,3,3)

ratings_count = Counter(originalList)

print(ratings_count)
print('='*20)

for rating in ratings_count:
    print("{}: {} occurences".format(rating, ratings_count[rating]))




# listToCheck = (1,4,9,15)
# zip(originalList, listToCheck)


# ((1,1),(2,4),(3,9),(4,15))

# ourList = (1,2,3,4)
# def square(number):
#     return number * number;
#
# resultList = map(lambda i: i*i, ourList)
# print(list(resultList))

# return map(lambda i:i*i, array1) == array2