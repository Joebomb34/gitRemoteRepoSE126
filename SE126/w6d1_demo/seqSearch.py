#W6D1 - Sequential Search Introduction

#Utilizing binary.txt
#   FIELD0  FIELD1  FIELD2  FIELD3
#   ID num  Names   Ages    Color

#-MAIN PROGRAM CODE

import csv

id = []
name = []
age = []
color = []

records = 0

search_count = 0 #holds the count of how many search loops were used to find the name/item we are looking for (how many times we have gone through the sequential search loop)

with open("w6d1_demo/binary.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        id.append(rec[0])
        name.append(rec[1])
        age.append(rec[2])
        color.append(rec[3])

for i in range(0, records):
    print("INDEX: {0}\t{1:10}\t{2:10}\t{3:10}\t{4:10}".format(i, id[i], name[i], age[i], color[i]))

print("\n\n\n")

answer = "y"

while answer == "y" or answer == "Y":

    #SEQUENTIAL SEARCH: specified in order in searching: top to bottom (data in file, first record first, last record last)

    #gather the search item data - NECESSARY

    found = -1 #starting value -1 because index values are not negative, it will hold the search for location of data IF search is completed successfully and the item is found

    search = input("Enter the full lastname of the record you are looking for: ")

    for i in range(0, records):

        search_count += 1 #count the number of times the search loop is run
        
        #we are looking for lastname
        if search == name[i]:
            found = i

            #print("we have found who you are looking for: {0} at index #{1}".format(search, i))
            #print("INDEX: {0}\t{1:10}\t{2:10}\t{3:10}\t{4:10}".format(i, id[i], name[i], age[i], color[i]))

        #else:
            #print("Your search for {0} was NOT FOUND".format(search))

    print("\t\tSEARCH HAS COMPLETED.\n\n")

    if found >= 0:#we found it
        print("we have found who you are looking for: {0} at index #{1}".format(search, found))
        print("INDEX: {0}\t{1:10}\t{2:10}\t{3:10}\t{4:10}".format(found, id[found], name[found], age[found], color[found]))

    else:
        print("Your search for {0} was NOT FOUND".format(search))

    print("SEARCH COUNT: {0}".format(search_count))

    #reset search_count
    search_count = 0


    answer = input("Would you like to search again?: ")