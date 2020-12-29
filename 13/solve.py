time, busses = open("13/input.txt").read().split("\n")
time = int(time)
bus_list = [(ind, int(bus)) for ind, bus in enumerate(busses.split(",")) if bus != 'x']


# Part One
wait_time_for_bus = {}
for bus in bus_list:
    wait_time_for_bus[bus[1]] = abs(time % bus[1] - bus[1])
best_bus = min(wait_time_for_bus, key=wait_time_for_bus.get)
print(best_bus * wait_time_for_bus.get(best_bus))


# Part Two
time = 0
product = 1
for bus_item in bus_list:
    offset, bus = bus_item
    while not (time + offset) % bus == 0:
        time += product
    product = product * bus
    print(f"Offset: {offset}, Product: {product}, Time: {time}")