adapters = open("10/input.txt").read().split("\n")
adapters = [int(num) for num in adapters]
adapters.append(0)
adapters.append(max(adapters) + 3)

# Part 1
adapters = sorted(adapters)
offset_diff = [y - x for x, y in zip(adapters, adapters[1:])]
print(offset_diff.count(3) * offset_diff.count(1))

# Part 2
paths = {0: 1}  # for adapter at index of key N, how many unique paths lead there
for adapter in adapters[1:-1]:
    paths[adapter] = (
        paths.get(adapter - 1, 0)
        + paths.get(adapter - 2, 0)
        + paths.get(adapter - 3, 0)
    )
print(f"Possible arrangements of adapters: {paths[max(paths.keys())]}")