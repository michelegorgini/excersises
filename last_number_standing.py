# Zombie Apocalypse: the Last Number Standing

# Story: In the realm of numbers, the apocalypse has arrived. Hordes of zombie numbers have infiltrated and are
# ready to turn everything into undead. The properties of zombies are truly apocalyptic: they reproduce themselves
# unlimitedly and freely interact with each other. Anyone who equals them is doomed. Out of an infinite number of
# natural numbers, only a few remain. This world needs a hero who leads remaining numbers in hope for survival:
# The highest number to lead those who still remain.
#
# Briefing: There is a list of positive natural numbers. Find the largest number that cannot be represented as
# the sum of this numbers, given that each number can be added unlimited times. Return this number, either 0 if
# there are no such numbers, or -1 if there are an infinite number of them.
#
# Example:
#
# Let's say [3,4] are given numbers. Lets check each number one by one:
# 1 - (no solution) - good
# 2 - (no solution) - good
# 3 = 3 won't go
# 4 = 4 won't go
# 5 - (no solution) - good
# 6 = 3+3 won't go
# 7 = 3+4 won't go
# 8 = 4+4 won't go
# 9 = 3+3+3 won't go
# 10 = 3+3+4 won't go
# 11 = 3+4+4 won't go
# 13 = 3+3+3+4 won't go
# ...and so on. So 5 is the biggest 'good'. return 5

# base on the theory of Frobenius number --> problem when we have three or more elements

import math

def survivor(zombies):
    print(zombies[0],zombies[1])
    find_gcd = math.gcd(zombies[0],zombies[1])
    find_lcm = abs(zombies[0]*zombies[1]) // find_gcd
    print(find_gcd, find_lcm)
    #code
    return #result


# abs(a*b) // math.gcd(a, b)




survivor([7, 10])
# survivor([7, 11]) #, 59,"[7, 11]")
# survivor([1, 7, 15]) #, 0,"[1, 7, 15]")
# survivor([2, 10]) #, -1,"[2, 10]")
# survivor([687,829,998]) #,45664,"[687,829,998]")






