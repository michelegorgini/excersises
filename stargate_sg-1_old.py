import math

def wire_DHD_SG1(existingWires):
    grid = build_maze(existingWires)
    #print(*grid, sep='\n')
    # print(grid[2][2])
    num_row =len(grid)
    num_col = len(grid[0])
    # print(num_row, num_col)
    open_dict = {}
    checked_dict = {}
    finish = []
    for ind_row in range(num_row):
        for ind_col in range(num_col):
            if grid[ind_row][ind_col] == 'S':
                new_key = ind_row, ind_col
                open_dict[new_key] = '', 0
            if grid[ind_row][ind_col] == 'G':
                finish = [ind_row, ind_col]
    result = shotest_exist_path(open_dict, checked_dict, finish, grid, num_row, num_col)
    return result


def build_maze(maze):
    board = []
    for element in maze.split('\n'):
        board.append(element)
    return board


def shotest_exist_path(open_dict_set, checked_dict_set, finish, grid, num_row, num_col):
    dict_move = {"1": [+1, 0],
                 "2": [-1, 0],
                 "3": [0, +1],
                 "4": [0, -1],
                 "5": [+1, +1],
                 "6": [+1, -1],
                 "7": [-1, +1],
                 "8": [-1, -1]}
    shorter_distance = 1000000
    set_reach_g = {}
    while open_dict_set:
        new_open_set = {}
        for keys, vals in open_dict_set.items():
            # print(keys)
            # print(vals)
            # print("k "*5)
            x = keys[0]
            y = keys[1]
            previous_key_dict = vals[0]      # keep the key of dict_move previous step iteration
            print(previous_key_dict)
            distance = vals[1]               # path distance
            if x == finish[0] and y == finish[1]:
                if distance <= shorter_distance:
                    set_reach_g[keys] = previous_key_dict , distance
                    shorter_distance = distance
            else:
                for key, val in dict_move.items():
                    if (x + val[0] >= 0 and  x + val[0] < num_row) and \
                            (y + val[1] >= 0 and  y + val[1] < num_col) and \
                            (grid[x + val[0]][y + val[1]] == '.' or grid[x + val[0]][y + val[1]] == 'G'):
                        new_x = x + val[0]
                        new_y = y + val[1]
                        tmp_key = new_x, new_y   # new key for new_open_set and checked_dict_set
                        if int(key) > 4:
                            distance = distance + math.sqrt(2)
                        else:
                            distance = distance + 1
                        if tmp_key not in checked_dict_set.keys():
                            if tmp_key not in new_open_set.keys():
                                new_open_set[tmp_key] = previous_key_dict + key, distance
                            else:
                                tmp_values = new_open_set[tmp_key]
                                if tmp_values[1] > distance:
                                    del new_open_set[tmp_key]
                                    new_open_set[tmp_key] = previous_key_dict + key, distance
                        else:
                            if checked_dict_set.get(tmp_key) > distance:
                                del checked_dict_set[tmp_key]
                                new_open_set[tmp_key] = previous_key_dict + key, distance
                        distance = vals[1]
            if keys not in checked_dict_set.keys():
                checked_dict_set[keys] = distance
        open_dict_set = new_open_set
    if set_reach_g:
        for short_key, short_value in set_reach_g.items():
            if short_value[1] == shorter_distance:
                return draw_shortest_path(short_key, short_value, grid, dict_move)  # method to draw shortest solution
    else:
        return "Oh for crying out loud..."


def draw_shortest_path(coordinate, list_values, grid, dict_move):
    tmp_grid = grid
    tmp_row = ""
    grid_result = ""
    path_with_P =[]
    x = int(coordinate[0])
    y = int(coordinate[1])
    if len(list_values[0]) < 2:
        for row in range(len(grid)):
            grid_result = grid_result + grid[row] + '\n'
        grid_result = grid_result[:-1]
        # print(grid_result)
        # print()
        return grid_result
    else:
        for step in reversed(list_values[0]):
            for key, val in dict_move.items():
                if step == key:
                    x = (x + (val[0]*-1))
                    y = (y + (val[1]*-1))
                    if grid[x][y] == '.':
                        path_with_P.append((x, y))
        sorted_path_with_P = sorted(path_with_P, key=lambda elem: elem[0])
        for row in range(len(tmp_grid)):
            for step in sorted_path_with_P:
                if row == step[0]:
                    tmp_row = tmp_grid[step[0]][:step[1]] + "P" + tmp_grid[step[0]][step[1]+1:]
                    tmp_grid[row] = tmp_row
                    tmp_row = ''
        for row in range(len(tmp_grid)):
            grid_result = grid_result + tmp_grid[row] + '\n'
        grid_result = grid_result[:-1]
        print(grid_result)
        return grid_result



