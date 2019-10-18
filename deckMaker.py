inp = input("Enter the program name and skill level (ex. breach 14): ")
deckString = ""
file = "starterDeck.txt"

while not inp == 'quit':
    if deckString == "":
        deckString = inp
    else:
        deckString = deckString + ":" + inp
    inp = input("Add another or type \'quit\': ")

f = open(file, "w")
f.write(deckString)
f.close()
