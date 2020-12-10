bag_rules = open("07/input.txt").read().replace(" bags", "").replace(" bag", "")
bag_rules = bag_rules.replace(" contain", ",").replace(".", "").split("\n")

# Build a DAG where parent = a bag color; child = bag color contained within that parent
bag_map = {}
for rule in bag_rules:
    parts = rule.split(", ")
    parent_item = parts.pop(0)
    contained_bags = {}
    for child in parts:
        count, bag = child.split(" ", 1)
        contained_bags[bag] = count
    bag_map[parent_item] = contained_bags

# Reverse the DAG where parent = a bag color; child = bag color that can hold that parent bag
bag_inv = {}
for key, val in bag_map.items():
    for subkey, subval in val.items():
        bag_inv.setdefault(subkey, {})
        bag_inv[subkey][key] = subval


def get_bags_containing(bag_inv, color, bags_containing=set()):
    bags_containing.add(color)
    if color in bag_inv:
        for inner_bag in bag_inv.pop(color):
            bags_containing = get_bags_containing(bag_inv, inner_bag, bags_containing)
    return bags_containing


def count_bags_inside(bag_map, color):
    to_add = 1
    for inner_bag in bag_map.get(color):
        if inner_bag != "other":
            to_add += (int(bag_map.get(color).get(inner_bag))) * count_bags_inside(
                bag_map, inner_bag
            )
    return to_add


print(len(get_bags_containing(bag_inv, "shiny gold")) - 1)  # Part One
print(count_bags_inside(bag_map, "shiny gold") - 1)  # Part Two