#
# # 1
# existingWires = """
# SX.
# XX.
# ..G
# """.strip('\n')

# print(wire_DHD_SG1(existingWires) == "Oh for crying out loud...")


# 2
# existingWires = """
# SX.
# X..
# XXG
# """.strip('\n')

# print(wire_DHD_SG1(existingWires) == """

#
# SX.
# XP.
# XXG
# """.strip('\n'))
#
# 3

# 2
existingWires = """
SX.
X..
XXG
""".strip('\n')

print(wire_DHD_SG1(existingWires) == """
SX.
XP.
XXG
""".strip('\n'))
#
# # 4
#
# existingWires = """
# ...
# S.G
# ...
# """.strip('\n')
#
# print(wire_DHD_SG1(existingWires) == """
# ...
# SPG
# ...
# """.strip('\n'))
#
# # 5
#
# existingWires = """
# ...
# SG.
# ...
# """.strip('\n')
#
# print(wire_DHD_SG1(existingWires) == """
# ...
# SG.
# ...
# """.strip('\n'))
#
# # 6
#
# existingWires = """
# .S...
# XXX..
# .X.XX
# ..X..
# G...X
# """.strip('\n')
#
# print(wire_DHD_SG1(existingWires) == """
# .SP..
# XXXP.
# .XPXX
# .PX..
# G...X
# """.strip('\n'))
#
# # # 7
# #
# existingWires = """
# XX.S.XXX..
# XXXX.X..XX
# ...X.XX...
# XX...XXX.X
# ....XXX...
# XXXX...XXX
# X...XX...X
# X...X...XX
# XXXXXXXX.X
# G........X
# """.strip('\n')
# #
# print(wire_DHD_SG1(existingWires) ==
# # """
# # XX.S.XXX..
# # XXXXPX..XX
# # ...XPXX...
# # XX.P.XXX.X
# # ...PXXX...
# # XXXXPP.XXX
# # X...XXP..X
# # X...X..PXX
# # XXXXXXXXPX
# # GPPPPPPP.X
# # """.strip('\n') ,
# """
# XX.S.XXX..
# XXXXPX..XX
# ...XPXX...
# XX..PXXX.X
# ...PXXX...
# XXXXPP.XXX
# X...XXP..X
# X...X..PXX
# XXXXXXXXPX
# GPPPPPPP.X
# """.strip('\n'))
#
#
#
# # # 8
# #
# # existingWires = """
# # .X.X.X....XXXXXX...X
# # XX.XX.XXXXXXXXXXX..X
# # .X.X.XX..X..X.XXXXXX
# # X.X..XXX...XX.X.XXX.
# # X.X..X..XXX.X.X.X...
# # .XXX..XXXXX.X.X..XX.
# # X.XX.SX......XXX..X.
# # .XXXXX.XXX...XX..X..
# # ....X.XX..X.XX.X..XX
# # ....X..XX..XX..X.XX.
# # X...X..XX.X.X.XX...X
# # .XXX.........X.XX..G
# # ..XX.XX.XX.X.XXXXXX.
# # .X.X...X.X.XXXX..X.X
# # ..X..XXX.XX....XXXX.
# # XX..XXXXXXX.....XXXX
# # XXXX.X.X..XXXXXX...X
# # X...X..X..XXXX..X..X
# # X.XXXXX..XX..XXX.X.X
# # XX.X.XX.XXXX.X..X.XX
# # """.strip('\n')
# #
# # print(wire_DHD_SG1(existingWires) == """
# # .X.X.X....XXXXXX...X
# # XX.XX.XXXXXXXXXXX..X
# # .X.X.XX..X..X.XXXXXX
# # X.X..XXX...XX.X.XXX.
# # X.X..X..XXX.X.X.X...
# # .XXX..XXXXX.X.X..XX.
# # X.XX.SXPPP...XXX..X.
# # .XXXXXPXXXP..XXP.X..
# # ....X.XX..XPXXPXP.XX
# # ....X..XX.PXXP.XPXX.
# # X...X..XX.XPXPXX.P.X
# # .XXX........PX.XX.PG
# # ..XX.XX.XX.X.XXXXXX.
# # .X.X...X.X.XXXX..X.X
# # ..X..XXX.XX....XXXX.
# # XX..XXXXXXX.....XXXX
# # XXXX.X.X..XXXXXX...X
# # X...X..X..XXXX..X..X
# # X.XXXXX..XX..XXX.X.X
# # XX.X.XX.XXXX.X..X.XX
# # """.strip('\n'))
#
#





