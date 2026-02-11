# Day 2 Part 2
with open("sample.txt", 'r') as file:
    data = file.read().split(',')

# List to store valid combos
combo_list = []

# Split nums at the dash to make ranges, convert to int
for i in data:
    start_num, end_num = i.split('-')
    start_num = int(start_num)
    end_num = int(end_num)

    # Check each number in range
    for j in range(start_num, end_num + 1):
        num = str(j)
        num_length = len(num)

        # Find chunks of possible combos
        for chunk in range(1, num_length // 2 + 1):
            if num_length % chunk == 0:
                pattern = num[:chunk]
                repeat = num_length // chunk

                # If the pattern repeated * number of chunks == original, valid
                if pattern * repeat == num:
                    combo_list.append(j)
                    break

print(sum(combo_list))
