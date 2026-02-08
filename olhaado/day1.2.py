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

    while turns != 0:
        if turns < 0:
            pos -= 1
            if pos == 0:
                zeroCount += 1
            if pos == -1:
                pos = 99
            turns += 1

        elif turns > 0:
            pos += 1
            if pos == 100:
                pos = 0
                zeroCount +=1
            turns -= 1
print(zeroCount)



""" scrapped this method because I was missing some passes
    pos += turns
    if pos == 0:
        zeroCount += 1
        print("count increased")
    print(f"position {pos}")
    while pos < 0:
        if startPos == 0 and turns > -99:
            zeroCount += 0
        else:
            zeroCount += 1
        print("count increased")
        pos = 100 + pos
    while pos > 99:
        zeroCount += 1
        print("count increased")
        pos = pos - 100
    print(f"final position {pos}")"""