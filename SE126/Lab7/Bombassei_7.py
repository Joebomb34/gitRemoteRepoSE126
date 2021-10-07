#Joe Bombassei
#SE126.02
#Lab 7
#9/8/21

#PROGRAM PROMPT: Program uses a menu function to search through the file. Program uses binary search for choices 1 and 2 and precedes with bubble sort. For options 3 and 4 program uses sequential search.

#VARRIABLE DICTIONARY:
#clear() - clear screen function
#menu() - display menu function
#choice - users choice from menu
#swap() - function for bubble sorting
#reenter() - function to ask user if they want to get back into the loop
#goodbye() - goodbye message function
#idCode - screen names of charectors if they had socialmedia
#lname - last name
#fname - first name
#age - charectors ages
#allegiance - allegiance of charectors
#records - number of records in the file
#csvfile - GOT_bubble_sort_7.txt
#file - csvfile after reader
#answer - used to enter the loop
#search - users input of who to search for
#min - minimum number of records
#max - maximum number of records
#guess - programs search through binary search
#found - found records through sequential search


# import only system from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear():  

    # for windows  
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')  
    else:  
        _ = system('clear')

def menu():
    '''shows menu, gets choice, ensures choice is valid, returns choice to user'''
    print("\t\tMENU")
    print("1. Search by FIRST NAME")
    print("2. Search by ID CODE")
    print("3. Search by LAST NAME")
    print("4. Search by ALLEGIANCE")
    print("5. EXIT")

    #gete user's choice
    choice = input("\tEnter your menu selection [1-5]: ")

        #make sure user gives you a valid value
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":

        #ERROR TRAP LOOP!
        print("\t\t***ERROR ERROR***")
        choice = input("\tEnter your menu selection [1-5]: ")

    return choice

def swap(listName, index):

    #this function handles the swapping of values for bubble sort
    temp_var = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp_var

def reenter():
    answer = input("Would you like to search again? [y/n]: ").lower()
    while answer != "n" and answer != "y":
        answer = reenter()
        answer = answer.lower()

    clear()

    return answer

def goodbye():
    '''prints goodbye message'''
    print("\n\n\t'Winter is comming'.\nThanks for using the program. GOODBYE :]")


import csv

idCode = []
lname = []
fname = []
age = []
allegiance = []

records = 0


with open("Lab7/GOT_bubble_sort_7.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1
        idCode.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        age.append(rec[3])
        allegiance.append(rec[4])

print(" {0}\t\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format("INDEX", "ID Code", "Lastname", "Firstname", "Age", "Allegiance"))
print("--------------------------------------------------------------------------------------------------------")

for i in range(0, records):

    print("INDEX: {0}\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format(i, idCode[i], lname[i], fname[i], age[i], allegiance[i]))

print("\n\n\n")

answer = "y"

while answer == "y" or answer == "Y":

    choice = menu()

    if choice == "1":

        for i in range(0, records - 1):

            for index in range(0, records - 1):

                if fname[index] > fname[index + 1]:

                    swap(fname, index)
                    swap(idCode, index)
                    swap(lname, index)
                    swap(age, index)
                    swap(allegiance, index)
             

        search = input("Enter the full first name of the person you are looking for: ")

        min = 0 

        max = records - 1 

        guess = int((min + max) / 2) 
        while (min < max and search != fname[guess]):
    
            if search < fname[guess]: 

                max = guess - 1
        
            else: 

                min = guess + 1
       
            guess = int((min + max) / 2)
    

        if search == fname[guess]:

            print(search, " name was FOUND at index: ", guess)
            print(" {0}\t\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format("INDEX", "ID Code", "Lastname", "Firstname", "ID", "Allegiance"))
            print("INDEX: {0}\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format(guess, idCode[guess], lname[guess], fname[guess], age[guess], allegiance[guess]))
    
        else: 
    
            print("Your search for ", search, " has NOT BEEN FOUND.")
            print("cHeCk YoUr SpElLiNg and try again!")

    elif choice == "2":

        for i in range(0, records - 1):

            for index in range(0, records - 1):

                if fname[index] > fname[index + 1]:

                    swap(fname, index)
                    swap(idCode, index)
                    swap(lname, index)
                    swap(age, index)
                    swap(allegiance, index)

        search = input("Enter the ID CODE of the person you are looking for: ")

        min = 0 

        max = records - 1 

        guess = int((min + max) / 2) 
        while (min < max and search != idCode[guess]):
    
            if search < idCode[guess]: 

                max = guess - 1
        
            else: 

                min = guess + 1
       
            guess = int((min + max) / 2)
    
        if search == idCode[guess]:

            print(search, " name was FOUND at index: ", guess)
            print(" {0}\t\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format("INDEX", "ID Code", "Lastname", "Firstname", "ID", "Allegiance"))
            print("INDEX: {0}\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format(guess, idCode[guess], lname[guess], fname[guess], age[guess], allegiance[guess]))
    
        else: 
    
            print("Your search for ", search, " has NOT BEEN FOUND.")
            print("Check the number you entered is correct!")

    elif choice == "3":

        found = -1

        search = input("Enter the full LAST NAME of the person you are looking for: ")

        print("\n {0}\t\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format("INDEX", "ID Code", "Lastname", "Firstname", "ID", "Allegiance"))

        for i in range(0, records):
            
            if search == lname[i]:
                found = i
                if found >= 0:
                    print("INDEX: {0}\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format(found, idCode[found], lname[found], fname[found], age[found], allegiance[found]))
                #print("\nWe have found who you are looking for {0}, at index number {1}".format(search, found))

        
            
            

                else:
                    print("\n\tYour search for {0} was NOT FOUND.".format(search))


    elif choice == "4":

        found = -1

        search = input("Enter the full ALLEGIANCE of the person you are looking for: ")

        print(" {0}\t\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format("INDEX", "ID Code", "Lastname", "Firstname", "ID", "Allegiance"))

        for i in range(0, records):
            
            if search == allegiance[i]:
                found = i
            if found >= 0:
                print("INDEX: {0}\t{1:15}\t{2:15}\t{3:12}\t{4:3}\t{5:35}".format(found, idCode[found], lname[found], fname[found], age[found], allegiance[found]))
                #print("\nWe have found who you are looking for {0}, at index number {1}".format(search, found))

        #print("\t\tSEARCH HAS COMPLETED.\n\n")
            else:
                print("\n\tYour search for {0} was NOT FOUND.".format(search))

    elif choice == "5":
        print("\t\tE X I T I N G . . .")
        answer = "n"

      

goodbye()