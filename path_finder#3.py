# codewar Path Finder #3: the Alpinist

# You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal
# directions (i.e. North, East, South, West). Return minimal number of climb rounds to target location [N-1, N-1].
# Number of climb rounds between adjacent locations is defined as difference of location
# altitudes (ascending or descending).
#
# Location altitude is defined as an integer number (0-9).


# # The  logic old algorithm doesn't worh for g case
#
# def path_finder(maze):
#     num_row = 0
#     rows = maze.split('\n')
#     num_row =len(rows)
#     num_col = len(rows[0])
#     grid = build_maze(maze)
#     finish = [num_row-1, num_col-1, int(grid[num_row-1][num_col-1])]
#     # print(finish)
#     print(*grid, sep='\n')
#     open_set = set()
#     open_set.add((0, 0, int(grid[0][0]), 0))
#     checked_set = set()
#    # checked_set.add((0, 0, int(grid[0][0]), 0))
#     # print(open_set)
#     result = exist_path(open_set, checked_set, finish, grid)
#     return result
#
#
# def build_maze(maze):
#     board = []
#     for element in maze.split('\n'):
#         board.append(element)
#     return board
#
#
# def exist_path(open_set, checked_set, finish, grid):
#     move = [[0, -1], [-1, 0], [+1, 0], [0, +1]]
#     min_difference_level = 9
#     climb_rounds = 0
#     while open_set:
#         new_open_set = set()
#         tmp_new_open_set = set()
#         for coordinate in open_set:
#             x = coordinate[0]
#             y = coordinate[1]
#             # print("?"*20)
#             # print(open_set)
#             # print()
#             # print(climb_rounds)
#             # print("result "*20)
#             if x == finish[0] and y == finish[1]:
#                 print(climb_rounds)
#                 return climb_rounds
#             else:
#                 for dir in move:
#                     if (x + dir[0] >= 0 and  x + dir[0] < finish[0]+1) and \
#                             (y + dir[1] >= 0 and  y + dir[1] < finish[1]+1) and \
#                             (abs(int(grid[x + dir[0]][y + dir[1]]) - coordinate[2]) <= min_difference_level):
#                         min_difference_level = abs(int(grid[x + dir[0]][y + dir[1]]) - coordinate[2])
#                         # print(min_difference_level)
#                         # print("min_tmp "*20)
#                         if (x + dir[0], y + dir[1], int(grid[x + dir[0]][y + dir[1]])) not in checked_set:
#                             tmp_new_open_set.add((x + dir[0], y + dir[1], int(grid[x + dir[0]][y + dir[1]]), min_difference_level))
#                         else:
#                             min_difference_level = 9
#                 # print("tmp "*20)
#                 # print(tmp_new_open_set)
#                 # print(min_difference_level)
#                 for tmp_coordinate in tmp_new_open_set:
#                     if min_difference_level == tmp_coordinate[3]:
#                         new_open_set.add(tmp_coordinate)
#                         # checked_set.add(tmp_coordinate)
#                         tmp_new_open_set = set()
#
#             # print("="*20)
#             # print(new_open_set)
#             checked_set.add((coordinate[0], coordinate[1], coordinate[2]))
#             # print("ck "*20)
#             # print(checked_set)
#         climb_rounds += min_difference_level
#         min_difference_level = 9
#         open_set = new_open_set
#     return False


# try new Solution

