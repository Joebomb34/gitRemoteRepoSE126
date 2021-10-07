#Joe Bombassei
#SE126.02
#Lab 6B
#9/1/21

#PROGRAM PROMPT: Take user inputs to assign seats of passengers to a flight. Display the taken seats with an "X" and if the seat has already been taken do not allow them to be taken again.

#VARIABLE DICTIONARY:
#sit() - function to ask what row the user wants to sit in
#row - input of a number
#row_ - list to append to keep a list of user selections
#ss() - function for user to input which seat they would like
#seat - input of seat letter
#seat_ - list to append and keep track of what user has selected
#state() - statement of running list to see "X" in seats already chosen
#cont() - function for asking user if they would like to re-enter the loop
#answer - keep loop in otion
#seatA, seatB, seatC, seatD - man made list for rows
#i - index


def sit():
    row = int(input("What row would you like to sit in?: "))
    while row != 1 and row != 2 and row != 3 and row != 4 and row != 5 and row != 6 and row != 7:
        row = int(input("\nInvalid Option. Select an option 1 - 7: "))

    row_.append(row)
    row -= 1

    return row

def ss():
    seat = input("What seat would you like?: ").upper()

    while seat != "A" and seat != "B" and seat != "C" and seat != "D":
        seat = input("\nInvalid Option. Select an option A - D: ").upper()
    
    seat_.append(seat)

    return seat

def state():
    for i in range(0, len(seatA)):
        print("{0}. {1} {2}\t{3} {4}".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

def cont():
    
    answer = input("\nWould you like to choose another seat? [y/n]: ").lower()

    return answer



row_ = []
seat_ = []
seatA = ["A", "A", "A", "A", "A", "A", "A"]
seatB = ["B", "B", "B", "B", "B", "B", "B"]
seatC = ["C", "C", "C", "C", "C", "C", "C"]
seatD = ["D", "D", "D", "D", "D", "D", "D"]

for i in range(0, len(seatA)):
    print("{0}. {1} {2}\t{3} {4}".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

answer = "y"

while answer == "y":

    row = sit()
    seat = ss()

    if seat == "A": 
        if seatA[row] == "X":
            print("Seat is taken.")
        else:
            seatA[row] = "X"
            state()
    
    elif seat == "B":
        seatB[row] = "X"
        state()
        if seatB[row] == "X":
            print("Seat is taken.")

    elif seat == "C":
        if seatC[row] == "X":
            print("Seat is taken.")
        else:
            seatC[row] = "X"
            state()

    elif seat == "D":
        if seatD[row] == "X":
            print("Seat is taken.")
        else:
            seatD[row] = "X"
            state()
        
    
    answer = cont()
        

    while answer != "y" and answer != "n":    
        print("***INVALID OPTION***")

        answer = input("\nWould you like to choose another seat? [y/n]: ").lower()

    if answer == "n":
        row += 1

        print("\nThese are your selected seats: ")
        
        for i in range(0, len(row_)):
            print(row_[i], seat_[i])  