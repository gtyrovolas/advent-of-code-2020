from itertools import chain


def parseRule(rule):
    id, nums = rule.split(": ")
    ranges = nums.split(" or ")
    
    res = []
    for r in ranges:
        st, en = map(int, r.split("-"))
        res.append(lambda x, st=st, en=en : st <= x and x <= en)
        # st, en have default values since they are mutable

    return (id, lambda x, res=res: any([r(x) for r in res]))



with open("16.in", "r") as f:
    rules, my_ticket, other_ticks = f.read().split("\n\n")

rules = rules.splitlines()
other_ticks = other_ticks.splitlines()[1:]
my_ticket = my_ticket.splitlines()[1]

rules = dict(map(parseRule, rules))
labels = rules.keys()
anyRule = lambda x : any([ r(x) for id, r in rules.items()])

other_ticks = [ list(map(int, tick.split(","))) for tick in other_ticks ]

sol = 0

other_ticks = [tick for tick in other_ticks if all([anyRule(elem) for elem in tick])]
field_number = len(other_ticks[0])
fields = [sorted([tick[i] for tick in other_ticks]) for i in range(field_number)]

candidates = [dict.fromkeys(labels, True) for _ in range(field_number)]

for i, list_val in enumerate(fields):
    for num in list_val:
        for label, rule in rules.items():
            if not rule(num):
                candidates[i][label] = False


filtered = [[k for k, v in candidates[i].items() if v] for i in range(field_number)]
solution = ["" for _ in range (20)]

change = True

while change:
    change = False

    for i, f in enumerate(filtered):
        if len(f) == 1:
            change = True
            solution[i] = f[0]
            toRem = f[0]
            break
        
    for i in range(len(filtered)):
        filtered[i] = list(filter(lambda x : x != toRem, filtered[i]))

print(list(enumerate(solution)))
            
    


# 9 = route