# def path_finder(maze):
#     num_row = 0
#     rows = maze.split('\n')
#     num_row =len(rows)
#     num_col = len(rows[0])
#     grid = build_maze(maze)
#     finish = [num_row-1, num_col-1, int(grid[num_row-1][num_col-1])]
#     print(finish)
#     print(*grid, sep='\n')
#     open_set = set()
#     open_set.add((0, 0, int(grid[0][0]), 0))
#     checked_set = set()
#     result = short_level_path(open_set, checked_set, finish, grid)
#     return result
#
#
# def build_maze(maze):
#     board = []
#     for element in maze.split('\n'):
#         board.append(element)
#     return board
#
#
# def short_level_path(open_set, checked_set, finish, grid):
#     move = [[+1, 0], [0, +1]]
#     while open_set:
#         new_open_set = set()
#         tmp_new_open_set = set()
#         difference_level = 9
#         min_total_climb_rounds = 100000
#         for coordinate in open_set:
#             x = coordinate[0]
#             y = coordinate[1]
#             if x == finish[0] and y == finish[1]:
#                 print(coordinate[3])
#                 return coordinate[3]
#             else:
#                 for dir in move:
#                     level = coordinate[2]
#                     total_climb_rounds = coordinate[3]
#                     if (x + dir[0] >= 0 and  x + dir[0] < finish[0]+1) and \
#                             (y + dir[1] >= 0 and  y + dir[1] < finish[1]+1):  # and (abs(int(grid[x + dir[0]][y + dir[1]]) - coordinate[2]) <= difference_level):
#                         difference_level = abs(int(grid[x + dir[0]][y + dir[1]]) - level)
#                         total_climb_rounds += difference_level
#                         if total_climb_rounds < min_total_climb_rounds:
#                             min_total_climb_rounds = total_climb_rounds
#                         if (x + dir[0], y + dir[1]) not in checked_set:
#                             if (x + dir[0], y + dir[1]) not in checked_set:
#                             tmp_new_open_set.add((x + dir[0], y + dir[1], int(grid[x + dir[0]][y + dir[1]]), total_climb_rounds))
#             checked_set.add((coordinate[0], coordinate[1]))
#         check = True
#         for tmp_coordinate in tmp_new_open_set:
#             if min_total_climb_rounds != tmp_coordinate[3]:
#                 check = False
#         # if all([tmp_coordinate[3] for tmp_coordinate in tmp_new_open_set if min_total_climb_rounds == tmp_coordinate[3]]):
#         if check:
#             for tmp_coordinate in tmp_new_open_set:
#                 if min_total_climb_rounds == tmp_coordinate[3]:
#                     new_open_set.add(tmp_coordinate)
#         else:
#             for tmp_coordinate in tmp_new_open_set:
#                 if min_total_climb_rounds == tmp_coordinate[3]:
#                     prevent_total_climb = prevent_end_better_path(tmp_coordinate, finish, grid)
#                     if prevent_total_climb:
#                         for tmp2_coordinate in tmp_new_open_set:
#                             if prevent_total_climb >= tmp2_coordinate[3]:
#                                 new_open_set.add(tmp2_coordinate)
#                             # else:
#                             #     new_open_set.add(tmp_coordinate)
#         print(new_open_set)
#         open_set = new_open_set
#     return False
#
#
# def prevent_end_better_path(tmp_coordinate, finish, grid):
#     prevent_open_set = set()
#     prevent_open_set.add((tmp_coordinate))
#     prevent_checked_set = set()
#     prevent_move = [[+1, 0], [0, +1]]
#     while prevent_open_set:
#         prevent_new_open_set = set()
#         prevent_tmp_new_open_set = set()
#         prevent_difference_level = 9
#         prevent_min_total_climb_rounds = 100000
#         for prevent_coordinate in prevent_open_set:
#             if prevent_coordinate[0] == finish[0]:
#                 prevent_move = [[0, +1]]
#             elif prevent_coordinate[1] == finish[1]:
#                 prevent_move = [[+1, 0]]
#             x = prevent_coordinate[0]
#             y = prevent_coordinate[1]
#             prevent_total_climb_rounds = prevent_coordinate[3]
#             if x == finish[0] and y == finish[1]:
#                 # print(prevent_total_climb_rounds)
#                 return prevent_coordinate[3]
#             else:
#                 for dir in prevent_move:
#                     prevent_level = prevent_coordinate[2]
#                     prevent_total_climb_rounds = prevent_coordinate[3]
#                     if (x + dir[0] >= 0 and  x + dir[0] < finish[0]+1) and \
#                             (y + dir[1] >= 0 and  y + dir[1] < finish[1]+1):  # and (abs(int(grid[x + dir[0]][y + dir[1]]) - prevent_coordinate[2]) <= prevent_difference_level):
#                         prevent_difference_level = abs(int(grid[x + dir[0]][y + dir[1]]) - prevent_level)
#                         prevent_total_climb_rounds += prevent_difference_level
#                         if prevent_total_climb_rounds < prevent_min_total_climb_rounds:
#                             prevent_min_total_climb_rounds = prevent_total_climb_rounds
#                         if (x + dir[0], y + dir[1]) not in prevent_checked_set:
#                             prevent_tmp_new_open_set.add((x + dir[0], y + dir[1], int(grid[x + dir[0]][y + dir[1]]), prevent_total_climb_rounds))
#             prevent_checked_set.add((prevent_coordinate[0], prevent_coordinate[1]))
#         for prevent_tmp_coordinate in prevent_tmp_new_open_set:
#             if prevent_min_total_climb_rounds == prevent_tmp_coordinate[3]:
#                 prevent_new_open_set.add(prevent_tmp_coordinate)
#         prevent_open_set = prevent_new_open_set
#     return False


