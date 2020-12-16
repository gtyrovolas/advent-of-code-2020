
with open("06.in", "r") as f:
    groups = f.read().split("\n\n")

def count(group):
    responses = group.splitlines()
    letter_sets = [ set([ c for c in res]) for res in responses]
    intersect_letters = set.intersection(*letter_sets)
    return len(intersect_letters)

ans = sum(map(count, groups))
print(ans)