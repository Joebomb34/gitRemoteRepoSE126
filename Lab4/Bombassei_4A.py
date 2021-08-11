#Joe Bombassei
#SE126.02
#Lab 4A
#8/11/21

#Program Prompt: Process the text file to a list, and reprocess the file to print the House motto, print each house fully with motto, total number of people in the list, average age, and tallies for each alliance.

#Variable Dictionary:

#Main Code------

import csv

records = 0
age_total = 0
house_stark = 0
nights_watch = 0
house_tully = 0
house_lannister = 0
house_baratheon = 0
house_targaryen = 0

fname = []
lname = []
age = []
nickname = []
allegiance = []
motto_list = []

avgage = []

with open("Lab4/lab4A_GOT_NEW.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        fname.append(rec[0])
        lname.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        allegiance.append(rec[4])


# for i in range(0, records): nooooooooooooooooooo
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

        if rec[4] == "House Stark":
            house_stark += 1

        elif rec[4] == "House Baratheon":
            house_baratheon += 1
        
        elif rec[4] == "House Tully":
            house_tully += 1

        elif rec[4] == "Night's Watch":
            nights_watch += 1

        elif rec[4] == "House Lannister":
            house_lannister += 1

        elif rec[4] == "House Targaryen":
            house_targaryen += 1

        
            

   

print("---ORIGINAL FILE DATA----------------------------------------------------")
print("{0:15}\t{1:15}\t{2:3}\t{3:10}\t{4:5}".format("FIRST", "LAST", "AGE", "NICKNAME", "ALLEGIANCE"))
print("-------------------------------------------------------------------------")
for i in range(0, records):
    print("{0:15}\t{1:10}\t{2:3}\t{3:18}\t{4:5}".format(fname[i], lname[i], age[i], nickname[i], allegiance[i]))

print("--------------------------------")
print("{0:27}".format("HOUSE MOTTO"))
print("--------------------------------")

for i in range(0, records):
    print("{0:27}".format(motto_list[i]))

print("--------------------------------------------------------------------------------------------------------------")
print("{0:15}\t{1:15}\t{2:3}\t{3:18}\t{4:18}\t{5:27}".format("FIRST", "LAST", "AGE", "NICKNAME", "ALLEGIANCE", "MOTTO"))
print("--------------------------------------------------------------------------------------------------------------")

for i in range(0, records):
    print("{0:15}\t{1:15}\t{2:3}\t{3:18}\t{4:18}\t{5:27}".format(fname[i], lname[i], age[i], nickname[i], allegiance[i], motto_list[i]))

print("-----------------")
print("NUMBER OF RECORDS")
print("-----------------")

print("{0:3}".format(records))

print("-----------")
print("AVERAGE AGE")
print("-----------")

for i in range(0, records):

    age_total += age[i]

average = age_total / records
print("{0:3.2f}".format(average))


print("--------------------------------")
print("    House Stark: {0}".format(house_stark))
print("    House Tully: {0}".format(house_tully))
print("  Night's Watch: {0}".format(nights_watch))
print("House Lannister: {0}".format(house_lannister))
print("House Baratheon: {0}".format(house_baratheon))
print("House Targaryen: {0}".format(house_targaryen))