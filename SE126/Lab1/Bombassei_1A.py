#Joe Bombassei
#SE126
#Lab1A
#7/21/21

#Program Prompt: This is a program to determine if a meeting room is safe by fire regulations based on maximum capacity and number of people attending.

#VARIABLE DICTIONARY
#answer - loop control
#cap - maximum capacity of the room
#people - people attending
#difference - difference of attendies and room capacity
#-----FUNCTIONS-----

#-----MAIN CODE-----
answer = "y"
 
while answer == "y":

    cap = int(input("\t\tWhat is the room capacity?: "))
    people = int(input("\n\t\tHow many people will be attending?: "))
    difference = cap - people
    sum = people - cap

    if difference >= 0:
        print("The event can be held. {0} more people can attend.".format(difference))

    else:
       
        print("{0} people need to be told they cannot attend.".format(sum))

    answer = input("Would you like to check any more rooms? [y/n]: ")

print("Thank you for using my program. Goodbye.")