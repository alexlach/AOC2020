stair_count = 4
step_options = [1, 2]
# how many unique routes are there to get to the top of the stairs?
# there are n stairs, and you can take 1 or two steps at a time
routes = {0: 1}
for step in range(1, stair_count + 1):
    routes[step] = routes.get(step - 1, 0) + routes.get(step - 2, 0)
print(routes.get(max(routes.keys())))