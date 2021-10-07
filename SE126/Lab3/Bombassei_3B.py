#Joe Bombassei
#SE126.02
#Lab 3B
#8/4/21

#Program Prompt: Rewrite voter registration lab to determine voter id number, age, and if person is registered or not, and if the person has voted or not

#Variable Dictionary:
#records = number of records processed
#pne = perspon not elgible
#oenr = old enogh not registered
#evnv = elgible to vote did not vote
#pdv = person did vote
#idnum = voter id
#age = person age
#reg = registered or not
#vote = vote or not
#csvfile = impoted file
#file = rnmaed file after read

#--Main Code--
import csv

records = 0
pne = 0
oenr = 0
evnv = 0
pdv = 0
#start list
idnum = []
age = []
reg = []
vote = []

with open("Lab3/voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1
        #append the list so file can close
        idnum.append(rec[0])
        age.append(int(rec[1]))
        reg.append(rec[2])
        vote.append(rec[3])

        #if and elif statements to figure the stats needed
        
        if rec[1] <= "17":
            pne += 1

        elif rec[1] >= "18" and rec[2] == "Y" and rec[3] == "Y":
            pdv += 1

        elif rec[1] >= "18" and rec[2] == "N":
            oenr += 1

        elif rec[1] >= "18" and rec[2] == "Y" and rec[3] == "N":
            evnv += 1


print("\n             Not Elgible: {0:2}\n  Of Age, Not Registered: {1:2}\nRegistered, Did Not Vote: {2:2}\n                Did Vote: {3:2}\n       Records Processed: {4:3}".format(pne, oenr, evnv, pdv, records))
