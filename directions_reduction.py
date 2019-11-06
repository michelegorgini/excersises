# codewar
#

# def dirReduc(arr):
#     print(arr)
#     save_walk_dict = {"NORTH": "SOUTH",
#                       "SOUTH": "NORTH",
#                       "EAST": "WEST",
#                       "WEST": "EAST"}
#     reduction = []
#     j = 1
#     for ind, val in enumerate(arr):
#         # print(len(arr))
#         # print("+"*20)
#         # print(j)
#         # print()
#         try:
#             if save_walk_dict[val] != arr[j]:
#                 j += 1
#                 reduction.append(val)
#             else:
#                 for num in range(j+1, len(arr)):
#                     reduction.append(arr[num])
#                 # print(reduction)
#                 # print("="*20)
#                 try:
#                     dirReduc(reduction)
#                 except IndexError:
#                     print(reduction)
#                     print(">"*20)
#                     return reduction
#                     break
#         except IndexError:
#             reduction.append(val)
#             print("*"*20)
#             print(reduction)
#             print("*"*20)
#             return reduction
#             break


def dirReduc(arr):
    print(arr)
    print("Start")
    save_walk_dict = {"NORTH": "SOUTH",
                      "SOUTH": "NORTH",
                      "EAST": "WEST",
                      "WEST": "EAST"}
    index_end = len(arr)
    reduction = []
    j = 1
    while len(arr):
        # pippo = save_walk_dict[arr[j-1]]
        # pluto = arr[j]
        if j < index_end:  # used to avoid index error
            if save_walk_dict[arr[j-1]] == arr[j]:   # test if value dictionary (for example element 1) == value
                for num in range(j+1, len(arr)):     #  next element (element2) . if they are equal I put in reduction
                    reduction.append(arr[num])       # list all the element starting from (element3) and I recall my
                arr = dirReduc(reduction)            # function
            else:
                reduction.append(arr[j-1])           # If they are not equal I put element 1 in reduction list and I
                j += 1                               # restart my loop
        else:
            reduction.append(arr[j-1])               # I append the last element
            # print(reduction)
            result = reduction
            return result                            # I debugged the program step by spep and when arrive at return
    print(reduction)                                 # result the program doesn't stop but re-start from line 59
    result = reduction                               # where I re-call my function
    return result




    # for i in range(len(arr) - 1):   # How is his logic (7?
    #     # opposite = save_walk_dict[arr[i+2]]
    #     # print(opposite)
    #     print(i)
    #     value = arr[i:i+2]
    #     print(value)
    # print()
    # print(value)



# b = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']
# arr = dirReduc(b)

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
arr = (dirReduc(a), ['WEST'])
#
# u = ["NORTH", "WEST", "SOUTH", "EAST"]
# arr = (dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
