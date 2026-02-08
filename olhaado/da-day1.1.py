pos = 50
zeroCount = 0

with open("day1input.txt", 'r') as file:
    data = file.read().splitlines()

    print(data)

for i in data:
    turns = 0
    if i[0] == 'L':
        turns -= int(i[1:])
    else:
        turns += int(i[1:])
    print(f"{turns} turns")
    pos += turns
    while pos < 0:
        pos = 100 + pos
    while pos > 99:
        pos = pos - 100
    print(f"position {pos}")
    if pos == 0:
        zeroCount += 1
print(zeroCount)
