import re

passport_list = open('04/input.txt').read().split("\n\n")
passport_list = [passport.replace("\n", " ") for passport in passport_list]

# Part 1
def eval_passport(passport):
    components = passport.split(" ")
    contained_components = [comp[:3] for comp in components]
    if "cid" in contained_components: contained_components.remove("cid")
    required_components = ["hgt", "eyr", "ecl", "hcl", "pid", "byr", "iyr"]
    return set(contained_components) == set(required_components)

valid_count = 0
for passport in passport_list:
    valid_count = valid_count + (1 if eval_passport(passport) else 0)
print(valid_count)

# Part 2
def eval_component(field, value):
    if field == "byr":
        if not (int(value) >= 1920 and int(value) <= 2002): return False
    if field == "iyr":
        if not (int(value) >= 2010 and int(value) <= 2020): return False
    if field == "eyr":
        if not (int(value) >= 2020 and int(value) <= 2030): return False
    if field == "hgt":
        if value[-2:] == "cm":
            if not (int(value[:-2]) >= 150 and int(value[:-2]) <= 193): return False
        elif value[-2:] == "in":
            if not (int(value[:-2]) >= 59 and int(value[:-2]) <= 76): return False
        else: return False
    if field == "hcl":
        if not (len(value) == 7 and value[0] == "#" and re.sub('[^a-f0-9]', "", value[1:]) == value[1:]):
            return False
    if field == "ecl":
        if not value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False
    if field == "pid":
        if not len(re.sub('[^0-9]', "", value)) == 9: return False
    return True

def eval_fields(passport):
    if not eval_passport(passport): return False
    components = passport.split(" ")

    for component in components:
        field, value = component.split(":")
        if not eval_component(field, value):
            return False
    return True

valid_count = 0
for passport in passport_list:
    valid_count = valid_count + (1 if eval_fields(passport) else 0)
print(valid_count)
