
with open("04.in", "r") as f:
    inp = f.read()

passports = inp.split("\n\n")

sol = 0
for passport in passports:
    attrs = passport.split()
    fields = set([pair.split(":")[0] for pair in attrs])
    if len(fields) == 8:
        sol += 1
    elif "cid" not in fields and len(fields) == 7:  
        sol += 1
print(sol)