# try solution with open_set dictionary not set
#
#
# def path_finder(maze):
#     print(maze)
#     num_row = 0
#     rows = maze.split('\n')
#     num_row =len(rows)
#     num_col = len(rows[0])
#     grid = build_maze(maze)
#     finish = [num_row-1, num_col-1, int(grid[num_row-1][num_col-1])]
#     # print(finish)
#     # print(*grid, sep='\n')
#     key_value_grid = grid[0][0]
#     key_coordinate = "{'0,' + '0,' + key_value_grid: 0}"
#     dict_open_set = eval(key_coordinate)
#     checked_set = {}
#     result = short_level_path(dict_open_set, checked_set, finish, grid)
#     return result
#
#
# def build_maze(maze):
#     board = []
#     for element in maze.split('\n'):
#         board.append(element)
#     return board
#
#
# def short_level_path(dict_open_set, checked_set, finish, grid):
#     move = [[+1, 0], [0, +1], [-1, 0], [0, -1]]
#     while dict_open_set:
#         # print(dict_open_set)
#         # print("newS "*5)
#         new_open_set = {}
#         tmp_new_open_set = {}
#         difference_level = 9
#         min_total_climb_rounds = 100000
#         best_climb = 100000
#         for key in dict_open_set.keys():
#             coordinate = []
#             for val in key.split(','):
#                 coordinate.append(val)
#             x = int(coordinate[0])
#             y = int(coordinate[1])
#             if x == finish[0] and y == finish[1]:
#                 if dict_open_set.get(key) < best_climb:
#                     best_climb = dict_open_set.get(key)
#                 continue
#             else:
#                 for dir in move:
#                     level = int(coordinate[2])
#                     total_climb_rounds = dict_open_set.get(key)
#                     new_x = x + dir[0]
#                     new_y = y + dir[1]
#                     if (new_x >= 0 and  new_x < finish[0]+1) and \
#                             (new_y >= 0 and  new_y < finish[1]+1):
#                         new_level = int(grid[new_x][new_y])
#                         difference_level = abs(int(grid[new_x][new_y]) - level)
#                         total_climb_rounds += difference_level
#                         tmp_new_key = str(new_x) + ',' + str(new_y) + ',' + str(new_level)
#
#                         if tmp_new_key not in checked_set.keys():
#                             if tmp_new_key not in tmp_new_open_set.keys() or tmp_new_open_set[tmp_new_key] > total_climb_rounds:
#                                 tmp_new_open_set[tmp_new_key] = total_climb_rounds
#                                 if total_climb_rounds < min_total_climb_rounds:
#                                     min_total_climb_rounds = total_climb_rounds
#                         else:
#                             if checked_set.get(tmp_new_key) > total_climb_rounds:
#                                 del checked_set[tmp_new_key]
#                                 tmp_new_open_set[tmp_new_key] = total_climb_rounds
#                                 if total_climb_rounds < min_total_climb_rounds:
#                                     min_total_climb_rounds = total_climb_rounds
#
#                         # if tmp_new_key not in checked_set.keys():
#                         #     if tmp_new_key not in tmp_new_open_set.keys():
#                         #         tmp_new_open_set[tmp_new_key] = total_climb_rounds
#                         #         # if total_climb_rounds < min_total_climb_rounds:
#                         #         #     min_total_climb_rounds = total_climb_rounds
#                         #     else:
#                         #         if tmp_new_open_set[tmp_new_key] > total_climb_rounds:
#                         #             tmp_new_open_set[tmp_new_key] = total_climb_rounds
#                         #     if total_climb_rounds < min_total_climb_rounds:
#                         #         min_total_climb_rounds = total_climb_rounds
#                         # else:
#                         #     if checked_set.get(tmp_new_key) > total_climb_rounds:
#                         #         del checked_set[tmp_new_key]
#                         #         tmp_new_open_set[tmp_new_key] = total_climb_rounds
#                         #         if total_climb_rounds < min_total_climb_rounds:
#                         #             min_total_climb_rounds = total_climb_rounds
#             if key not in checked_set.keys():
#                 checked_set[key] = dict_open_set.get(key)
#         # check = True
#         # for tmp_value in tmp_new_open_set.values():
#         #     if min_total_climb_rounds != tmp_value:
#         #         check = False
#         # if check:
#         #     for tmp_items in tmp_new_open_set.items():
#         #         if min_total_climb_rounds == tmp_items[1]:
#         #             new_open_set[tmp_items[0]] = tmp_items[1]
#         # else:
#         tmp_check_first_min = True  # to get inside "prevent_end_better_path" only one time
#         for tmp_item in tmp_new_open_set.items():
#             if min_total_climb_rounds == tmp_item[1] and tmp_check_first_min:
#                 prevent_total_climb = prevent_end_better_path(tmp_item, finish, grid)
#                 if prevent_total_climb or prevent_total_climb == 0:
#                     tmp_check_first_min = False
#                     for tmp2_item in tmp_new_open_set.items():
#                         if prevent_total_climb >= tmp2_item[1]:
#                             # if tmp2_item[0] not in new_open_set.keys():
#                             new_open_set[tmp2_item[0]] = tmp2_item[1]
#                         else:
#                             # if tmp_item[0] not in new_open_set.keys():
#                             new_open_set[tmp_item[0]] = tmp_item[1]
#         dict_open_set = new_open_set
#     return best_climb
#
#
# def prevent_end_better_path(tmp_item, finish, grid):
#     prevent_dict_open_set = {}
#     prevent_dict_open_set[tmp_item[0]] = tmp_item[1]
#     # print(prevent_dict_open_set)
#     # print("prevent new dict "*5)
#     prevent_checked_set = {}
#     prevent_move = [[+1, 0], [0, +1]] #, [-1, 0], [0, -1]]
#     while prevent_dict_open_set:
#         prevent_new_open_set = {}
#         prevent_tmp_new_open_set = {}
#         prevent_difference_level = 9
#         prevent_min_total_climb_rounds = 100000
#         prevent_best_climb = 100000
#         for prevent_key in prevent_dict_open_set.keys():
#             prevent_coordinate = []
#             for val in prevent_key.split(','):
#                 prevent_coordinate.append(val)
#             # if prevent_coordinate[0] == finish[0]:
#             #     prevent_move = [[0, +1]]
#             # elif prevent_coordinate[1] == finish[1]:
#             #     prevent_move = [[+1, 0]]
#             prevent_x = int(prevent_coordinate[0])
#             prevent_y = int(prevent_coordinate[1])
#             if prevent_x == finish[0] and prevent_y == finish[1]:
#                 if prevent_dict_open_set.get(prevent_key) < prevent_best_climb:
#                     prevent_best_climb = prevent_dict_open_set.get(prevent_key)
#                 continue
#             else:
#                 for dir in prevent_move:
#                     prevent_total_climb_rounds = prevent_dict_open_set.get(prevent_key)
#                     prevent_new_x = prevent_x + dir[0]
#                     prevent_new_y = prevent_y + dir[1]
#                     prevent_level = int(prevent_coordinate[2])
#                     if (prevent_new_x >= 0 and  prevent_new_x < finish[0]+1) and \
#                             (prevent_new_y >= 0 and  prevent_new_y < finish[1]+1):
#                         prevent_new_level = int(grid[prevent_new_x][prevent_new_y])
#                         prevent_difference_level = abs(int(grid[prevent_new_x][prevent_new_y]) - prevent_level)
#                         prevent_total_climb_rounds += prevent_difference_level
#                         prevent_tmp_new_key = str(prevent_new_x) + ',' + str(prevent_new_y) + ',' + str(prevent_new_level)
#                         if prevent_tmp_new_key not in prevent_checked_set.keys():
#                             prevent_tmp_new_open_set[prevent_tmp_new_key] = prevent_total_climb_rounds
#                             if prevent_total_climb_rounds < prevent_min_total_climb_rounds:
#                                 prevent_min_total_climb_rounds = prevent_total_climb_rounds
#
#                         # if prevent_tmp_new_key not in prevent_checked_set.keys():
#                         #     if prevent_tmp_new_key not in prevent_tmp_new_open_set.keys():
#                         #         prevent_tmp_new_open_set[prevent_tmp_new_key] = prevent_total_climb_rounds
#                         #         if prevent_total_climb_rounds < prevent_min_total_climb_rounds:
#                         #             prevent_min_total_climb_rounds = prevent_total_climb_rounds
#                         #     else:
#                         #         if prevent_tmp_new_open_set[prevent_tmp_new_key] > prevent_total_climb_rounds:
#                         #             prevent_tmp_new_open_set[prevent_tmp_new_key] = prevent_total_climb_rounds
#                         #             if prevent_total_climb_rounds < prevent_min_total_climb_rounds:
#                         #                 prevent_min_total_climb_rounds = prevent_total_climb_rounds
#                         # else:
#                         #     if prevent_checked_set.get(prevent_tmp_new_key) > prevent_total_climb_rounds:
#                         #         del prevent_checked_set[prevent_tmp_new_key]
#                         #         prevent_tmp_new_open_set[prevent_tmp_new_key] = prevent_total_climb_rounds
#                         #         if prevent_total_climb_rounds < prevent_min_total_climb_rounds:
#                         #             prevent_min_total_climb_rounds = prevent_total_climb_rounds
#             if prevent_key not in prevent_checked_set.keys():
#                 prevent_checked_set[prevent_key] = prevent_dict_open_set.get(prevent_key)
#         for prevent_tmp_item in prevent_tmp_new_open_set.items():
#             if prevent_min_total_climb_rounds == prevent_tmp_item[1]:
#                 prevent_new_open_set[prevent_tmp_item[0]] = prevent_tmp_item[1]
#         prevent_dict_open_set = prevent_new_open_set
#     return prevent_best_climb



