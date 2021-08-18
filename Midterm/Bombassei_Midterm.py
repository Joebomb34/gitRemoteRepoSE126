#Joe Bombassei
#SE126.02
#Midterm
#8/17/21

#Program Prompt: List out people's first and last name, age, residence, or last name and residence, show the amount of people old enough to rent a car (print last name and yes or no, based on the age 25 or older), show people who will and won't need a co-signer for a rent (print last name and co signer yes or no) or exit based in a menu

#Variable Dictionary:
#records - number of records processed
#fname - first name based in list
#lname - lastname as it appears in list
#age - age or person
#residence - town which person live
#csvfile - midterm.txt
#file - csvfile after reader
#income - yearly income
#rent_car - rent car list
#cosign_list - based on needing $60K to not need a cosign
#rent - yes or no to rent a car based on persons age
#cosigner - yes or no based on list
#answer - true statment to get into loop
#user - input user gives when presented with the menu function
#drink - elgability to drink based on file
#drank - based on being 21 or older
#income_total - total income accross the file
#average - average income based on the file
#datetime - current datetime as GMT as default
#now() - default program function to update in real time
#current_time - real time based on datetime as a variable
#age1_list - list of ages as determined by rec[5] year
#age_1 - ages after rec[5] is subtracted from the current year
#current_time.year - current year in GMT as program default

#Function---
def menu():
    '''shows menu to user, gets the users choice, makes sure user input is valid, and returns what the user input was back to the userreturns'''
    print("\t\tMENU")
    print("1. Print Full Record")
    print("2. Print Last name, Elgibility to rent a car")
    print("3. Print Last name and if person would need a cosigner on a lease based on minimum $60,000 for no co-signer")
    print("4. Print the number of records in the file")
    print("5. Print Last Name, Elgability of Drinking")
    print("6. Print average income of the file")
    print("7. Print Last Name Age based on Current Year")
    print("8. EXIT")

    #gete user's choice
    user = input("\tEnter your menu selection [1-8]: ")

    #make sure user gives you a valid value
    while user != "1" and user != "2" and user != "3" and user != "4" and user != "5" and user != "6" and user != "7" and user != "8":

        #ERROR TRAP LOOP!
        print("\t\t***ERROR ERROR***")
        user = input("\tEnter your menu selection [1-8]: ")

    return user

def deuces():
    '''Goodbye message'''
    print("Thanks for using my program, Have a nice day!")

#Main Code---

import csv
#imports current datetime from greewich mean time as default
import datetime
#applies datetime to varriable current_time
current_time = datetime.datetime.now()

records = 0
income_total = 0

fname = []
lname = []
age = []
residence = []
income = []
year = []
rent_car = []
cosign_list = []
drank = []
age1_list = []


with open("Midterm/midterm.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        records += 1
        fname.append(rec[0])
        lname.append(rec[1])
        age.append(int(rec[2]))
        residence.append(rec[3])
        income.append(int(rec[4]))
        year.append(int(rec[5]))

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

        if rec[2] >= "21":
            drink = "YES"

        if rec[2] < "21":
            drink = "NO"

        drank.append(drink)


answer = "y"

while answer == "y".lower():
    user = menu()

    if user == "1":
        print("-----------------------------------------------------------------------------------------------")
        print("{0:10}\t{1:10}\t{2:3}\t{3:16}\t {4:6}\t\t{5:5}".format("FIRST", "LAST", "AGE", "RESIDENCE", "INCOME", "Birth Year"))
        print("-----------------------------------------------------------------------------------------------")

        for i in range(0,records):
            print("{0:10}\t{1:10}\t{2:3}\t{3:16}\t${4:6}\t\t{5:5}".format(fname[i], lname[i], age[i], residence[i], income[i], year[i]))

    elif user == "2":
        print("-----------------------------------------")
        print("{0:10}\t{1:3}\t{2:5}".format("LAST NAME", "AGE", "CAR RENTAL"))
        print("-----------------------------------------")

        for i in range(0, records):
            print("{0:10}\t{1:3}\t{2:5}".format(lname[i], age[i], rent_car[i]))

    elif user == "3":
        print("------------------------------------------")
        print("{0:10}\t{1:7}\t\t{2:5}".format("LAST NAME", "INCOME", "CO-SIGNER"))
        print("------------------------------------------")

        for i in range(0, records):
            print("{0:10}\t${1:7}\t{2:5}".format(lname[i], income[i], cosign_list[i]))

    elif user == "4":
        print("-----------------")
        print("NUMBER OF RECORDS")
        print("-----------------")

        print("{0:3}".format(records))

    elif user == "5":
        print("------------------------------------------------------------------")
        print("{0:10}\t   {1:6}{2:5}".format("LAST NAME", "AGE", "Drinking Elgability"))
        print("------------------------------------------------------------------")

        for i in range(0, records):
            print("{0:10}\t{1:6}\t\t{2:5}".format(lname[i], age[i], drank[i]))

    elif user == "6":
        print("------------------------")
        print("{0:7}".format("AVERAGE INCOME"))
        print("------------------------")

        for i in range(0, records):
            income_total += income[i]

        average = income_total / records

        print("${0:7.2f}".format(average))

    elif user == "7":
        print("--------------------")
        print("{0:10}\t{1:3}".format("LAST NAME", "AGE"))
        print("--------------------")

        for i in range(0, records):

            #takes current year and subtracts from the rec[5] list to determine persons age
            age_1 = current_time.year - int(year[i])
            
            age1_list.append(int(age_1))

            print("{0:10}\t{1:3}".format(lname[i], age1_list[i]))
        
        

    elif user == "8":
        print("\t\tE X I T I N G . . .")
        answer = "x"


    if user != "8":#this gives people who choose EXIT are not asked if they would like to return to the loop
        answer = input("\t\tWould you like to see the menu again? [y/n]: ").lower()

        while answer != "n" and answer != "y":
            answer = input("Would you like to se the menu again?[y/n]: ").lower()
            answer = answer.lower()


deuces()