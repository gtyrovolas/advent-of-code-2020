
def getSeatNumber(input_str):
    getVer = lambda x : int( "".join(['0' if c == 'F' else '1' for c in x]), 2 )
    getHor = lambda x : int( "".join(['0' if c == 'L' else '1' for c in x]), 2 )
    return 8 * getVer(input_str[: -3]) + getHor(input_str[-3 :])


with open("05.in", "r") as f:
    seats = f.read().splitlines()

seatNums = set(map(getSeatNumber, seats))

for row in range(128):
    print("Row ", row, end=" ")
    for col in range(8):
        if 8 * row + col in seatNums:
            print("X", end=" ")
        else:
            print("*", end=" ")
    print("")
