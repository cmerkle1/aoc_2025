#AdeventOfCode2025
#Day 2
#Jason R Evarts

#import data and split on the , between each group
file1 = open('day2data.txt', 'r')
ids = file1.readline().split(',')
invalid_id_total = 0


#step through each grouping
for group in ids:
    group_split = group.split("-")
    start_id = group_split[0]
    finish_id = group_split[1]
    #debug print group
    #print("start_id: "+start_id+"\nfinish_id: "+finish_id+"\n")

#if both starting and end id are odd numbers of digits and match in length no invalid ID can be present
    if (len(start_id) == len(finish_id)) and len(start_id)%2==1:
        continue

# if grouping could have invalid ID check for an even split of digits
    for id in range(int(start_id),int(finish_id)+1):
        str_id = str(id)
        #length of the ID is even if modulo 2 returns zero
        if (len(str_id)%2)==0:
            #compare the two strings
            str_split= int(len(str_id)/2)
            #compare two halves of string to see if they match
            if str_id[0:str_split] == str_id[str_split:]:
                #they match, so they get added to the counter
                invalid_id_total = invalid_id_total + id
                print("invalid id: "+str_id+"\ninvalid id total: "+str(invalid_id_total)+"\n")

