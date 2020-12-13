
file_in = open('02.in', "r")
lines = list(file_in.readlines())
count = 0

for line in lines:
    range_, char, passwd = line.split(" ")
    
    char = char[:-1]
    st, en = tuple(map(int, range_.split("-")))
    occurences = passwd.count(char)
    if st <= occurences <= en:
        count += 1

print(count)

