# Day 1 Part 1

file_path = 'sample.txt'

# Create a list from combos file, replace L and R with directions - +
with open(file_path, 'r') as file:
    num_list = [
        int(line.rstrip('\n').replace('R', '').replace('L', '-')) for line in file
        ]

# Set a counter to determine the number of times 0 is passed
zero_counter = 0

# Position starts at 50
previous = 50

for num in num_list:
    # Sets place factoring in the dial movement
    previous = (previous + num) % 100

    if previous == 0:
        zero_counter += 1

print(zero_counter)
