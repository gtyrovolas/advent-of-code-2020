
with open("06.in", "r") as f:
    groups = f.read().split("\n\n")

def count(group):
    responses = group.splitlines()
    letters = set([c for res in responses for c in res])
    return len(letters)

ans = sum(map(count, groups))
print(ans)