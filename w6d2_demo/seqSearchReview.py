#W6D2 Sequential Search Review - Hand populated list

name = ["Nate", "Ron", "Steph", "Joe", "Ethan", "Berta", "Jess"]
favDrink = ["Water", "Coors Lite", "High Noon", "Knob Creek", "Water", "Lemonade", "Titos's"]

answer = "y"

while answer == "y":
    search = input("Enter the name you are looking for: ").lower()

    found = -1 #will represent the index of the searched for item if found; if not found it will remain -1

    for i in range(0, 7):#when using a hand populated list you jst count out the number of items

        if search == name[i].lower():

            #name found
            found = i #store the current location into found
    
    if found != -1:

        print("Your search for {0} was FOUND!".format(search))
        print("NAME: {0} FAVORITE DRINK: {1}".format(name[found], favDrink[found]))

    else:
        print("Your search for {0} was NOT FOUND!".format(search))

    search2 = input("Enter the DRINK you wish to find: ").lower()

    found = -1

    for i in range(0, 7):

        if search2 == favDrink[i].lower():

            found = i
            print("NAME: {0} FAVORITE DRINK: {1}".format(name[found], favDrink[found]))

    #   if found != -1:
    #     print("Your search for {0} was FOUND!".format(search))
    #     print("NAME: {0} FAVORITE DRINK: {1}".format(name[found], favDrink[found]))

    # else:
    #     print("Your search for {0} was NOT FOUND!".format(search))

    if found == -1:
        print("Your search for {0} was NOT FOUND!".format(search2))

    answer = input("\nWould you like to search again? [y/n]: ").lower()


