#Joe Bombassei
#SE126.02
#Lab 6B
#9/1/21

#PROGRAM PROMPT:

#VARIABLE DICTIONARY:

def sit():
    row = int(input("What row would you like to sit in?: "))
    while row != 1 and row != 2 and row != 3 and row != 4 and row != 5 and row != 6 and row != 7:
        row = input("Invalid Option. Select an option 1 - 7: ")
    row -= 1

    

    return row

def ss():
    seat = input("What seat would you like?: ")

    while seat != "A" and seat != "B" and seat != "C" and seat != "D":
        seat = input("Invalid Option. Select an option A - D: ")

    return seat

def state():
    for i in range(0, len(seatA)):
        print("{0}. {1} {2}\t{3} {4}".format((i + 1), seatA[i], seatB[i], seatC[i], seatD[i]))

def cont():
    
    answer = input("Would you like to choose another seat? [y/n]: ").lower()

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
        seatA[row] = "X"
        state()
        
    elif seat == "B":
        seatB[row] = "X"
        state()

    elif seat == "C":
        seatC[row] = "X"
        state()

    elif seat == "D":
        seatD[row] = "X"
        state()

    
    
    
    answer = cont()

   

    while answer != "y" and answer != "n":    
        print("***INVALID OPTION***")

        answer = input("Would you like to choose another seat? [y/n]: ").lower()

    if answer == "n":
        row += 1
        row_.append(row)
        seat_.append(seat)
        for i in range(0, len(row_)):
            print("These are your selected seats:")
            print("{0}".format(row_[i]))