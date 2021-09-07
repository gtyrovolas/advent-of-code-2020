from collections import defaultdict
import re

def go_up(par):
    if ans[par]:
        return
    ans[par] = True
    for d in dads[par]:
        go_up(d)
    return


def go_down(cur):
    ans = 1
    for c, num in rules[cur]:
        ans += num * go_down(c)
    return ans 

rules = {}
dads = defaultdict(list)

with open("07.in", "r") as f:
    for line in f:
        parent, children = line.split(" contain ")
        
        parent = parent.removesuffix(" bags")
        
        p = re.compile(" bag, | bags, ")
        children = p.split(children)
        children = [ (" ".join(c.split()[1:3]), int(c.split()[0])) for c in children if c.split()[0] != "no"]

        for c, _ in children:
            dads[c].append(parent)
        
        rules[parent] = children

ans = {k: False for k in rules.keys()}

for parent, children in rules.items():
    for c, _ in children:
        if c == "shiny gold":
            go_up(parent)



# print(ans)

print(len([x for x in ans.values() if x]))
print(go_down("shiny gold") - 1)
