import random
import time

def skillCheck(skill):
    ques = input("Where do you want to roll? (system/irl): ")
    randBinary()

    if ques == "system":
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        r3 = random.randint(1, 6)
        rsum = r1 + r2 + r3

        roll = r1, r2, r3
        roll = str(roll)
        return rsum < skill
        
    elif ques == "irl":
        rsum = input("What was the roll?: ")
        rsum = int(rsum)
        return rsum < skill

def randBinary():
    binLength = random.randint(200, 1000)
    for x in range(binLength):
        string = '01'
        print(random.choice(string), end = "")
        x+=1
    print('')

    
def breach():
    print("Running breach.exe", end = '')
    time.sleep(.75)
    print('.', end = '')
    time.sleep(.75)
    print('.', end = '')
    time.sleep(.75)
    print('.')
    
    if skillCheck(deck['breach']):
        print("You're in.")
        return True
    else:
        print("No dice.")
        return False

file = "starterDeck.txt"

"""f = open(file, "w")
f.write("breach 14:damage 16:search 14")
f.close()"""

f = open(file, "r")
initial = str(f.read())

programs = initial.split(':')
deck = {}
for x in range(len(programs)):
    program = programs[x].split()[0]
    skill = int(programs[x].split()[1])
    deck[program] = skill

progList = []
for key in deck.keys():
    progList.append(key)


connected = False

inp = input("You have the connection, ready to breach?(y/n): ")

if inp == 'y':
    connected = breach()

while connected:
    
    print("What's the plan?", progList, ": ")
    inp = input()
    if inp == "breach":
        breach()
    elif inp == "quit":
        connected = False
    else:
        print("Can't do that yet cowboy.")

print("See you next time.")
