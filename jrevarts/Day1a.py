#AdeventOfCode2025
#Day 1
#Jason R Evarts

file1 = open('day1data.txt', 'r')
count = 0
current_num = 50
rotation_dir = ''
rotation_num = 0

while True:

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    rotation_num = int(line[1:])
    rotation_dir = str(line[0])

    #rotate the dial
    if rotation_dir == "L":
        current_num = current_num - rotation_num
    elif rotation_dir == "R":
        current_num = current_num + rotation_num
    else:
        print("Error in Rotation Dir")

    #solve for dial going past 0 in either direction
    if current_num != 0:
        while current_num>99 or current_num<0:
            #process number over 100
            if current_num>99:
                current_num -= 100
            #process number under 0
            elif current_num<0:
                current_num+=100
            else:
                print("Error in current_num outside bounds")
    if current_num == 0:
        count+=1
    print("current_num = "+str(current_num)+"\ncount = "+str(count)+"\n\n")


