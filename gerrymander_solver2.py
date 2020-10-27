# Codewar: Gerrymander Solver

# gerrymander — noun. the dividing of a state, county, etc., into election districts so as to give one political
# party a majority in many districts while concentrating the voting strength of the other party into as few districts
# as possible.
#
# Objective:
# Given a 5 x 5 region populated by 25 citizens, your task is to write a function that divides the region into 5
# districts given the following conditions:
# - 10 citizens will vote for your candidate, while the other 15 will vote for the opponent
# - Your candidate must win the popular vote for 3 of the 5 districts
# - Each district must have an equal number of voters
# - Each district must be one contiguous cluster of voters (i.e. each voter has one or more orthogonally adjacent
#   neighbors from the same district)
#
# Concept Overview:
#
# A: You're given a 5 x 5 square matrix representing the layout of the region occupied by eligible voters.
# The following panels show different ways to set boundaries for 5 districts.
#
# B: Proportionate outcome — blue and red win in proportion to their voting
# C: Disproportionate outcome — blue wins all
# D: Disproportionate outcome — red wins majority despite having fewer total supporters
# Your function must solve the challenge presented in panel D
#
# Input
# Your function will receive a newline-separated string consisting of X and O characters.
# The Os represent the voters in support of your candidate, and the Xs represent those in support of the opponent.
#
# Output
# Your function should return a 5x5 newline-separated string comprised of the digits 1 through 5 where each group
# of identical digits represents its own unique district.
#
# If a solution does not exist, return null, None, or nil
#
# Test Example
#
# region = [
#     'OOXXX',
#     'OOXXX',
#     'OOXXX',
#     'OOXXX',
#     'OOXXX'
# ]
#
# # one possible solution where regions 1,2, and 3 are won
# gerrymander('\n'.join(region)) # '11114\n12244\n22244\n35555\n33335'
# Testing Constraints
# Full Test Suite: 10 fixed tests and 10 randomly-generated tests
# Zero or more valid solutions will exist for each test
# Inputs will always be valid

from itertools import combinations


def gerrymander(s):
    #s = s.split('\n')
    grid = []
    for row in s:
        grid.append(list(row))
    # print(grid)
    num_row = len(s)
    num_col = len(s[0])
    my, other, allvote = all_vote_position(num_row, num_col, grid)
    # print(allvote)
    my_vote = set(my)
    other_vote = set(other)
    all_vote = set(allvote)
    result = calculate_combinations(all_vote, my_vote, grid)
    return result


def all_vote_position(num_row, num_col, grid):
    vote_my_candidate = set()
    vote_other_candidate = set()
    vote_all_vote = set()
    for row in range(0, num_row):
        for col in range(0, num_col):
            if grid[row][col] == 'O':
                vote_my_candidate.add((row, col))
                vote_all_vote.add((row, col))
            else:
                vote_other_candidate.add((row, col))
                vote_all_vote.add((row, col))
    # print(vote_my_candidate, vote_all_vote)
    return vote_my_candidate, vote_other_candidate, vote_all_vote


def calculate_combinations(all_vote, my_vote, grid):
    combs_my_vote = set()
    combs_my_district = set()
    all_combs = combinations(all_vote, 5)
    #print(all_vote)
    # next step I get district with 3 'O' and all cells adjacent
    for comb in all_combs:
        if district_myvote_win(comb, my_vote):
            combs_my_vote.add(comb)
    # print(*sorted(combs_my_vote), sep= '\n')  # we have here the correct districts
    combs_3_districts = combinations(combs_my_vote, 3)
    # next step I get 3 district, where I win, without cells in common
    for combs in combs_3_districts:
        if district_no_common_vote(combs):
            combs_my_district.add(combs)
    # next step I get all vote non present in my district to check if they are adjacent and complete the square.

    final_combs_districts = remain_vote_other_candidate(all_vote, combs_my_district)
    # print(final_combs_districts, grid)
    if final_combs_districts:
        return built_result(final_combs_districts, grid)
    else:
        return None


def built_result(final_districts, grid):
    grid_result = ""
    for ind, district in enumerate(final_districts, start=1):
        for coordinate in district:
            x = coordinate[0]
            y = coordinate[1]
            grid[x][y] = ind
    # print(*grid, sep='\n')
    for row in range(len(grid)):
        grid_result = grid_result + ''.join(str(val)for val in grid[row]) + '\n'
    grid_result = grid_result[:-1]
    #print(grid_result, 'double')
    return grid_result


def district_myvote_win (combination, my_vote):
    # method to check if we have 3 my vote 'O' in every district combination
    count_myvote = 0
    for coordinate in combination:
        x = coordinate[0]
        y = coordinate[1]
        for x_myvote, y_myvote in my_vote:
            if (x == x_myvote) and (y == y_myvote):
                count_myvote += 1
    if count_myvote == 3:
        return district_adjacent_cells(combination)


