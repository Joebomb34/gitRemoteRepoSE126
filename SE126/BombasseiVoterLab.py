#Joe Bombassei
#Lab 3B
#8/4/21
#SE126.02
#Program Prompt: Program to analyze potential voters

#Varriable Dictionary:

#pne = perspon not elgible
#oenr = old enogh not registered
#evnv = elgible to vote did not vote
#pdv = person did vote
#tot = Total number of people
#answer = 'y' to stay in the loop 'n' to exit
#idn = identification number
#age = voters age
#rv = registered to vote
#vote = did they vote

pne = 0
oenr = 0
evnv = 0
pdv = 0
tot = 0
answer = "Y"
print("\n\t\t\t\t\t\tWelcome!")

#ask all questions first
while answer.upper() == "Y":
  idn = input("\nWhat is the voters ID number?: ")
  age = int(input("What is the voters age?: "))
  rv = input("Is the person registered to vote?: ")
  vote = input("Did the person vote?: ")
  #set condition to what catagory people will be entered
  if age <= 17:
    pne += 1
    tot += 1
  
  if age >= 18 and rv.upper() == "Y" and vote.upper() == "Y":
    pdv += 1
    tot += 1

  if age >= 18 and rv.upper() == "Y" and vote.upper() == "N": 
    evnv += 1
    tot += 1
  
  if age >= 18 and rv.upper() == "N":
    oenr += 1
    tot += 1
#ask question to exit the loop
  answer = input("Would you like to enter someone else?[Y/N]: ").upper()
#display fina results
print("\n\t\t\t      Number of people not elgible: {0}\nNumber of people old enough but not registered: {1}\n     People old enogh to vote but did not vote: {2}\n\t\t\t     Number of people who did vote: {3}\n\t\t\t\t\t   Total number of records: {4}".format(pne, oenr, evnv, pdv, tot))
print("\n\n\t\t\t\t\tHave a great day!")