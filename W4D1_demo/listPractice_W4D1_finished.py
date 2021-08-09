#WEEK 4 DAY 1: LIST PRACTICE & REVIEW DEMO

#PROMPT: Write a program that reads the data file (below) and stores the data into lists.� then, process the lists to reprint the file data, record by record. Next, reprocess the lists to find each student's current average score along with the class average.� Store each student's average into a new list called 'avg' and reprint the records to include the average.� Reprocess the lists one more time to find the letter equivalent of the average and store this into a new list called 'let_avg'.� Reprint the lists for a third and final time, record by record including average score and average letter equivalent.� After this third print, print to the console the total number of student's in the class along with the class numeric average.��



#NOTES: 
#       *All averages should be rounded to the 2nd decimal place.
#       *Process List = for loop
#       * 'index' represents location within a list when processing through a for loop 
#       * average = sum_total / num_items
#       * 90 >= A ; 90 < B >= 80; 80 < C >= 70; 70 < D >= 60; 60 < F
#       * FILE SETUP:
#           FIELD0      FIELD1      FIELD2      FIELD3      FIELD4
#           FIRSTNAME   LASTNAME    TEST1       TEST2       TEST3
#       *once all processing of lists has taken place, the following should appear for each student
#       FIRSTNAME   LASTNAME    TEST1       TEST2       TEST3       NUM AVG     LETTER AVG


#VARIABLE DICTIONARY----------------------

#records        total records within the file, also total number of values in each list
#csvfile        shorthand name for file location, full file path
#file           firendly name for file data, after it has been passed through csv.reader()
#rec            LIST, an inidivudal record from the file; only used when connected to file
#first          LIST, first names of students ( rec[0] )
#last           LIST, last names of students ( rec[1] )
#test1          LIST, test 1 scores of students ( rec[2] )
#test2          LIST, test 2 scores of students ( rec[3] )
#test3          LIST, test 3 scores of students ( rec[4] )
#average        average sudents test score; average = (test1 + test2 + test3) / 3
#avg            LIST, numeric averages of each student
#letter         letter equivalent of student's average, requires an if/elif/elif/elif/else chain
#avg_let        LIST, letter averages of each student
#class_total    sum total of all numeric averages in the class
#class_average  class numeric average; class_average = class_total / records



#BASE PROGRAM CODE------------------------------------------------------------------------------------------------------------

#import library for text file handling
import csv 

#initialize variables for program (that will add to themselves)
records = 0 
class_total = 0 


#initialize empty lists for program - one list for every field in the text file
firstname = []
lastname = []
test1 = []
test2 = []
test3 = []

avg = []
let_avg = []


#CONNECTED TO FILE-----------------------------------------------------------
#connect to file location
with open("W4D1_demo/listPractice1.txt") as csvfile:
    #allow file data to be accessed as 'file'
    file = csv.reader(csvfile)


    #process file data using 'rec' and 'file'
    for rec in file:
        #print(rec)
        #update current records count
        records += 1
        #print(records-1)
        #store (append) file data into lists; since we are splitting one record's data into specific lists at a time, data is stored into separate lists *at the same point (position, index)* in each of the lists
        #the test scores will be mathematically processed, so make sure the test lists are populated with numeric data
        firstname.append(rec[0])
        lastname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
        


#"FILE CLOSED"----------------------------------------------------------------

#PROCESS LISTS = FOR LOOP!
print("---ORIGINAL FILE DATA----------------------------------")
print("{0:15}\t{1:15}\t{2:5}\t{3:5}\t{4:5}".format("FIRST", "LAST", "TEST1", "TEST2", "TEST3"))
print("-------------------------------------------------------")
#Process the lists to reprint the file data, record by record
for i in range(0, records):
    #REMEMBER: index = position in the list
    print("{0:15}\t{1:15}\t{2:5}\t{3:5}\t{4:5}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i]))


#Reprocess the lists to find each student's current average score along with the class average. Store each student's average into a new list called 'avg' and reprint the records to include the average
print("\n\n---AVERAGES ADDED------------------------------------------")
print("{0:15}\t{1:15}\t{2:5}\t{3:5}\t{4:5}\t{5:5}".format("FIRST", "LAST", "TEST1", "TEST2", "TEST3", "AVG"))
print("---------------------------------------------------------------")
for i in range(0, len(firstname)):
    #find student's average
    average = (test1[i] + test2[i] + test3[i]) / 3
    #store average into list: avg (where the rest of this student's data is found)
    avg.append(average)
    #add student's average into class_total
    class_total += average
    #print entire student record including avg
    print("{0:15}\t{1:15}\t{2:5}\t{3:5}\t{4:5}\t{5:5.2f}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i], avg[i]))

#Reprocess the lists one more time to find the letter equivalent of the average and store this into a new list called 'let_avg'.� Reprint the lists for a third and final time, record by record including average score and average letter equivalent.
print("\n\n---AVERAGES ADDED------------------------------------------------------")
print("{0:15}\t{1:15}\t{2:5}\t{3:5}\t{4:5}\t{5:5}\t\t{6:3}".format("FIRST", "LAST", "TEST1", "TEST2", "TEST3", "AVG", "LET"))
print("---------------------------------------------------------------------------")
for i in range(0, records):
    #find student's letter grade based on their average (thier average is stored in the list named 'avg'
    if avg[i] >= 90:
        letter = "A"
    elif avg[i] >= 80:
        letter = "B"
    elif avg[i] >= 70:
        letter = "C"
    elif avg[i] >= 60:
        letter = "D"
    else:
        letter = "F"
    #store letter value into let_avg list (where the rest of this student's data is found)
    let_avg.append(letter)

    #reprint student's entire record data, include their numeric and letter averages
    print("{0:15}\t{1:15}\t{2:5}\t{3:5}\t{4:5}\t{5:5.2f}\t\t{6:3}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i], avg[i], let_avg[i]))

#process class_average to find its value
class_average = class_total / records

#Print to the console the total number of student's in the class along with the class numeric average.��
print("\n\nSTUDENTS IN CLASS: {0} | CLASS AVERAGE: {1:.2f}".format(records, class_average))
