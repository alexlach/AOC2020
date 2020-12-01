import pandas as pd

num_df = pd.read_csv('01/input.csv', header=None)
num_col = num_df[0]

print("Finding two numbers that add up to 2020, then multiplying them together:")
for i in range(0, len(num_col)):
    for j in range(i + 1, len(num_col)):
        if num_col[i] + num_col[j] == 2020:
            print(num_col[i])
            print(num_col[j])
            print(num_col[i] * num_col[j])


print("Finding three numbers that add up to 2020, then multiplying them together:")
for i in range(0, len(num_col)):
    for j in range(i + 1, len(num_col)):
        for k in range(i + j + 1, len(num_col)):
            if num_col[i] + num_col[j] + num_col[k] == 2020:
                print(num_col[i])
                print(num_col[j])
                print(num_col[k])
                print(num_col[i] * num_col[j] * num_col[k])