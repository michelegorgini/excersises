#Programming for the Puzzled -- Srini Devadas
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal

caps0 = []
caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]
# In the array below I tried to built an array stating with 'F' cap having more intervals with 'B'. It's not possible.
# If the array starts with 'F' the intervals with 'F' always are >= 'B' .
caps3 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'B', 'B', 'B', 'F' ]
caps = ['H','F','B','H','B','F','B','B','B','F','H','F','F']

def pleaseConformOpt(caps):
    #Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    caps = caps + ['END']

    #Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            
            if caps[start] == 'F':
                forward += 1
            elif caps[start] == 'B':   # Exercise 3: Solution
                backward += 1
            start = i

    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    #print(intervals, forward, backward)
    for t in intervals:
        if t[2] == flip:
            #Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]:
                print ('Person at position', t[0], 'flip your caps!')
            else:
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')

# # Exercise 2: no 'H' in the caps
# def pleaseConformOnepass(caps):
#     if caps:
#         caps = caps + [caps[0]]
#         print(caps)
#         written = False
#         for i in range(1, len(caps)):
#             if caps[i] != caps[i-1]:
#                 if caps[i] != caps[0]:
#                     if caps[i] != caps[i+1]:
#                         print('Person at position', i, 'flip your caps!')
#                         written = True
#                     else:
#                         print('People in positions', i, end='')
#                         written = False
#                 elif not written:
#                     print(' through', i-1, 'flip your caps!')
#     else:
#         print('No caps!!!')

# Exercise 3 - I try to apply Exercise 3 (with 'H' in the caps) at this function
def pleaseConformOnepass(caps):
    if caps:
        caps = caps + [caps[0]]
        print(caps)
        written = False
        start = -1
        for i in range(1, len(caps)):
            if start < 0:
                if caps[i-1] != 'H':
                    start = i-1
            if caps[i] != caps[i-1] and start > -1 and caps[i] != 'H':
                    if caps[i] != caps[start]:
                        if caps[i] != caps[i+1]:
                            print('Person at position', i, 'flip your caps!')
                            written = True
                        else:
                            print('People in positions', i, end='')
                            written = False
                    elif not written and caps[i-1] != 'H':
                        print(' through', i-1, 'flip your caps!')
    else:
        print('No caps!!!')

                           
pleaseConformOpt(caps)
print('*'*20)
pleaseConformOnepass(caps)
