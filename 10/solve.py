adapters = open("10/test.txt").read().split("\n")
adapters = [int(num) for num in adapters]
device_rating = max(adapters) + 3
adapters.append(0)
adapters.append(device_rating)

# Part 1
adapters = sorted(adapters)
offset_diff = [y - x for x, y in zip(adapters, adapters[1:])]
print(offset_diff.count(3) * offset_diff.count(1))

# Part 2
# start at the top
# loop through
print(adapters)
step_options = [1, 2, 3]


def num_ways(adapters, depth=""):
    ways = 0
    list_copy = adapters[:]
    if len(list_copy) == 1:
        print(f"\n{depth}Made it to the end", end="")
        return 1
    current_joltage = list_copy.pop(0)
    looking_for = [current_joltage + step for step in step_options]
    for num in list_copy:
        if num > max(looking_for):
            print(f" Dead end", end="")
            break
        elif num in looking_for:
            print(f"\n{depth}Step from {current_joltage} to {num}", end="")
            ways += num_ways(list_copy, depth + "  ")
    return ways


print(num_ways(adapters))