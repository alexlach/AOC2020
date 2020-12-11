import pprint
import copy
pp = pprint.PrettyPrinter(indent=0)
area = list(map(list, open("11/input.txt").read().split("\n")))
pp.pprint(area)
row_count = len(area)
col_count = len(area[0])

def update_grid(grid):
    new_grid = copy.deepcopy(grid)
    resolved = True
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            count_filled = 0
            if grid[row][col] != '.':
                for neighbor_row in range(max(row - 1, 0), min(row + 2, row_count)):
                    for neighbor_col in range(max(col - 1, 0), min(col + 2, col_count)):
                        if grid[neighbor_row][neighbor_col] == '#':
                            count_filled += 1
            if grid[row][col] == 'L' and count_filled == 0:
                new_grid[row][col] = '#'
                resolved = False
            elif grid[row][col] == '#' and count_filled >= 5:
                new_grid[row][col] = 'L'
                resolved = False
    return new_grid, resolved

resolved = False
iterations = 0
while not resolved:
    area, resolved = update_grid(area)
    iterations += 1
    print(iterations)
for row in area:
    print(''.join(row))
print(f"Resolved in {iterations} iterations.")
print(sum(x.count('#') for x in area))

# if row in range(rows) and col in range(cols):
#     print(row + " " + col)