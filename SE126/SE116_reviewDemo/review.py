#Joe Bombassei
#SE116 Review
#7/21/2021

#Program Prompt: This is a temperature converter program, it allows user to enter as many Farenheit temperatures as the user wants and shows the Celcius conversion for each. It also counts the number of temeratures entered, and determines average of all temps.

#VARIABLE DICTIONARY
#temp_count - the total number of temperatures
#total_temp - sum total of all temps entered
#avg_tempF
#avg_tempC - average of all temps
#tempF - temp in Farenheit
#tempC - temp in Celcius
#answer - loop control

#--------IMPORTS--------

#-------FUNCTIONS-------
def temp_converter(f):
    '''This function returns the celcius temp equivalent of the argument passed to it'''

    c = (f - 32) * (5 /9)

    return c



#-------MAIN CODE-------


temp_count = 0
total_temp = 0

answer = "y"

#total = int(input("\n\t\tHow many temperatures would you like to check today?: "))


while answer == "y" or answer == "Y":

    tempF = float(input("\t\tEnter temperature in Farenheit: "))

    tempC = temp_converter(tempF)

    temp_count += 1
    total_temp += tempF

    print("\tTemp# {0}\tTemp {1:.1f}F = Temp {2:.1f}C\n".format(temp_count, tempF, tempC))

    answer = input("\t\tWould you like to enter another temperature? [y/n]: ").lower()

    while answer != "y" and answer != "n":

        print("***INVALID OPTION***")

        answer = input("\t\tWould you like to enter another temperature? [y/n]: ").lower()


avg_tempF = total_temp / temp_count

avg_tempC = temp_converter(avg_tempF)

print("\n\t\tHere is your final session information: ")
print("\t\tTOTAL TEMPS ENTERED: {0}".format(temp_count))
print("\t\tAVERAGE TEMPS: {0:.1f}F | {1:.1f}C".format(avg_tempF, avg_tempC))

print("\n\n\t\tThank you for using the program. Goodbye.\n\n")