# Try new Solution for better performance

def path_finder(maze):
    num_row = 0
    rows = maze.split('\n')
    num_row =len(rows)
    num_col = len(rows[0])
    grid = build_maze(maze)
    finish = [num_row-1, num_col-1, int(grid[num_row-1][num_col-1])]
    # print(finish)
    # print(*grid, sep='\n')
    key_value_grid = grid[0][0]
    key_coordinate = "{'0,' + '0,' + key_value_grid: 0}"
    dict_open_set = eval(key_coordinate)
    checked_set = {}
    result = short_level_path(dict_open_set, checked_set, finish, grid)
    return result


def build_maze(maze):
    board = []
    for element in maze.split('\n'):
        board.append(element)
    return board


def short_level_path(dict_open_set, checked_set, finish, grid):
    move = [[+1, 0], [0, +1], [-1, 0], [0, -1]]
    best_climb = 100000
    while dict_open_set:
        print(dict_open_set)
        print("newS "*5)
        # new_open_set = {}
        tmp_new_open_set = {}
        difference_level = 9
        for key in dict_open_set.keys():
            x = int(key[0])
            y = int(key[2])
            z = int(key[4])
            if x == finish[0] and y == finish[1]:
                if dict_open_set.get(key) < best_climb:
                    best_climb = dict_open_set.get(key)
                continue
            else:
                for dir in move:
                    level = z
                    total_climb_rounds = dict_open_set.get(key)
                    new_x = x + dir[0]
                    new_y = y + dir[1]
                    if (new_x >= 0 and  new_x < finish[0]+1) and \
                            (new_y >= 0 and  new_y < finish[1]+1):
                        new_level = int(grid[new_x][new_y])
                        difference_level = abs(new_level - level)
                        total_climb_rounds += difference_level
                        tmp_new_key = str(new_x) + ',' + str(new_y) + ',' + str(new_level)
                        if tmp_new_key not in checked_set.keys():
                            if tmp_new_key not in tmp_new_open_set.keys() or tmp_new_open_set[tmp_new_key] > total_climb_rounds:
                                tmp_new_open_set[tmp_new_key] = total_climb_rounds
                        else:
                            if checked_set.get(tmp_new_key) > total_climb_rounds:
                                del checked_set[tmp_new_key]
                                tmp_new_open_set[tmp_new_key] = total_climb_rounds
            if key not in checked_set.keys():
                checked_set[key] = dict_open_set.get(key)
        print(checked_set)
        print("ck "*20)
        dict_open_set = tmp_new_open_set
    return best_climb

