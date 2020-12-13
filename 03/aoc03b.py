
file_in = open("03.in", "r")
lines = file_in.read().splitlines()

steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
ans = 1

for hor_step, ver_step in steps:
    relevant_chars = [ line[(hor_step * i) % len(line)] for i, line in enumerate(lines[::ver_step])]
    ans *= relevant_chars.count("#")

print(ans)