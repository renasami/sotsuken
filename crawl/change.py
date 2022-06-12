from csv import reader
import csv
with open('copied.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

newlist = []
for lis in list_of_rows:
    count = 0
    for index,item in enumerate(lis):
        if index != 0 and item != "":
            count += 1
    print(lis)
    if count != 0:
        newlist.append(lis)
print(newlist)
f = open('changed_data.csv', 'w')
writer = csv.writer(f).writerows(newlist)
f.close()