##something new here

# # 5 Exercise - Killer Garage Door
#
# def controller(events):
#     print(events)
#     result =''
#     #temp = '0'
#     last = ''
#     if events[:1] == '.':
#         result ='0'
#         temp = 0
#     elif events[:1] == '':
#         result =''
#     else:
#         result ='1'
#         temp = 1
#         last = '+'
#     event1 = events[1:]
#     for i in event1:
#         if i == '.' and (temp == 0 or temp == 5):
#             result +=str(temp)
#             #print(result)
#         elif i == '.' and (temp > 0 and temp < 5) and last == '+':
#             result+= str(temp+1)
#             temp = temp+1
#         elif i == '.' and (temp > 0 and temp < 5) and last == '-':
#             result+= str(temp-1)
#             temp = temp-1
#         elif i == '.' and (temp > 0 and temp < 5) and (last == '+=' or last == '-='):
#             result+= str(temp)
#             temp = temp
#         elif i == 'P' and temp == 0:
#             result += '1'
#             temp = 1
#             last = '+'
#         elif i == 'P' and temp == 5:
#             result += str(temp-1)
#             temp = temp-1
#             last = '-'
#         elif i == 'P' and (temp > 0 and temp < 5) and last == '+':
#             result+= str(temp)
#             last = '+='
#             temp = temp
#         elif i == 'P' and  (temp > 0 and temp < 5) and (last == '-' ):
#             result+= str(temp)
#             last = '-='
#             temp = temp
#         elif i == 'P' and  (temp > 0 and temp < 5) and (last == '+='):
#             result+= str(temp+1)
#             last = '+'
#             temp = temp+1
#         elif i == 'P' and  (temp > 0 and temp < 5) and (last == '-='):
#             result+= str(temp-1)
#             last = '-'
#             temp = temp-1
#         elif i == 'O' and (temp > 0 and temp < 5) and (last == '+' or last == '+='):
#             result+= str(temp-1)
#             last = '-'
#             temp = temp-1
#         elif i == 'O' and (temp > 0 and temp < 5) and (last == '-' or last == '-='):
#             result+= str(temp+1)
#             last = '+'
#             temp = temp+1
#     return(result)
#     print(result)
#
#
#
# # P......P.O....
# # 12345554342345
# ##12345554345555
# events = 'P......P.O....'
# result = controller(events)
# print(result)

events = '.......P.O....'
state = 0
movement = False
direction = True
output = ''
for event in events:
    if event is 'P':
        movement = not movement
    if event is 'O':
        direction = not direction

    tmp = ((-1, 1)[direction] * movement)
    print(tmp)
    state = state + (-1, 1)[direction] * movement# it means direction (-1,1)and movement (0,1). I why movement is not between squares
    print(direction)
    print("]"*20)
    if state in (0, 5):
        direction = not state#state # if state is not 0 or 5 --> direction = False??
        pippo = not state
        print(direction)
        print('='*20)
        movement  = False # (0 and 5 means "stop" --> movement = False- ok and change direction when state is not 0 or 5
    output += str(state)
#print(output)
#print(events)

#print((0,2,5)[1])
# #Best Solution
# def controller(events):
#     state = 0
#     movement = False
#     direction = True
#     output = ''
#     for event in events:
#         if event is 'P':
#             movement = not movement
#         if event is 'O':
#             direction = not direction
#         state = state + (-1, 1)[direction] * movement
#         if state in (0, 5):
#             direction = not state
#             movement  = False
#         output += str(state)
#     return output
#
# events = 'P......P.O....'
# result = controller(events)
# print(result)

# Situation
# You have been hired by a company making electric garage doors. Accidents with the present product line have resulted
# in numerous damaged cars, broken limbs and several killed pets. Your mission is to write a safer version of their
# controller software.
#
# Specification
# We always start with a closed door. The remote control has exactly one button, with the following behaviour.
#
# If the door is closed, a push starts opening the door, and vice-versa
# It takes 5 seconds for the door to open or close completely
# While the door is moving, one push pauses movement, another push resumes movement in the same direction
# In order to make the door safer, it has been equiped with resistance-based obstacle detection. When the door detects
# an obstacle, it must immediately reverse the direction of movement.
#
# Input
# A string where each character represents one second, with the following possible values.
#
# '.' No event
# 'P' Button has been pressed
# 'O' Obstacle has been detected (supersedes P)
# As an example, '..P....' means that nothing happens for two seconds, then the button is pressed, then no further
# events.
#
# Output
# A string where each character represents one second and indicates the position of the door (0 if fully closed and 5
# fully open). The door starts moving immediately, hence its position changes at the same second as the event.
#
# Example
# ..P...O..... as input should yield 001234321000 as output


