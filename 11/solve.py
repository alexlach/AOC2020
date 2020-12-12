import copy


def update_grid(grid):
    new_grid = copy.deepcopy(grid)
    resolved = True
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            count_filled = 0
            if grid[row][col] != ".":
                for neighbor_row in range(max(row - 1, 0), min(row + 2, row_count)):
                    for neighbor_col in range(max(col - 1, 0), min(col + 2, col_count)):
                        if grid[neighbor_row][neighbor_col] == "#":
                            count_filled += 1
            if grid[row][col] == "L" and count_filled == 0:
                new_grid[row][col] = "#"
                resolved = False
            elif grid[row][col] == "#" and count_filled > 4:
                new_grid[row][col] = "L"
                resolved = False
    return new_grid, resolved


# Part 1
area = list(map(list, open("11/input.txt").read().split("\n")))
row_count = len(area)
col_count = len(area[0])
resolved = False
while not resolved:
    area, resolved = update_grid(area)
seat_count = sum(x.count("#") for x in area)
print(f"Final grid contains {seat_count} occupied seats.")


# Part 2 (line of sight updating of grid)
def check_direction(grid, coord, step):
    occupied_seat_found = False
    reached_end = False
    while not reached_end:
        coord = (coord[0] + step[0], coord[1] + step[1])
        if coord[0] not in range(row_count) or coord[1] not in range(col_count):
            reached_end = True
        elif grid[coord[0]][coord[1]] == "L":
            reached_end = True
        elif grid[coord[0]][coord[1]] == "#":
            occupied_seat_found = True
            reached_end = True
    return occupied_seat_found


def count_seats_in_sight(grid, coord):
    occupied_seat_count = 0
    for row_step in (-1, 0, 1):
        for col_step in (-1, 0, 1):
            step = (row_step, col_step)
            occupied_seat_count += check_direction(grid, coord, step)
    return occupied_seat_count


def update_grid_line_of_sight(grid):
    new_grid = copy.deepcopy(grid)
    resolved = True
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            count_filled = 0
            if grid[row][col] != ".":
                count_filled = count_seats_in_sight(grid, (row, col))
            if grid[row][col] == "L" and count_filled == 0:
                new_grid[row][col] = "#"
                resolved = False
            elif grid[row][col] == "#" and count_filled > 5:
                new_grid[row][col] = "L"
                resolved = False
    return new_grid, resolved


area = list(map(list, open("11/input.txt").read().split("\n")))
resolved = False
while not resolved:
    area, resolved = update_grid_line_of_sight(area)
seat_count = sum(x.count("#") for x in area)
print(f"Final grid contains {seat_count} occupied seats.")