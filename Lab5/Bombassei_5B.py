#Joe Bombassei
#SE126.02
#Lab 5B
#8/23/21

#Program Prompt: Store data to a list, prompt the user to enter the full birthday of the person they are searching for, and print the number of records the program went through before finding or not finding the file, reset the search count before entering the loop again, if the search was not found display that, if person was found display the full record of that person.

#Variable Dictionary:
#lname - list lastname
#fname - list firstname
#birth - the birthdate held in list
#records - number of records in file
#search_count - holds count of how many records program sees through
#csvfile - lab5_updated.txt
#file - lab5_updated.txt after csv reader
#answer - answer to enter loop
#found - hold the search for location of data if the search has completed successfully and the item is found


#--MAIN CODE--

import csv

lname = []
fname = []
birth = []
age = []
tm = 8
td = 28
ty = 2021


records = 0
search_count = 0

with open("Lab5/lab5_updated.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        records += 1
        lname.append(rec[0])
        fname.append(rec[1])
        birth.append(rec[2])

print(" {0}\t\t{1:10}\t{2:10}\t{3:12}".format("INDEX", "Lastname", "Firstname", "Birthday"))
print("--------------------------------------------------------------")

for i in range(0, records):

    print("INDEX: {0}\t{1:10}\t{2:10}\t{3:12}".format(i, lname[i], fname[i], birth[i]))

print("\n\n\n")

for i in range(0, records):
    birth_L = birth[i].split("/")
    month = int(birth_L[0])
    day = int(birth_L[1])
    year = int(birth_L[2])
    
    if month > tm:
        age_ = ty - year - 1
        age.append(age_)

    elif month < tm:
        age_ = ty - year + 1

        age.append(age_)

    else:
        if day > td:
            age = ty
        age.append(age_)


answer = "y"

while answer == "y" or answer == "Y":

    found = -1

    search = input("Enter the full birthday of the person you are looking for: ")

    for i in range(0, records):
        search_count += 1

        if search == birth[i]:
            found = i

    print("\t\tSEARCH HAS COMPLETED.\n\n")

    if found >= 0:

        print("We have found who you are looking for {0}, at index number {1}".format(search, found))
        print("\nINDEX: {0}\t{1:10}\t{2:10}\t{3:12}\t{4:3}".format(found, lname[found], fname[found], birth[found], age[found]))

    else:
        print("\n\tYour search for {0} was NOT FOUND.".format(search))

    print("\nSEARCH COUNT: {0}".format(search_count))

    search_count = 0

    answer = input("Would you like to do another search? [y/n]: ")