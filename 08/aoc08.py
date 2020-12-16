

with open("08.in", "r") as f:
    instr_string = f.read().splitlines()

instructions = [(inst.split(" ")[0], int(inst.split(" ")[1])) for inst in instr_string] 

# simulation of the console:
curLine = 0
accum_value = 0
visited = [False] * len(instructions)

while not visited[curLine]:
    instr, num = instructions[curLine]
    visited[curLine] = True

    if instr == "jmp":
        curLine += num
    elif instr == "acc":
        accum_value += num
        curLine += 1
    elif instr == "nop":
        curLine += 1
    else:
        print("ERROR")

print(accum_value)