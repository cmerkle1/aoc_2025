#AdeventOfCode2025
#Day 2 part B
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

    for id in range(int(start_id),int(finish_id)+1):
        str_id = str(id)
        #find even splits of the id where modulo equals zero by incrementing through from 2 to length
        for split_num in range(2,len(str_id)+1):
            if (len(str_id)%split_num)==0:
                #compare the two strings
                length_of_split = int(len(str_id)/split_num)
                str_splits= [str_id[i:i+length_of_split] for i in range(0,len(str_id),length_of_split)]
                #print(str_splits)
                #compare strings to see if they match
                invalid_id = False
                for split in str_splits:
                    if split == str_splits[0]:
                        invalid_id = True
                    else:
                        invalid_id = False
                        break
                if invalid_id:
                   #they match, so they get added to the counter
                   invalid_id_total = invalid_id_total + id
                   print("invalid id: "+str_id+"\ninvalid id total: "+str(invalid_id_total)+"\n")
                   break

