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

    '''This asks the room cap question'''

    cap = int(input("\t\tWhat is the room capacity?: "))
    
    return cap

def attendees():

    '''This asks the attending question'''

    people = int(input("\n\t\tHow many people will be attending?: "))
    
    return people

def register(cap, people):

    '''This takes the answer from each function and finds the difference'''

    diff = cap - people

    return diff

def again():  
    
    '''This asks if you want to remain in the loop'''

    answer = input("Would you like to check any more rooms? [y/n]: ").lower()  
    
    return answer

    
#-----MAIN CODE-----
answer = "y"
 
while answer == "y" or answer == "Y":

    cap = capacity()

    people = attendees()

    difference = register(cap, people)
   
    #conditions for the event

    if difference >= 0:
        print("The event can be held. {0} more people can attend.".format(difference))

    #when the above is false

    else:
        difference = difference * -1

        print("{0} people need to be told they cannot attend.".format(difference))

    answer = again()

    #user trap so the program won't just shut down or error

    while answer != "y" and answer != "n":    
        print("***INVALID OPTION***")

        answer = input("Would you like to check any more rooms? [y/n]: ").lower()    
        

print("Thank you for using my program. Goodbye.")