
with open("09.in", "r") as f:
    numbers = list(map(int, f.read().splitlines()))


def find_invalid():

    cur = numbers[:25]
    for num in numbers[25:]:
        poss = [ cur[i] + cur[j] for i in range(25) for j in range(i + 1, 25) ]
        if num not in poss:
            return num
        cur.pop(0)
        cur.append(num)

target = find_invalid()
print(target)

left, right = 0, 0
total = 0

while(total != target):
    if total < target:
        total += numbers[right]
        right += 1
    elif total > target:
        total -= numbers[left]
        left += 1

print(min(numbers[left:right]) + max(numbers[left:right]))