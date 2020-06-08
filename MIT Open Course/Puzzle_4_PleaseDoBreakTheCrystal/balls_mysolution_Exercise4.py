# Michele: Doesn't exit Exercise 4, I created it to implement the algorithm changing the new floor to drop the ball
# when and if we reach the step where we increment the Floor of 1 unit, whe we reach this step we can save some drops
# if we don't increment the next drop of 1 unit but if we calculate the median Floor in our currently interval and
# we drop the ball at this Floor.

# It looks a good work!!!

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
    remainBalls = d
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
            diffFlor = endFloor - startFloor
            if i != (d-1) or (i == (d-1) and remainBalls == 1) or (i == (d-1) and diffFlor <= 1):

                #Make sure you aren't higher than the highest floor
                if Floor > n:
                    floorNoBreak[i] -= 1
                    break
                print('%'*20)
                print(floorNoBreak)
                print('Drop ball', breakBalls+1, 'from Floor', Floor)
                print('The intervals of floors under consideration is from floor: ', startFloor, 'to floor: ', endFloor)
                print('Total number of balls we remain', remainBalls)
                yes = input('Did the ball break (yes/no)?:')
                numDrops += 1
                if yes == 'yes':
                    floorNoBreak[i] -= 1
                    breakBalls += 1
                    remainBalls -= 1
                    endFloor = Floor - 1
                    break
                elif yes == 'no' and Floor == startFloor == endFloor:
                    break
                else:
                    startFloor = Floor + 1
            else:
                # I change interval only in the last i, with remain ball > 1 and
                # if the difference between startfloor and endfloor >1
                medianFloor = ((endFloor - startFloor)+1) // 2
                floorNoBreak[i] += medianFloor
                Floor = convertToDecimal(r, d, floorNoBreak)
                print('$'*20)
                print(floorNoBreak)
                print('Drop ball', breakBalls+1, 'from Floor', Floor)
                print('The intervals of floors under consideration is from floor: ', startFloor, 'to floor: ', endFloor)
                print('Total number of balls we remain', remainBalls)
                yes = input('Did the ball break (yes/no)?:')
                numDrops += 1
                if yes == 'yes':
                    floorNoBreak[i] -= (1 + medianFloor)
                    breakBalls += 1
                    remainBalls -= 1
                    endFloor = Floor - 1
                else:
                    startFloor = Floor + 1


    hardness = convertToDecimal(r, d, floorNoBreak)
    print('Hardness coefficient is', hardness)
    print('Total number of drops is', numDrops)
    print('Total number of balls broken is', breakBalls)
    print('Total number of balls we remain', remainBalls)

    return


def convertToDecimal(r, d, rep):
    number = 0
    for i in range(d-1):
        number = (number + rep[i]) * r

    number += rep[d-1]
    print('='*20)
    print(number)

    return number


howHardIsTheCrystal(600, 4)