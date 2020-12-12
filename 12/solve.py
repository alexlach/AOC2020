import math

orders = open("12/input.txt").read().split("\n")

# Part 1
x_pos = 0
y_pos = 0
direction = 0  # east is 0, south is 90, north is 270
for order in orders:
    command = order[:1]
    value = int(order[1:])
    if command == "N":
        y_pos += value
    elif command == "S":
        y_pos -= value
    elif command == "E":
        x_pos += value
    elif command == "W":
        x_pos -= value
    elif command == "R":
        direction -= value
    elif command == "L":
        direction += value
    elif command == "F":
        x_pos = x_pos + value * math.cos(direction / 180 * math.pi)
        y_pos = y_pos + value * math.sin(direction / 180 * math.pi)
print(f"Manhattan distance from origin is {abs(x_pos) + abs(y_pos)}.")

# Part 2
ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = 1
for order in orders:
    command = order[:1]
    value = int(order[1:])
    if command == "N":
        waypoint_y += value
    elif command == "S":
        waypoint_y -= value
    elif command == "E":
        waypoint_x += value
    elif command == "W":
        waypoint_x -= value
    elif command == "R":
        for i in range(value // 90):
            waypoint_x, waypoint_y = waypoint_y, -waypoint_x
    elif command == "L":
        for i in range(value // 90):
            waypoint_x, waypoint_y = -waypoint_y, waypoint_x
    elif command == "F":
        ship_y += waypoint_y * value
        ship_x += waypoint_x * value
print(f"Manhattan distance from origin is {abs(ship_x) + abs(ship_y)}.")