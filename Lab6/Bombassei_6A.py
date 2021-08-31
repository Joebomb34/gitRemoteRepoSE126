#Joe Bombassei
#SE126.02
#Lab 6A
#8/31/21

#Program Prompt: Store data to a list, prompt the user to enter the full lastname of the person they are searching for, and print the number of records the program went through before finding or not finding the file, reset the search count before entering the loop again, if the search was not found display that, if person was found display the full record of that person.

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

records = 0
binary_loop = 0
min = 0
max = records - 1
guess = int((min + max) / 2)

with open("Lab6/lab6A.txt") as csvfile:
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

answer = "y"
while (min < max and search != lname[guess]):

    search = input("Enter the full last name of the person you are looking for: ")
    
    binary_loop += 1 

    if search < lname[guess]:

        max = guess - 1

    else: 
            
        min = guess + 1
        
    guess = int((min + max) / 2)

if search == lname[guess]:

    print(search, " name was FOUND at index: ", guess)
    print("\t\t\t{1:10} \t {2:10} \t {3:10} \t {4:10}".format(guess, lname[guess], fname[guess], birth[guess]))
    
else:
    
    print("Your search for ", search, " has NOT BEEN FOUND.")
    print("cHeCk YoUr SpElLiNg and try again!")

print("\n\nBINARY SEARCH LOOPS: ", binary_loop)
answer = input("Would you like to do another search? [y/n]: ")