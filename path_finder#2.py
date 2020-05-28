# codewar Path Finder #2: shortest path

# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North,
# East, South, West). Return the minimal number of steps to exit position [N-1, N-1] if it is possible to reach the
# exit from the starting position. Otherwise, return false in JavaScript/Python and -1 in C++/C#/Java.
#
# Empty positions are marked .. Walls are marked W. Start and exit positions are guaranteed to be empty
# in all test cases.

def path_finder(maze):
    num_row = 0
    rows = maze.split('\n')
    num_row =len(rows)
    num_col = len(rows[0])
    finish = [num_row-1, num_col-1]
    print(finish)
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
    count_move = 0
    while open_set:
        new_open_set = set()
        for coordinate in open_set:
            x = coordinate[0]
            y = coordinate[1]
            if x == finish[0] and y == finish[1]:
                return count_move
            else:
                for dir in move:
                    if (x + dir[0] >= 0 and  x + dir[0] < finish[0]+1) and \
                            (y + dir[1] >= 0 and  y + dir[1] < finish[1]+1) and \
                            (grid[x + dir[0]][y + dir[1]] == '.'):
                        if (x + dir[0], y + dir[1]) not in checked_set:
                            new_open_set.add((x + dir[0], y + dir[1]))
            checked_set.add(coordinate)
        count_move += 1
        open_set = new_open_set
    return False








a = "\n".join([
    ".W.",
    ".W.",
    "..."
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


print(path_finder(a)==4)
# print(path_finder(b)== False)
# print(path_finder(c)== 10)
# print(path_finder(d)== False)


