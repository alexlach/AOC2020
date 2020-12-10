xmas = open("09/input.txt").read().split("\n")
xmas = [int(num) for num in xmas]

# Part 1
def two_sums_for_target(num_list, target):
    for ind1, num1 in enumerate(num_list):
        for ind2, num2 in enumerate(num_list):
            if ind1 != ind2 and num1 + num2 == target:
                return True
    return False


lookback = 25
target = 0
num_list = xmas[0:lookback]
for i in range(lookback, len(xmas)):
    target = xmas[i]
    if two_sums_for_target(num_list, target):
        del num_list[0]
        num_list.append(target)
    else:
        print(f"Found invalid value {target} at index {i}.")
        break

# Part 2
def find_target_sum(xmas, target):
    for i in range(len(xmas)):
        for j in range(len(xmas)):
            if sum(xmas[i:j]) == target:
                print(f"Add numbers from {i} to {j}.")
                return min(xmas[i:j]) + max(xmas[i:j])


print(find_target_sum(xmas, target))