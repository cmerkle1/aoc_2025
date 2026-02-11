# Day 2 Part 1

# Open data file and split at commas
with open("sample.txt", 'r') as file:
    data = file.read().split(',')

# List to store valid combos
combo_list = []

# Split nums at the dash to make ranges
for i in data:
    start_num, end_num = i.split('-')
    start_num = int(start_num)
    end_num = int(end_num)

    for j in range(start_num, end_num + 1):
        k = str(j)

        # If numbers are even, check if first half == second half
        if len(k) % 2 == 0:
            half = len(k) // 2
            if k[half:] == k[:half]:
                combo_list.append(j)

print(sum(combo_list))
