# Michele: I was not able to find solution to Exercise1, I tried to add code after if Floor > n: But it' s wrong the
# only possible solution is Teacher's solution that I copied :(

#Programming for the Puzzled -- Srini Devadas
#Please Do Break the Crystal
#This is an interactive procedure that given n floors and d balls determines
#what floors to drop the balls from to minimize the worst-case number of
#drops required to determine the hardness coefficient of the crystal.
#The hardness coefficient will range from 0 (breaks at Floor 1) or n (does not
#break at n.
def howHardIsTheCrystal(n, d):
    #Initialize startFloor = 0 and endFloor = n
    startFloor = 0
    endFloor = n

    #First determine the radix r
    r = 1
    while (r**d <= n):
        r = r + 1
    print('Radix chosen is', r)


    #See if you can reduce d -> Exercise 1 Solution
    newd = d
    while (r**(newd-1) > n):
        newd -= 1
    if newd < d:
        print('Using only', newd, 'balls')
        d = newd


    breakBalls = 0
    numDrops = 0
    floorNoBreak = [0] * d
    for i in range(d):
        #Begin phase i
        for j in range(r-1):
            #increment ith digit of representation
            floorNoBreak[i] += 1
            print(j)
            print(floorNoBreak)
            Floor = convertToDecimal(r, d, floorNoBreak)
            #Make sure you aren't higher than the highest floor
            if Floor > n:
                floorNoBreak[i] -= 1
                break
            print('$'*20)
            print(floorNoBreak)
            print ('Drop ball', i+1, 'from Floor', Floor)
            print('The intervals of floors under consideration is from floor: ', startFloor, 'to floor: ', endFloor)
            yes = input('Did the ball break (yes/no)?:')
            numDrops += 1
            if yes == 'yes':
                floorNoBreak[i] -= 1
                breakBalls += 1
                endFloor = Floor - 1
                break
            else:
                startFloor = Floor + 1


    hardness = convertToDecimal(r, d, floorNoBreak)
    print('Hardness coefficient is', hardness)
    print('Total number of drops is', numDrops)
    print('Total number of balls broken is', breakBalls)


    return

def convertToDecimal(r, d, rep):
    number = 0
    for i in range(d-1):
        number = (number + rep[i]) * r
        #print(number)
    number += rep[d-1]
    print('='*20)
    print(number)

    return number


howHardIsTheCrystal(128, 4)