def district_adjacent_cells(combs_check):
    # method to check if the district,  have all cell adjacent
    adjacent_moves = [[+1, 0], [-1, 0], [0, +1], [0, -1]]
    open_set = set()
    checked_set = set()
    combs_to_check = sorted(combs_check)
    open_set.add(combs_to_check[0])
    adjacent_position_to_check = combs_to_check[1:]
    count_cell_district = 0
    new_open_set = set()
    for i in range(1, 5):
        if count_cell_district < 4:
            find_adjacent = False
            for x_start, y_start in open_set:
                for move in adjacent_moves:
                    if (x_start + move[0] >= 0 and  x_start + move[0] < 5) and \
                            (y_start + move[1] >= 0 and  y_start + move[1]< 5):
                        new_x = x_start + move[0]
                        new_y = y_start + move[1]
                        for x_adjacent, y_adjacent in adjacent_position_to_check:
                            if new_x == x_adjacent and new_y == y_adjacent and \
                                    (new_x, new_y) not in new_open_set and (new_x, new_y) not in checked_set:
                                count_cell_district += 1
                                find_adjacent = True
                                new_open_set.add((new_x, new_y))
                                checked_set.add((new_x, new_y))
            # find_adjacent == True --> I found a cell adjacent in the district. Otherwise district is wrong
            if find_adjacent:
                open_set = new_open_set
                new_open_set = set()
            else:
                return False
    if count_cell_district == 4:
        return True
    else:
        return False

# def get_adjacent_cells( self, x_coord, y_coord ):
#     result = {}
#     for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
#         if (x,y) in grid.cells:
#             result[(x,y)] = grid.cells[(x,y)]




def district_no_common_vote(combs_district):
    # method to find all combination of 3 different district, where I won, without cell in common
    combs_districts = set(combs_district)
    checked_set = set()
    for comb in combs_districts:
        for coordinate in comb:
            if coordinate not in checked_set:
                checked_set.add(coordinate)
            else:
                return False
    return True


def remain_vote_other_candidate(all_vote, combs_my_district):
    # print(all_vote, combs_my_district)
    final_combinations = []
    for districts in combs_my_district:
        final_districts = []
        all_vote_remain = set(all_vote)
        for district in districts:
            final_districts.append(district)
            all_vote_remain = all_vote_remain.difference(district)
        combs_other_districts = remain_districts_other_candidate(all_vote_remain)
        if combs_other_districts:
            for comb in combs_other_districts:
                final_districts.append(comb)
                final_combinations = final_districts
    if final_combinations:
        return final_combinations
    else:
        return None


def remain_districts_other_candidate(all_vote_remain):
    adjacent_moves = [[+1, 0], [-1, 0], [0, +1], [0, -1]]
    open_set = set()
    checked_set = set()
    vote_remain_to_check = sorted(all_vote_remain)
    open_set.add(vote_remain_to_check[0])
    checked_set.add(vote_remain_to_check[0])
    adjacent_position_to_check = vote_remain_to_check[1:]
    count_cells = 0
    count_districts = 0
    new_open_set = set()
    while count_districts < 2:
        for i in range(1, 5):
            if count_cells < 4:
                find_adjacent = False
                for x_start, y_start in open_set:
                    for move in adjacent_moves:
                        if (x_start + move[0] >= 0 and  x_start + move[0] < 5) and \
                                (y_start + move[1] >= 0 and  y_start + move[1]< 5):
                            new_x = x_start + move[0]
                            new_y = y_start + move[1]
                            for x_adjacent, y_adjacent in adjacent_position_to_check:
                                if new_x == x_adjacent and new_y == y_adjacent and \
                                        (new_x, new_y) not in new_open_set and (new_x, new_y) not in checked_set:
                                    count_cells += 1
                                    find_adjacent = True
                                    new_open_set.add((new_x, new_y))
                                    checked_set.add((new_x, new_y))
                # find_adjacent == True --> I found a cell adjacent in the district. Otherwise district is wrong
                if find_adjacent:
                    open_set = new_open_set
                    new_open_set = set()
                else:
                    return False
        if count_cells == 4 and count_districts == 0:
            first_district = set(checked_set)
            count_districts += 1
            vote_remain_to_check = sorted(all_vote_remain.difference(checked_set))
            open_set = set()
            open_set.add(vote_remain_to_check[0])
            checked_set = set()
            checked_set.add(vote_remain_to_check[0])
            adjacent_position_to_check = vote_remain_to_check[1:]
            count_cells = 0
        elif count_cells == 4 and count_districts == 1:
            second_district = set(checked_set)
            return first_district, second_district
        else:
            return False





#s ='OOXXX\nOOXXX\nOOXXX\nOOXXX\nOOXXX'
#s ='XOXOX\nOXXOX\nXXOXX\nXOXOX\nOOXOX'

# s = [
#     'OOXXX',
#     'OOXXX',
#     'OOXXX',
#     'OOXXX',
#     'OOXXX']

# s = [
#     'XOXOX',
#     'OXXOX',
#     'XXOXX',
#     'XOXOX',
#     'OOXOX']
# #

# s = [
#     'XXOXO',
#     'XOXOX',
#     'OXOXO',
#     'XOXOX',
#     'XXOXX']
#
#print(gerrymander(s))


#test.describe('5 Example Tests')
s = [
    [
        'OOXXX',
        'OOXXX',
        'OOXXX',
        'OOXXX',
        'OOXXX'],
    [
        'XOXOX',
        'OXXOX',
        'XXOXX',
        'XOXOX',
        'OOXOX'],
    [
        'OXOOX',
        'XXOXO',
        'XOXXX',
        'XXOXX',
        'OXXOO'],
    [
        'XXOXO',
        'XOXOX',
        'OXOXO',
        'XOXOX',
        'XXOXX'],
    [
        'XXXXX',
        'OOOXO',
        'XXXOX',
        'OOOOO',
        'XXXXX']
]

gerrymander(s)

for i,v in enumerate('\n'.join(v) for v in s):
    (v,gerrymander(v),i == 3)
print('<COMPLETEDIN::>')


