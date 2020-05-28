# Codewar Path Finder #1: can you reach the exit?

# Task
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North,
# East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
#
# Empty positions are marked .
# Walls are marked W
# Start and exit positions are empty in all test cases.
#
# Treat it like a matrix,(0,0) means first element of the first row(TOP LEFT) and (n-1,n-1) means last element of
# the last row(BOTTOM RIGHT)--> Trattalo come una matrice, (0,0) significa primo elemento della prima riga (TOP LEFT)
# e (n-1, n-1) significa l'ultimo elemento dell'ultima riga (BOTTOM RIGHT).
#
# Path Finder Series:
# #1: can you reach the exit?
# #2: shortest path
# #3: the Alpinist
# #4: where are you?
# #5: there's someone here


def path_finder(maze):
    num_row = 0
    rows = maze.split('\n')
    num_row =len(rows)
    num_col = len(rows[0])
    finish = [num_row-1, num_col-1]
    # print(finish)
    grid = build_maze(maze)
    print(*grid, sep='\n')
    open_set = set()
    open_set.add((0, 0))
    checked_set = set()
    result = exist_path(open_set, checked_set, finish, grid)
    return result

def build_maze(maze):
    board = []
    for element in maze.split('\n'):
        board.append(element)
    return board

def exist_path(open_set, checked_set, finish, grid):
    move = [[+1, 0], [-1, 0], [0, +1], [0, -1]]

    while open_set:
        new_open_set = set()
        for coordinate in open_set:
            x = coordinate[0]
            y = coordinate[1]
            if x == finish[0] and y == finish[1]:
                return True
            else:
                for dir in move:
                    if (x + dir[0] >= 0 and  x + dir[0] < finish[0]+1) and \
                            (y + dir[1] >= 0 and  y + dir[1] < finish[1]+1) and \
                            (grid[x + dir[0]][y + dir[1]] == '.'):
                        if (x + dir[0], y + dir[1]) not in checked_set:
                            new_open_set.add((x + dir[0], y + dir[1]))
            checked_set.add(coordinate)

        open_set = new_open_set
        # return exist_path(open_set, checked_set, finish, grid)
    return False





a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W."
])

b = "\n".join([
    ".W.",
    ".W.",
    "W.."
])

c = "\n".join([
    "......",
    "......",
    "......",
    "......",
    "......",
    "......"
])

d = "\n".join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "....W."
])

print(path_finder(a) == True) #, True)
print(path_finder(b) == False) #, False)
print(path_finder(c) == True) #, True)
print(path_finder(d) == False) #, False)

#old solution, no performance:
# Codewar Path Finder #1: can you reach the exit?

# Task
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North,
# East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
#
# Empty positions are marked .
# Walls are marked W
# Start and exit positions are empty in all test cases.
#
# Treat it like a matrix,(0,0) means first element of the first row(TOP LEFT) and (n-1,n-1) means last element of
# the last row(BOTTOM RIGHT)--> Trattalo come una matrice, (0,0) significa primo elemento della prima riga (TOP LEFT)
# e (n-1, n-1) significa l'ultimo elemento dell'ultima riga (BOTTOM RIGHT).
#
# Path Finder Series:
# #1: can you reach the exit?
# #2: shortest path
# #3: the Alpinist
# #4: where are you?
# #5: there's someone here
#
#
# def path_finder(maze):
#     num_row = 0
#     rows =  maze.split('\n')
#     num_row =len(rows)
#     num_col = len(rows[0])
#     start = [0, 0]
#     finish = [num_row-1, num_col-1]
#     # print(finish)
#     grid = draw_maze(maze)
#     print(*grid, sep='\n')
#     open_set = [start]
#     checked_set = []
#     result = exist_path(open_set, checked_set, finish, grid)
#     return result
#
# def draw_maze(maze):
#     board = []
#     for element in maze.split('\n'):
#         board.append(element)
#     return board
#
# def exist_path(open_set, checked_set, finish, grid):
#     move = [[+1, 0], [-1, 0], [0, +1], [0, -1]]
#     new_open_set = []
#     while open_set:
#         for i in range(len(open_set)):
#             x = open_set[i][0]
#             y = open_set[i][1]
#             if x == finish[0] and y == finish[1]:
#                 return True
#             else:
#                 temp_new_open_set = [[x+i[0], y+i[1]] for i in move
#                                      if x + i[0] >= 0 and  x + i[0] < finish[0]+1
#                                      if y + i[1] >= 0 and  y + i[1] < finish[1]+1
#                                      if grid[x + i[0]][y + i[1]] == '.']
#                 for field in temp_new_open_set:
#                     if field not in new_open_set:
#                         new_open_set.append(field)
#                 temp_new_open_set = []
#             if open_set[i] not in checked_set:
#                 checked_set.append(open_set[i])
#         # print(new_open_set)
#         list_del = []
#         for item in new_open_set:
#             for el in checked_set:
#                 if el == item and item not in list_del:
#                     list_del.append(item)
#         # print(list_del)
#         # print("+"*20)
#         if list_del:
#             for elem in list_del:
#                 # print(new_open_set)
#                 new_open_set.remove(elem)
#         open_set = new_open_set
#         # return exist_path(open_set, checked_set, finish, grid)
#     return False

    # gridline = []
    # for i in range(count):
    #     gridline.append('.')
    # grid = []
    # for i in range(count):
    #     grid.append(list(gridline))
    # print(*grid, sep='\n')

    # height = len(maze)
    # print(height)
    # length = 0
    # my_list = ''.join(element for element in maze.split('\n'))
    # print(my_list)
    # print("="*20)
    #
    # gridline = []
    # for i in range(len(maze)):
    #     gridline.append(maze[i].split('\n'))
    # print(gridline)
    # grid = []
    # for i in range(self.row):
    #     grid.append(list(gridline))
    #


    # for i in range(len(maze)):
    #     print(i)
    #     for char in maze:
    # print()

# for elem in my_list:
#     n_address = ' '.join(fields for fields in elem.split()
#                          if fields[0] != '<' and fields[0] != '+' and fields[-1] != '>')
#     my_address.append(n_address)

# print(element)


#    return # can go to lower right corner from upper left one (puoi andare nell'angolo in basso a destra da quello
# in alto a sinistra)
# def draw_grid(self): # Method to build the grid
#     gridline = []
#     for i in range(self.col):
#         gridline.append(0)
#     grid = []
#     for i in range(self.row):
#         grid.append(list(gridline))
#     return grid







