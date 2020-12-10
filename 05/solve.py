seat_list = open('05/input.csv').read().split("\n")
print(seat_list[0])

def find_seat(text):
    lower_row = 0
    upper_row = 127
    for letter in text[:7]:
        if letter == "F": upper_row = (lower_row + upper_row) / 2
        elif letter == "B": lower_row = (lower_row + upper_row) / 2
    lower_col = 0
    upper_col = 7
    for letter in text[-3:]:
        if letter == "L": upper_col = (lower_col + upper_col) / 2
        elif letter == "R": lower_col = (lower_col + upper_col) / 2

    return int(round((lower_row + upper_row) / 2, 0)), int(round((lower_col + upper_col) / 2, 0))

# Part 1
seat_id_list = []
for seat in seat_list:
    row, col = find_seat(seat)
    current_id = row * 8 + col
    seat_id_list.append(row * 8 + col)
print(max(seat_id_list))

# Part 2
seat_id_list = sorted(seat_id_list)
offset_list = [x - y for x, y in zip(seat_id_list, seat_id_list[1:])]
my_seat_index = offset_list.index(min(offset_list))
print(seat_id_list[my_seat_index] + 1)