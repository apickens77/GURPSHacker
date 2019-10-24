import random
import time
from tkinter import *
from tkinter import ttk

#not used at the moment
#generates a random string of 0's and 1's from length 200 to 1000
#used for flavor but doesn't seem to work as well on textboxes
def randBinary():
    binLength = random.randint(200, 1000)
    for x in range(binLength):
        string = '01'
        print(random.choice(string), end = "")
        x+=1
    print('')

#file IO stuff
file = "starterDeck.txt"
f = open(file, "r")

#sets the file input to a string
initial = str(f.read())

#splits the string into individual skills with skill levels and initializes stuff for later
programs = initial.split(':')
deck = {}
progList = []

#creates a dictionary with the skill name as keys and the skill levels as values
for x in range(len(programs)):
    program = programs[x].split()[0]
    progList.append(program)
    skill = int(programs[x].split()[1])
    deck[program] = skill

"""
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
"""

#sets up gui window
root = Tk()
root["bg"] = "black"
root.title("GURPS Hacker")
root.minsize(800, 500)

#grabs image to be used for background. Image size needs changing
bgImage = PhotoImage(file = "background.png")
w = bgImage.width()
h = bgImage.height()
root.geometry("%dx%d+50+30" % (w, h))
cv = Canvas(width = w, height = h)

cv.create_image(0, 0, image = bgImage, anchor = 'nw')

#adds the top and bottom frame to the root window
topFrame = Frame(cv)
topFrame['bg'] = ''
bottomFrame = Frame(cv)
bottomFrame['bg'] = ''
sideFrame = Frame(cv)
sideFrame['bg'] = ''

#radio buttons
v = IntVar()

systemButt = Radiobutton(sideFrame, text = "System", bg = 'black', fg = 'red', variable = v, value = 0)
irlButt = Radiobutton(sideFrame, text = "IRL", bg = 'black', fg = 'red', variable = v, value = 1)

#sets the combobox values to the list of programs read in from the file
comboBox1 = ttk.Combobox(topFrame, values = progList)

#somethings wierd here
#it sets the colors but not for the whole combobox
style = ttk.Style()
style.map('TCombobox', fieldbackground=[('readonly','black')])
style.map('TCombobox', selectbackground=[('readonly', 'black')])
style.map('TCombobox', selectforeground=[('readonly', 'red')])
comboBox1['state'] = 'readonly'

#checks what program is being executed and runs the method associated with it
#VERY INCOMPLETE. Only breach program is implemented
def execute():
    textBox.delete('1.0', END)
    if comboBox1.get() == "breach":
        breach()
    elif comboBox1.get() == "":
        textBox.insert(END, "You actually going to do something?")
    else:
        textBox.insert(END, "You can't do that yet.")

#creates the execure button and textbox where all the relevent info will be displayed
executeButt = Button(topFrame, text = "Execute Program", bg = "black", fg = "red", command = execute)
textBox = Text(bottomFrame, height = 10, bg = "black", fg = "red")

#input box
inpBox = Text(bottomFrame, height = 1, bg = 'black', fg = '#03f6fe')
inpBox.pack(side = BOTTOM)

#simple method to clear the textbox 
def clear():
    textBox.delete("1.0", END)
    inpBox.delete("1.0", END)
    
clrButton = Button(bottomFrame, text = "Clear Window", bg = "black", fg = "red", command = clear)

#takes the skill level in and simulates a dice roll to check for success
#taken from the GURPS rulebook
def skillCheck(skill):
    #ques = input("Where do you want to roll? (system/irl): ")
    #randBinary()

    #if ques == "system":
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    r3 = random.randint(1, 6)
    rsum = r1 + r2 + r3


    roll = r1, r2, r3
    roll = str(roll)
    stmt = "Skill: " + str(skill) + "\nRoll: " + str(rsum) + roll + "\n"
    textBox.insert(END, stmt)
    return rsum <= skill

    #option for player to roll dice manually
    #to be implemented later    
    """elif ques == "irl":
        rsum = input("What was the roll?: ")
        rsum = int(rsum)
        return rsum < skill"""

#runs a skill check against the users breach program skill
#not much functionality and doesn't account for other system complications
def breach():
    textBox.insert(END, "Running breach.exe...\n")

    """if v == 0:
        chk = skillCheck(deck['breach'])
    else:
        inpBox.insert(END, "What was the roll?: ")
        chk = inpBox.get(1.0, END).split()[-1]"""
        
        

    #chk = int(chk)
    
    if skillCheck(chk):
        textBox.insert(END, "You're in.")
    else:
        textBox.insert(END, "No dice.")

#inserts all relevent objects into the gui and sets the main loop to display window
cv.pack(side = 'bottom', fill = 'both', expand = 'yes')
topFrame.pack(padx = 20)
sideFrame.pack(padx = 20, pady = 20)
clrButton.pack()
bottomFrame.pack(padx = 20, pady = 200)

executeButt.pack(padx = 20, pady = 20)

systemButt.pack(side = LEFT)
irlButt.pack(side = LEFT)
comboBox1.pack()
textBox.pack()



root.mainloop()
if v == 1:
    inpBox.insert(END, "What was the roll?: ")
    
    chk = inpBox.get(1.0, END).split()[-1]
