#Joe Bombassei
#SE126.02
#Lab 3A
#8/4/21

#Program Prompt: Replace computers that were made 2016 and earlier and determine the cost to replace each and display the number of dektops, and laptops being replaced and the price to do so

#Variable Dictionary:
#badD = number of bad desktops
#badL = number of bad laptops
#total_computers = number of records processed
#c_type = computer type
#brand = manufacturer
#cpu = cpu computer has
#ram = ram computer has
#fdisk = first hdd
#tot_hdd = number of hdd
#secdisk = second hdd (if any)
#os = operating system computer is running
#yr = year computer was purchased
#csvfile = rename of impoted file
#file = rename of csvfile
#price = total price to replace desktops or laptops

#--Main Program--
badD = 0
badL = 0
total_computers = 0
c_type = []
brand = []
cpu = []
ram = []
fdisk = []
tot_hdd = []
secdisk = []
os = []
yr = []

import csv

with open("Lab3/lab3a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        total_computers += 1

        c_type.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(rec[3])
        fdisk.append(rec[4])
        tot_hdd.append(int(rec[5]))

        if rec[5] == "1":
            secdisk.append(" ")
            os.append(rec[6])
            yr.append(int(rec[7]))

        elif rec[5] == "2":
            secdisk.append(rec[6])
            os.append(rec[7])
            yr.append(int(rec[8]))

print("\nRecords Processed: {0}".format(total_computers))

for i in range(0, total_computers):
    if yr[i] <= 16 and c_type[i] == "D":
        badD += 1
        price = badD * 2000
print("\nTo replace {0} Dektops it will cost ${1:8.2f}".format(badD, price))

for i in range(0, total_computers):
    if yr[i] <= 16 and c_type[i] == "L":
        badL += 1
        price = badL * 1500
print("\nTo replace {0} Laptops it will cost ${1:8.2f}".format(badL, price))

print("\nPress Any Key To Continue. . .")