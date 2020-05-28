# Zombie Apocalypse: the Last Number Standing

import math

def survivor(zombies):
    count_zombi = len(zombies)
    min_zombi = min(zombies)
    sum_zombies = 0
    # print(count_zombi)
    # print(min_zombi)
    if min_zombi == 1:
        return 0
    look_for_multiples = True
    for zombie in zombies:
        sum_zombies = sum_zombies + zombie
        if zombie % min_zombi != 0:
            look_for_multiples = False
    if look_for_multiples == True:
        return -1
    first_zombie = zombies[0]
    second_zombie = zombies[1]
    if count_zombi == 2:
        lcm_2zombies = find_lcm(first_zombie,second_zombie)
        print(lcm_2zombies - sum_zombies)
        return lcm_2zombies - sum_zombies
    else:
        lcm_more_zombies = find_lcm(first_zombie,second_zombie)
        print(lcm_more_zombies)
        print('---')
        for i in range(2, count_zombi):
            lcm_more_zombies += lcm_more_zombies + find_lcm(zombies[1], zombies[i])
        print(lcm_more_zombies - sum_zombies)
        return lcm_more_zombies - sum_zombies



def find_lcm(num1, num2):
    if(num1>num2):
        numerator = num1
        denominator = num2
    else:
        numerator = num2
        denominator = num1
    resto = numerator % denominator
    while(resto != 0):
        numerator = denominator
        denominator = resto
        resto = numerator % denominator
    gcd = denominator
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm




#
# print(survivor([7, 11]) == 59)
# print(survivor([1, 7, 15]) == 0)
# print(survivor([2, 10])== -1)
# print(survivor([687,829,998])==45664)

print(survivor([687,829])==568007)
#print(survivor([687,998])==683941)
#print(survivor([829,998])==825515)

