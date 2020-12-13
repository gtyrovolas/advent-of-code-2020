
file_in = open("03.in", "r")
lines = file_in.read().splitlines()

relevant_chars = [ line[(3 * i) % len(line)] for i, line in enumerate(lines)]
ans = relevant_chars.count("#")

print(ans)