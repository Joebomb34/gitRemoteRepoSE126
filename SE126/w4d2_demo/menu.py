#when we're building a menu, usually, its a repeated process --> WHILE LOOP

def menu():
    '''shows menu, gets choice, ensures choice is valid, returns choice to user'''
    print("\t\tmenu")
    print("1. Print a random color")
    print("2. Print a random number")
    print("3. Print Hello World")
    print("4. EXIT")

    #gete user's choice
    choice = input("\tEnter your menu selection [1-4]: ")

    #make sure user gives you a valid value
    while choice != "1" and choice != "2" and choice != "3" and choice != "4":

        #ERROR TRAP LOOP!
        print("\t\t***ERROR ERROR***")
        choice = input("\tEnter your menu selection [1-4]: ")

    return choice

def goodbye():
    '''prints goodbye message'''
    print("\n\n\tThanks for using the program. GOODBYE :]")

#MAIN PROGRAM-----------------------------------

#initialize the loop key variable
answer = "y"

while answer == "y":

    # print("\t\tmenu")
    # print("1. Print a random color")
    # print("2. Print a random number")
    # print("3. Print Hello World")
    # print("4. EXIT")

    # #gete user's choice
    # choice = input("\tEnter your menu selection [1-4]: ")

    # #make sure user gives you a valid value
    # while choice != "1" and choice != "2" and choice != "3" and choice != "4":

    #     #ERROR TRAP LOOP!
    #     print("\t\t***ERROR ERROR***")
    #     choice = input("\tEnter your menu selection [1-4]: ")

    #call menu() and store to main 'choice'
    choice = menu()

    if choice == "1":
        print("\t\tRandom color\n\n")

    elif choice == "2":
        print("\t\tRandom number\n\n")

    elif choice == "3":
        print("\t\tHello World\n\n")

    elif choice == "4":
        print("\t\tE X I T I N G . . .")
        #in order to exit, we must break out of the loop ie make the loop condition false
        answer = "x"

    #option to re-enter loop; opportunity to revalue the loop condition key (answer)
    if choice != "4":#this gives people who choose EXIT are not asked if they would like to return to the loop
        answer = input("\t\tWould you like to re-enter the loop? [y/n]: ")

        while answer != "n" and answer != "y":
            answer = input("Would you like to re-enter the loop?[y/n]: ")
            answer = answer.lower()

goodbye()

