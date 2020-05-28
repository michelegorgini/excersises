# Stargate SG-1: Cute and Fuzzy (Improved version)

# Your Mission
# Given a string containing the current state of the control crystals inner pathways (labeled as "X") and
# its gaps (labeled as "."), generate the shortest path from the start node (labeled as "S") to the goal node
# (labeled as "G") and return the new pathway (labeled with "P" characters).
# If no solution is possible, return the string "Oh for crying out loud..." (in frustration).
#
#
# The Rules
# - Nodes labeled as "X" are not traversable.
# - Nodes labeled as "." are traversable.
# - A pathway can be grown in eight directions (up, down, left, right, up-left, up-right, down-left, down-right),
# so diagonals are possible.
# - Nodes labeled "S" and "G" are not to be replaced with "P" in the case of a solution.
# - The shortest path is defined as the path with the shortest euclidiean distance going from one node to the next.
# - If several paths are possible with the same shortest distance, return any one of them.
#
# Note that the mazes won't always be squares.
#
#
# Example #1: Valid solution
# .S...             .SP..
# XXX..             XXXP.
# .X.XX      =>     .XPXX
# ..X..             .PX..
# G...X             G...X
#
# Example #2: No solution
# S....
# XX...
# ...XX      =>     "Oh for crying out loud..."
# .XXX.
# XX..G
#
#
# Note: Your solution will have to be efficient because it will have to deal with a lot of maps and big ones.
# Caracteristics of the random tests:
#
# map sizes from 3x3 to 73x73 (step is 5 from one size to the other, mazes won't always be squares)
# 20 random maps for each size.
# Overall, 311 tests to pass with the fixed ones.


# This Solution works. I rewrite to make it more readable
import math

def wire_DHD_SG1(existingWires):
    grid = build_maze(existingWires)
    # print(grid)
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
                open_dict[new_key] = [], 0
            if grid[ind_row][ind_col] == 'G':
                finish = [ind_row, ind_col]
    # print(open_dict)
    # print("?"*5)
    result = shotest_exist_path(open_dict, checked_dict, finish, grid, num_row, num_col)
    return result


def build_maze(maze):
    board = []
    for element in maze.split('\n'):
        print(element)
        # print("ele "*3 )
        board.append(list(element))
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
            previous_value_dict = vals[0]      # keep the key of dict_move previous step iteration
            distance = vals[1]               # path distance
            if x == finish[0] and y == finish[1]:
                if distance <= shorter_distance:
                    set_reach_g[keys] = previous_value_dict , distance
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
                                ## problematic solution:
                                ## previous_value_dict.append(.....)
                                best_list = previous_value_dict[:]
                                best_list.append((new_x, new_y))
                                new_open_set[tmp_key] = best_list, distance
                                # new_open_set[tmp_key] = previous_key_dict + key, distance old solution
                            else:
                                tmp_values = new_open_set[tmp_key]
                                if tmp_values[1] > distance:
                                    del new_open_set[tmp_key]
                                    best_list = previous_value_dict[:]
                                    best_list.append((new_x, new_y))
                                    new_open_set[tmp_key] = best_list, distance
                        else:
                            if checked_dict_set.get(tmp_key) > distance:
                                del checked_dict_set[tmp_key]
                                best_list = previous_value_dict[:]
                                best_list.append((new_x, new_y))
                                new_open_set[tmp_key] = best_list, distance
                        distance = vals[1]
            if keys not in checked_dict_set.keys():
                checked_dict_set[keys] = distance
        open_dict_set = new_open_set
    if set_reach_g:
        #print(set_reach_g)
        for short_key, short_value in set_reach_g.items():
            if short_value[1] == shorter_distance:
                return draw_shortest_path(short_value, grid)  # method to draw shortest solution
    else:
        return "Oh for crying out loud..."


def draw_shortest_path(steps_values, grid):
    grid_result = ""
    for step in steps_values[0]:
        x = step[0]
        y = step[1]
        if grid[x][y] == '.':
            grid[x][y] = 'P'
    for row in range(len(grid)):
        grid_result = grid_result + ''.join(grid[row]) + '\n'
    grid_result = grid_result[:-1]
    print(grid_result)
    return grid_result



