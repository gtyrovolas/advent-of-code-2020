from itertools import chain


def parseRule(rule):
    id, nums = rule.split(": ")
    ranges = nums.split(" or ")
    
    res = []
    for r in ranges:
        st, en = map(int, r.split("-"))
        res.append(lambda x, st=st, en=en : st <= x and x <= en)
        # st, en have default values since they are mutable

    return (id, lambda x: any([r(x) for r in res.copy()]))



with open("16.in", "r") as f:
    rules, my_ticket, other_ticks = f.read().split("\n\n")

rules = rules.splitlines()
other_ticks = other_ticks.splitlines()[1:]
my_ticket = my_ticket.splitlines()[1]

rules = dict(map(parseRule, rules))
anyRule = lambda x : any([ r(x) for id, r in rules.items()])

other_ticks = [ list(map(int, tick.split(","))) for tick in other_ticks ]

sol = 0

for idx, tick in enumerate(other_ticks.copy()):
    for elem in tick:
        if not anyRule(elem):
            sol += elem

print(sol)