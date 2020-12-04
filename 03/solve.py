import functools, operator

reader = open('03/input.csv','r')
grid = []
for line in reader.readlines():
    grid.append(line.replace("\n", ""))

grid_width = len(grid[0])
grid_height = len(grid)

# Part 1
tree_count = 0
col = 0
row = 0
while row < grid_height - 1:
    col += 3
    row += 1
    if grid[row][col % grid_width] == '#':
        tree_count += 1
print(f"Tree Count: {tree_count}")

# Part 2
slope_list = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
tree_count_list = []
for slope in slope_list:
    tree_count = 0
    col = 0
    row = 0
    while row < grid_height - 1:
        col += slope[0]
        row += slope[1]
        if grid[row][col % grid_width] == '#':
            tree_count += 1
    tree_count_list.append(tree_count)
print(f"Product: {functools.reduce(operator.mul, tree_count_list)}")