pos = 50
zeroCount = 0

with open("day1input.txt", 'r') as file:
    data = file.read().splitlines()

    print(data)

for i in data:
    turns = 0
    startPos = pos
    if i[0] == 'L':
        turns -= int(i[1:])
    else:
        turns += int(i[1:])
    print(f"{turns} turns")
    pos += turns
    if pos == 0:
        zeroCount += 1
        print("count increased")
    """elif pos < 0:
        if pos > -100:
            zeroCount += 1
        else:
            zeroCount += int(pos/-100)
    elif pos > 99:
        zeroCount += int(pos/100)"""
    print(f"position {pos}")
    while pos < 0:
        if startPos == 0:
            zeroCount += 0
        else:
            zeroCount += 1
        print("count increased")
        pos = 100 + pos
    while pos > 99:
        if startPos == 0:
            zeroCount += 0
        else:
            zeroCount += 1
        print("count increased")
        pos = pos - 100
    print(f"position {pos}")

print(zeroCount)