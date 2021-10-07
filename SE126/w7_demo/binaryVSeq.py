#W7D2 - Sequential Vs Binary Search

import csv

id_ = []
name = []
age = []
color = []
records = 0

with open("w7d1_demo/binary-1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        id_.append(rec[0])
        name.append(rec[1])
        age.append(rec[2])
        color.append(rec[3])

#Disconnected from file
print("{0:4}\t{1:15}\t{2:3}\t{3:10}".format("ID number", "NAME", "AGE", "COLOR"))

for i in range(0, records):
    print("{0:4}\t{1:15}\t{2:3}\t{3:10}".format(id_[i], name[i], age[i], color[i]))

#we are creaing a dual search system - we will ask a user for a search item, then we will run BOTH sequential as well as binary search to find the searched for item; both results will also print the search_loop count to compare the speed of each search type.

answer = "y"

while answer == "y": #main search loop - it allows the user to search multpile times

    #get search term
    search = input("Enter the NAME of the user you are looking for: ")

    #SEQUENTIAL SEARCH REVIEW
    #seq. search every potential vlaue (ie the entire list) is checked against the search item. it works on unordered lists as well as multiple returns of the search item (ie many people with the same last name)

    found = -1

    search_count = 0

    print("SEQUENTIAL SEARCH")

    for i in range(0, records):
        search_count += 1

        if search == name[i]:
            found = i

            #when searching for multpiles, you could put the print inside of this if OR you could append the i value to a new list

    if found != -1:
        print("Your search for {0} was FOUND in {1} loops!".format(search, search_count))
        print("{0:4}\t{1:15}\t{2:3}\t{3:10}".format("ID number", "NAME", "AGE", "COLOR"))
        print("{0:4}\t{1:15}\t{2:3}\t{3:10}".format(id_[found], name[found], str(age[found]), color[found]))

    else:
        print("Your search for {0} was NOT FOUND in {1} loops!".format(search, search_count))
        print("Please check your spelling and capitalization and try again.")


    #BINARY SEARCH REQUIRES ordered list - will split list searching into 2 sections, searched item will compared through the middle point
    print("BINARY SEARCH")
    min = 0
    max = records - 1
    guess = (min + max) // 2 #or int((min + max) / 2)

    search_count = 0

    while (min < max and search != name[guess]):
        search_count += 1

        if search < name[guess]:
            #search is greter than middle point, so we dont need anythng in lower half
            max = guess - 1

        else:
            #search is less than middle point, so we dont nedd anything above middle point
            min = guess + 1

        guess = (min + max) // 2

        if search != name[guess]:
            print("Your search for {0} was FOUND in {1} loops!".format(search, search_count))
            print("{0:4}\t{1:15}\t{2:3}\t{3:10}".format("ID number", "NAME", "AGE", "COLOR"))
            print("{0:4}\t{1:15}\t{2:3}\t{3:10}".format(id_[guess], name[guess], str(age[guess]), color[guess]))

        else:
            print("Your search for {0} was NOT FOUND in {1} loops!".format(search, search_count))
            print("Please check your spelling and capitalization and try again.")

        answer = input("Would you like to search again? [y/n]: ").lower()