import pandas as pd

pass_df = pd.read_csv('02/input.csv', header=None, sep=': | |-', names=["min", "max", "char", "pass"])

# Part One
valid_pass_count = 0
for row_index in range(len(pass_df)):
    letter_count = pass_df["pass"][row_index].count(pass_df["char"][row_index])
    if letter_count >= pass_df["min"][row_index] and letter_count <= pass_df["max"][row_index]:
        valid_pass_count += 1
print(f"There are {valid_pass_count} valid passwords.")

# Part Two
valid_pass_count = 0
for row_index in range(len(pass_df)):
    first_position = pass_df["pass"][row_index][pass_df["min"][row_index] - 1] == pass_df["char"][row_index]
    second_position = pass_df["pass"][row_index][pass_df["max"][row_index] - 1] == pass_df["char"][row_index]
    if (first_position and not second_position) or (not first_position and second_position):
        valid_pass_count += 1
print(f"There are {valid_pass_count} valid passwords.")