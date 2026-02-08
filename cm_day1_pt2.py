# Day 1 Part 2

file_path = 'sample.txt'

with open(file_path, 'r') as file:
    num_list = [
        int(line.rstrip('\n').replace('R', '').replace('L', '-')) for line in file
        ]

# Dial still starts at 50
position = 50

# Counter keeps track of passes over 0
zero_counter = 0

for num in num_list:
    if num > 0:
        step = 1  # Moving right
    else:
        step = -1  # Moving left

    # Number of times the dial moves to get to the new number
    movements = abs(num)

    # Check position each time for the number of movements to see if 0 is passed
    for i in range(movements):
        # Wraps around dial accounting for stopping point at 99
        position = (position + step) % 100

        # If dial points to 0, add to counter
        if position == 0:
            zero_counter += 1

print(zero_counter)
