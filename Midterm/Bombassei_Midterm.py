#Joe Bombassei
#SE126.02
#Midterm
#8/16/21

#Program Prompt: List out people's first and last name, age, residence, or last name and residence, show the amount of people old enough to rent a car (print last name and yes or no, based on the age 25 or older), show people who will and won't need a co-signer for a rent (print last name and co signer yes or no) or exit based in a menu

#Variable Dictionary:
#records - number of records processed
#fname - first name based in list
#lname - lastname as it appears in list
#age - age or person
#residence - town which person live
#csvfile - midterm.txt
#file - csvfile after reader

#Function---
def menu():
    '''shows menu to user, gets the users choice, makes sure user input is valid, and returns what the user input was back to the userreturns'''
    print("\t\tMENU")
    print("1. Print Full Record")
    print("2. Print Last name, Elgibility to rent a car")
    print("3. Print Last name and if person would need a cosigner on a lease based on minimum $60,000 for no co-signer")
    print("4. Print the number of records in the file")
    print("5. EXIT")

    #gete user's choice
    user = input("\tEnter your menu selection [1-5]: ")

    #make sure user gives you a valid value
    while user != "1" and user != "2" and user != "3" and user != "4" and user != "5":

        #ERROR TRAP LOOP!
        print("\t\t***ERROR ERROR***")
        user = input("\tEnter your menu selection [1-5]: ")

    return user

def goodbye():
    '''Goodbye message'''
    print("Thanks for using my program, Have a nice day!")

#Main Code---

import csv

records = 0

fname = []
lname = []
age = []
residence = []
income = []
rent_car = []
cosign_list = []


with open("Midterm/midterm.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        records += 1
        fname.append(rec[0])
        lname.append(rec[1])
        age.append(int(rec[2]))
        residence.append(rec[3])
        income.append(int(rec[4]))

        if rec[2] < "25":
            rent = "NO"

        elif rec[2] >= "25":
            rent = "YES"

        rent_car.append(rent)

        if rec[4] >= "60000":
            cosigner = "NO"

        elif rec[4] < "60000":
            cosigner = "YES"

        cosign_list.append(cosigner)

answer = "y"

while answer == "y".lower():
    user = menu()

    if user == "1":
        print("------------------------------------------------------------------------------------------")
        print("{0:10}\t{1:10}\t{2:3}\t{3:16}\t {4:6}".format("FIRST", "LAST", "AGE", "RESIDENCE", "INCOME"))
        print("------------------------------------------------------------------------------------------")

        for i in range(0,records):
            print("{0:10}\t{1:10}\t{2:3}\t{3:16}\t${4:6}".format(fname[i], lname[i], age[i], residence[i], income[i]))

    elif user == "2":
        print("-----------------------------------------")
        print("{0:10}\t{1:5}".format("LAST NAME", "CAR RENTAL"))
        print("-----------------------------------------")

        for i in range(0, records):
            print("{0:10}\t{1:5}".format(lname[i], rent_car[i]))

    elif user == "3":
        print("------------------------------------------")
        print("{0:10}\t{1:6}\t\t{2:5}".format("LAST NAME", "INCOME", "CO-SIGNER"))
        print("------------------------------------------")

        for i in range(0, records):
            print("{0:10}\t${1:6}\t\t{2:5}".format(lname[i], income[i], cosign_list[i]))

    elif user == "4":
        print("-----------------")
        print("NUMBER OF RECORDS")
        print("-----------------")

        print("{0:3}".format(records))
        

    elif user == "5":
        print("\t\tE X I T I N G . . .")
        answer = "x"


    if user != "5":#this gives people who choose EXIT are not asked if they would like to return to the loop
        answer = input("\t\tWould you like to re-enter the loop? [y/n]: ").lower()

        while answer != "n" and answer != "y":
            answer = input("Would you like to re-enter the loop?[y/n]: ").lower()
            answer = answer.lower()


goodbye()