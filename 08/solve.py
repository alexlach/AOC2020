instructions = open("08/input.txt").read().split("\n")

# Part One
def execute_program(instructions):
    history = []
    accumulator = 0
    index = 0
    while index not in history and not index == len(instructions):
        history.append(index)
        cmd, val = instructions[index].split(" ")
        if cmd == "acc":
            accumulator += int(val)
            index += 1
        elif cmd == "nop":
            index += 1
        elif cmd == "jmp":
            index = index + int(val)
    return accumulator, index
print(execute_program(instructions)[0])

# Part Two
for i in range(len(instructions)):
    program = instructions[:]
    if program[i].startswith("nop"):
        program[i] = program[i].replace("nop", "jmp")
    elif program[i].startswith("jmp"):
        program[i] = program[i].replace("jmp", "nop")
    accum_value, term_ind = execute_program(program)
    if term_ind == len(instructions):
        print(accum_value)