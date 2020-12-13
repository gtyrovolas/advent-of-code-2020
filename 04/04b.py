import re

rules = {
    "byr" : lambda x : 1920 <= int(x) <= 2002,
    "iyr" : lambda x : 2010 <= int(x) <= 2020,
    "eyr" : lambda x : 2020 <= int(x) <= 2030,
    "hgt" : lambda x : x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193 or x[-2:] == "in" and 59 <= int(x[:-2]) <= 76,
    "hcl" : lambda x : re.match(r"^#[0-9a-f]{6}$", x),
    "ecl" : lambda x : x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid" : lambda x : re.match(r"^[0-9]{9}$", x)
}
# code inspired by Dionysis Zindros

def validate(attrs):
    for k, v in attrs.items():
        if not rules[k](v):
            return False
    return True

with open("04.in", "r") as f:
    inp = f.read()

passports = inp.split("\n\n")

sol = 0
for passport in passports:
    attrs = passport.split()
    attrs = [tuple(pair.split(":")) for pair in attrs]
    attrs = dict(attrs)
    attrs.pop("cid", None)
    if len(attrs) == 7:
        if validate(attrs):
            sol += 1

print(sol)