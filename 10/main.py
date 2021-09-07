

with open("10.in", "r") as f:
    adapters = list(map(int, f.readlines()))
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

one_diff, three_diff = 0, 0

for prev, jolt in zip(adapters, adapters[1:]):
    if jolt - prev == 1:
        one_diff += 1
    elif jolt - prev == 3:
        three_diff += 1

dp = [0] * (max(adapters) + 1)
dp[0] = 1

print(one_diff * three_diff)

for i in adapters[1:]:
    dp[i] = sum(dp[max(i - 3, 0) : i])

print(dp[-1])