# # Solution more readable.
#
# import math
#
# class Path:
#     def __init__(self, existingWires):
#         self.maze = existingWires
#         self.grid = self.build_maze()
#         self.num_row =len(self.grid)
#         self.num_col = len(self.grid[0])
#         # open_dict --> key = coordinate new position to check. value 1 = track previous steps, value 2 = distance
#         # open_dict begins with start position
#         self.open_dict_set = self.calculate_start_position()
#         # checked_dict --> key = coordinate position checked. value = distance
#         self.checked_dict_set = {}
#         # finish --> coordinate position letter G (destination path)
#         self.finish = self.calculate_final_position()
#         self.dict_move = {"1": [+1, 0],       # keys from "1" to "4" = horizontal and vertical moves --> distance = 1
#                           "2": [-1, 0],
#                           "3": [0, +1],
#                           "4": [0, -1],
#                           "5": [+1, +1],      # keys from "5" to "8" = diagonal moves --> distance = √2
#                           "6": [+1, -1],
#                           "7": [-1, +1],
#                           "8": [-1, -1]}
#         self.set_final_paths = {}                 # dictionary with information about shorter distance
#
#     def calculate_start_position(self):
#         start = {}
#         for ind_row in range(self.num_row):
#             for ind_col in range(self.num_col):
#                 if self.grid[ind_row][ind_col] == 'S':
#                     new_key = ind_row, ind_col
#                     start[new_key] = '', 0
#         return start
#
#     def calculate_final_position(self):
#         destination = []
#         for ind_row in range(self.num_row):
#             for ind_col in range(self.num_col):
#                 if self.grid[ind_row][ind_col] == 'G':
#                     destination = [ind_row, ind_col]
#         return destination
#
#     def build_maze(self):
#         board = []
#         for element in self.maze.split('\n'):
#             board.append(element)
#         return board
#
#     def shorter_distance(self):
#         while self.open_dict_set:
#             new_open_set = {}
#             for coord_key, path_values in self.open_dict_set.items():
#                 x = coord_key[0]
#                 y = coord_key[1]
#                 keep_steps_track = path_values[0]
#                 distance = path_values[1]
#                 if x == self.finish[0] and y == self.finish[1]:
#                     self.check_content_final_paths(distance, keep_steps_track, coord_key)
#                 else:
#                     for key, neighbor in self.dict_move.items():
#                         if (x + neighbor[0] >= 0 and  x + neighbor[0] < self.num_row) and \
#                                 (y + neighbor[1] >= 0 and  y + neighbor[1] < self.num_col) and \
#                                 (self.grid[x + neighbor[0]][y + neighbor[1]] == '.' or
#                                  self.grid[x + neighbor[0]][y + neighbor[1]] == 'G'):
#                             new_x = x + neighbor[0]
#                             new_y = y + neighbor[1]
#                             tmp_key = new_x, new_y   # new key for new_open_set and checked_dict_set
#                             new_distance = self.calculate_new_distance(key, distance)
#                             if tmp_key not in self.checked_dict_set.keys():
#                                 if tmp_key not in new_open_set.keys():
#                                     new_open_set[tmp_key] = keep_steps_track + key, new_distance
#                                 else:
#                                     (old_steps, old_distance) = new_open_set[tmp_key]
#                                     if old_distance > new_distance:
#                                         del new_open_set[tmp_key]
#                                         new_open_set[tmp_key] = keep_steps_track + key, new_distance
#                             else:
#                                 if self.checked_dict_set.get(tmp_key) > new_distance:
#                                     del self.checked_dict_set[tmp_key]
#                                     new_open_set[tmp_key] = keep_steps_track + key, new_distance
#                 if coord_key not in self.checked_dict_set.keys():
#                     self.checked_dict_set[coord_key] = distance
#             self.open_dict_set = new_open_set
#         if self.set_final_paths:
#             for coordinate, (steps, route) in self.set_final_paths.items():
#                 return self.draw_shorter_path(coordinate, steps)
#         else:
#             return "Oh for crying out loud..."
#
#     def check_content_final_paths(self, distance, keep_steps_track, coord_key):
#         if self.set_final_paths:
#             for coordinate, (steps, route) in self.set_final_paths.items():
#                 if route > distance:
#                     del self.set_final_paths[coordinate]
#                     self.set_final_paths[coord_key] = keep_steps_track, distance
#         else:
#             self.set_final_paths[coord_key] = keep_steps_track, distance
#
#     def calculate_new_distance(self,key, distance):
#         calculate_distance = distance
#         if int(key) > 4:
#             calculate_distance = calculate_distance + math.sqrt(2)
#         else:
#             calculate_distance = calculate_distance + 1
#         return calculate_distance
#
#
# # class DrawPath(Path):
# #
# #     def __init__(self):
# #         Path.__init__(self)
#
#     def draw_shorter_path(self, coordinate, steps):
#         tmp_grid = self.grid
#         if len(steps) < 2:
#             return self.prepare_final_grid(tmp_grid)
#         else:
#             tmp_grid = self.mark_path_with_p(coordinate, steps, tmp_grid)
#             return self.prepare_final_grid(tmp_grid)
#
#     def mark_path_with_p(self, coordinate, steps, tmp_grid):
#         x = int(coordinate[0])
#         y = int(coordinate[1])
#         path_with_p = []
#         for step in reversed(steps):
#             for key, val in self.dict_move.items():
#                 if step == key:
#                     x = (x + (val[0]*-1))
#                     y = (y + (val[1]*-1))
#                     if self.grid[x][y] == '.':
#                         path_with_p.append((x, y))
#         sorted_path_with_p = sorted(path_with_p, key=lambda elem: elem[0])
#         for row in range(len(tmp_grid)):
#             for step in sorted_path_with_p:
#                 if row == step[0]:
#                     tmp_row = ""
#                     tmp_row = tmp_grid[step[0]][:step[1]] + "P" + tmp_grid[step[0]][step[1]+1:]
#                     tmp_grid[row] = tmp_row
#         print(*tmp_grid, sep='\n')
#         print('pppp' *5)
#         return tmp_grid
#
#     def prepare_final_grid(self, tmp_grid):
#         grid_result = ""
#         for row in range(len(tmp_grid)):
#             grid_result = grid_result + tmp_grid[row] + '\n'
#         grid_result = grid_result[:-1]
#         return grid_result
#
#
# def wire_DHD_SG1(existingWires):
#     game = Path(existingWires)
#     result = game.shorter_distance()
#     # print(result)
#     return result



#
# # 1
# existingWires = """
# SX.
# XX.
# ..G
# """.strip('\n')

# print(wire_DHD_SG1(existingWires) == "Oh for crying out loud...")


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
# # 3
#
# existingWires = """
# .S.
# ...
# .G.
# """.strip('\n')
#
# print(wire_DHD_SG1(existingWires) == """
# .S.
# .P.
# .G.
# """.strip('\n'))
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
existingWires = """
...
SG.
...
""".strip('\n')

print(wire_DHD_SG1(existingWires) == """
...
SG.
...
""".strip('\n'))
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





