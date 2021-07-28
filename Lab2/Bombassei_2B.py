#Joe Bombassei
#SE126
#Lab2B
#7/28/21

#PROGRAM PROMPT: Read the csv file and display the information in the file in a more clear way.

#VARIABLE DICTIONARY:
#total_computers = computers in the file
#csvfile = lab2b.csv
#file = csv after reader
#c_type = type of computer
#brand = manufacturer
#intel = processor type
#ram = RAM in GB
#hdd_size = size of the Hard Disk Drive
#n_hdd = number of HDD's
#t_hdd = second HDD size
#os = Operating System
#yr = year the computer was purchased

#MAIN CODE
import csv

total_computers = 0

#header
print("{0:8}\t{1:8}\t{2:3}\t{3:7}{4:2} {5:2}  {6:6}  {7:6}  {8:4}".format("TYPE", "BRAND", "CPU", "RAM", "1st DISK", "#HDD", "2nd DISK", "OS", "YR"))
print("------------------------------------------------------------------------------------")

with open("Lab2/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)


    for rec in file:

        total_computers += 1

        if rec[0] == "D":
            c_type = "Desktop"

        else:
            c_type = "Laptop"


        if rec[1] == "DL":
            brand = "Dell"

        elif rec[1] == "HP":
            brand = "HP"

        else:
            brand = "Gateway"

        intel = rec[2]

        ram = rec[3]

        hdd_size = rec[4]

        n_hdd = int(rec[5])

        if n_hdd == 1:
            t_hdd = " "
            os = rec[6]
            yr = rec[7]

        else:
            t_hdd = rec[6]
            os = rec[7]
            yr = rec[8]

        print("{0:8}\t{1:8}\t{2:3}\t{3:7}\t{4}\t{5:2}\t{6:6}\t{7:6}\t{8:4}".format(c_type, brand, intel, ram, hdd_size, n_hdd, t_hdd, os, yr))
        
print("TOTAL NUMBER OF COMPUTERS: {0}".format(total_computers))
