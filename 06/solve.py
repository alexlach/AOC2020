answer_list = open('06/input.txt').read().split("\n\n")

# Part 1
answer_list_combined = [answer.replace("\n", "") for answer in answer_list]
yes_count = 0
for answer in answer_list_combined:
    yes_count += len(''.join(set(answer)))
print(yes_count)

# Part 2
common_yes_count = 0
for answer in answer_list:
    person_list = answer.split("\n")
    common_answers = set(person_list[0])
    for person in person_list:
        common_answers = set(person).intersection(common_answers) 
    common_yes_count += len(common_answers)
print(common_yes_count)