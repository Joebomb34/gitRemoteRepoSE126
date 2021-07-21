#Joe Bombassei
#SE126
#Lab1C
#7/21/21

#Program Prompt: This is a program to determine if a meeting room is safe by fire regulations based on maximum capacity and number of people attending.

#VARIABLE DICTIONARY
#answer - loop control
#cap - maximum capacity of the room
#people - people attending
#difference - difference of attendies and room capacity
#-----FUNCTIONS-----
def capacity():
    cap = int(input("\t\tWhat is the room capacity?: "))

    return cap


#-----MAIN CODE-----
answer = "y"
 
while answer == "y" or answer == "Y":

    cap = capacity()

    people = int(input("\n\t\tHow many people will be attending?: "))
    difference = cap - people
    sum = people - cap

    if difference >= 0:
        print("The event can be held. {0} more people can attend.".format(difference))

    else:
       
        print("{0} people need to be told they cannot attend.".format(sum))

    answer = input("Would you like to check any more rooms? [y/n]: ").lower()

    while answer != "y" and answer != "n":
        print("***INVALID OPTION***")

        answer = input("Would you like to check any more rooms? [y/n]: ").lower()

print("Thank you for using my program. Goodbye.")