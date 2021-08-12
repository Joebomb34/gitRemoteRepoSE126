#Joe Bombassei
#SE126.02
#Lab 4B
#8/12/21

#PROGRAM PROMPT: Build a program that users select from a menu what they want to see from the imported txt file.

#VARIABLE DICTIONARY:

#FUNCTIONS
def menu():
    '''shows menu, gets choice, ensures choice is valid, returns choice to user'''
    print("\t\tmenu")
    print("1. Print all First, Last, Nicknames")
    print("2. Print Last names with House Allegiance and Motto")
    print("3. Print Full Records")
    print("4. EXIT")

    #gete user's choice
    choice = input("\tEnter your menu selection [1-4]: ")

    #make sure user gives you a valid value
    while choice != "1" and choice != "2" and choice != "3" and choice != "4":

        #ERROR TRAP LOOP!
        print("\t\t***ERROR ERROR***")
        choice = input("\tEnter your menu selection [1-4]: ")

    return choice

def goodbye():
    '''prints goodbye message'''
    print("\n\n\tThanks for using the program. GOODBYE :]")

#MAIN CODE

import csv

records = 0
fname = []
lname = []
age = []
nickname = []
allegiance = []
motto_list = []

with open("Lab4/lab4A_GOT_NEW.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        fname.append(rec[0])
        lname.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        allegiance.append(rec[4])

        if rec[4] == "House Stark":
            motto = "Winter is Coming."

        elif rec[4] == "House Baratheon":
            motto = "Ours is the fury."

        elif rec[4] == "House Tully":
            motto = "Family. Duty. Honor."

        elif rec[4] == "Night's Watch":
            motto = "And now my watch begins"

        elif rec[4] == "House Lannister":
            motto = "Hear me roar!"

        elif rec[4] == "House Targaryen":
            motto = "Fire & Blood"

        motto_list.append(motto)

answer = "y"

while answer == "y":
    choice = menu()

    if choice == "1":
        print("--------------------------------------------------------------------------------------------------------------")
        print("{0:15}\t{1:15}\t{2:18}".format("FIRST", "LAST", "NICKNAME"))
        print("--------------------------------------------------------------------------------------------------------------")

        for i in range(0, records):
            print("{0:15}\t{1:15}\t{2:18}".format(fname[i], lname[i], nickname[i]))

    elif choice == "2":
        print("--------------------------------------------------------------------------------------------------------------")
        print("{0:15}\t{1:18}\t{2:27}".format("LAST", "ALLEGIANCE", "MOTTO"))
        print("--------------------------------------------------------------------------------------------------------------")

        for i in range(0, records):
            print("{0:15}\t{1:18}\t{2:27}".format(lname[i], allegiance[i], motto_list[i]))


    elif choice == "3":
        print("--------------------------------------------------------------------------------------------------------------")
        print("{0:15}\t{1:15}\t{2:3}\t{3:18}\t{4:18}\t{5:27}".format("FIRST", "LAST", "AGE", "NICKNAME", "ALLEGIANCE", "MOTTO"))
        print("--------------------------------------------------------------------------------------------------------------")

        for i in range(0, records):
            print("{0:15}\t{1:15}\t{2:3}\t{3:18}\t{4:18}\t{5:27}".format(fname[i], lname[i], age[i], nickname[i], allegiance[i], motto_list[i]))

    elif choice == "4":
        print("\t\tE X I T I N G . . .")
        #in order to exit, we must break out of the loop ie make the loop condition false
        answer = "x"

    #option to re-enter loop; opportunity to revalue the loop condition key (answer)
    if choice != "4":#this gives people who choose EXIT are not asked if they would like to return to the loop
        answer = input("\t\tWould you like to re-enter the loop? [y/n]: ")

        while answer != "n" and answer != "y":
            answer = input("Would you like to re-enter the loop?[y/n]: ")
            answer = answer.lower()

goodbye()