# print(path_finder(a) == 0)

# a = "\n".join([
#     "000",
#     "000",
#     "000"
# ])
#
# b = "\n".join([
#     "010",
#     "010",
#     "010"
# ])
#
# c = "\n".join([
#     "010",
#     "101",
#     "010"
# ])
#
d = "\n".join([
    "0707",
    "7070",
    "0707",
    "7070"
])
#
# e = "\n".join([
#     "700000",
#     "077770",
#     "077770",
#     "077770",
#     "077770",
#     "000007"
# ])
#
# f = "\n".join([
#     "777000",
#     "007000",
#     "007000",
#     "007000",
#     "007000",
#     "007777"
# ])
#
# g = "\n".join([
#     "000000",
#     "000000",
#     "000000",
#     "000010",
#     "000109",
#     "001010"
# ])
#
# m = "\n".join([
#     "636529252",
#     "018901723",
#     "447708405",
#     "406477007",
#     "346659191",
#     "283217162",
#     "396597351",
#     "016067917",
#     "388609202"
# ])
#
# n = "\n".join([
#     "6982812976203213476",
#     "4932252517000070578",
#     "0566866939075072449",
#     "3741412165203223329",
#     "6229131422133165537",
#     "8453562226394645565",
#     "1860719855193238638",
#     "7733357487126135024",
#     "0214559922167551320",
#     "7296870218120319423",
#     "9345874212263727593",
#     "7080279844181717938",
#     "1824571588290713607",
#     "7670149473508646298",
#     "8133043886862147126",
#     "3734905590915086611",
#     "2848406054694660852",
#     "5275355330592340779",
#     "1315950688822365620"
# ])
#
# p = "\n".join([
#     "03473412",
#     "77758443",
#     "11387397",
#     "52647162",
#     "08930712",
#     "94252611",
#     "98265206",
#     "69421813"
# ])

