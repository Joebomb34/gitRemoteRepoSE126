#Joe Bombassei
#SE126
#Lab2A
#7/28/21

#PROGRAM PROMPT: Determine the number of capacity of the rooms and display the rooms that are over capacity, and the number of people that need to be removed.

#VARIABLE DICTIONARY
#total_rooms = total number of rooms processed
#rooms_over = number of rooms over capacity
#csvfile = lab2a.csv
#file = csvfile after reader
#room = the name of the room
#capacity = the maximum capacity of the room
#people = number of people planning to be in the room
#over = amount of people that need to leave

# MAIN CODE

import csv

total_rooms = 0
rooms_over = 0

#Header
print("\t\tROOM\t\t MAX\tPEOPLE\tREMOVE")
print("\t-------------------------------------------------")

with open("Lab2/lab2a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        total_rooms += 1

        room = rec[0]
        capacity = int(rec[1])
        people = int(rec[2])

        if int(rec[2]) > int(rec[1]):

            rooms_over += 1

            over = int(rec[2]) - int(rec[1])
            
            print("\t{0:20}\t{1:4}\t{2:4}\t{3:4}".format(room,capacity,people,over))

print("\nThere were {0} rooms processed.".format(total_rooms))
print("There are {0} rooms over capacity.".format(rooms_over))
input("\nPress any key to continue . . .")