#W3D2 -- List Practice; connect to and read from a text file then store data from file into lists and be used throughout the program

import csv #will also read .txt

#count records iin the file
records = 0

#prep some empty lists
#one list for every potential field in the file
name = [] #name = ['Nate', 'Ron', 'Steph', 'Joe'] --used if you dont want to use a text file, don't do this
age = []
color = []
animal = []
section = []

with open("w3d2_Demo/classList_202140.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        #store data into the lists
        name.append(rec[0])
        age.append(int(rec[1]))
        color.append(rec[2])
        animal.append(rec[3])
        section.append("SE126.02")
#disconnected from the file
print("\n\tFinished reading file; {0} records processed\n".format(records))

#list processing --> FOR LOOP!
for i in range(0, records): #for each index starting at 0 and running up to record number (in this case 9, UP TO not including)
    print("INDEX: {0} |{1:7}{2:4}{3:8}{4:10}{5}".format(i, name[i], str(age[i]), color[i], animal[i], section[i]))

total_age = 0
for i in range(0, len(age)): #len()returns number of items

    total_age += age[i]

average_age = total_age / records

print("\n\tAverage Age: {0:.2f}".format(average_age))

#process the lists to count/ tally favorite animals

crow = 0
elephant = 0
dog = 0
dolphin = 0
monkey = 0
lion = 0
wolf = 0

for i in range(0, records):

    if animal[i] == "crow":
        crow += 1

    elif animal[i] == "elephant":
        elephant += 1

    elif animal[i] == "dog":
        dog += 1

    elif animal[i] == "dolphin":
        dolphin += 1

    elif animal[i] == "monkey":
        monkey += 1

    elif animal[i] == "lion":
        lion += 1

    elif animal[i] == "wolf":
        wolf += 1

    else:
        print("**ERROR** unexpected animal found in record: ", i)

print("\n\tFAVORITE ANIMAL TALLIES: ")
print("\t\tDOG: ", dog)
print("\t\tCROW: ", crow)
print("\t\tELEPHANT: ", elephant)
print("\t\tDOLPHIN: ", dolphin)
print("\t\tWOLF: ", wolf)
print("\t\tLION: ", lion)
print("\t\tMONKEY: ", monkey)