q = "\n".join([
    "6583840257821498",
    "2141577183136747",
    "4361881028460674",
    "3083494148067891",
    "1118603805589150",
    "5674382521585688",
    "2994769341032596",
    "5274865348169898",
    "4213871367777144",
    "0830949732487642",
    "4557259292839554",
    "5571053752513745",
    "9114693839199374",
    "9646414448781792",
    "1385614097628823",
    "3136426393343741"
])

# print(path_finder(a) == 0)
# print(path_finder(b) == 2)
# print(path_finder(c) == 4)
print(path_finder(d) == 42)
# print(path_finder(e)== 14)
# print(path_finder(f)== 0)
# print(path_finder(g)== 4)
# print(path_finder(m)== 30)
# print(path_finder(n)== 50)
# print(path_finder(p)== 27)

# print(path_finder(q)== 39)


# min_total_climb_rounds = 3
# tmp_new_open_set = {(1, 0, 0, 5), (0, 1, 3, 3)}
#
# if all([tmp_coordinate[3] == 3 for tmp_coordinate in tmp_new_open_set]):
#     print ("True")
# else:
#     print("False")

# check = True
# for tmp_coordinate in tmp_new_open_set:
#     if min_total_climb_rounds != tmp_coordinate[3]:
#         check = False
# print(check)








