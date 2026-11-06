import random as rr
import time as tt

elementsDictionary = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Boron",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Ne": "Neon",
    "Na": "Sodium",
    "Mg": "Magnesium",
    "Al": "Aluminum",
    "Si": "Silicon",
    "P": "Phosphorus",
    "S": "Sulfur",
    "Cl": "Chlorine",
    "Ar": "Argon",
    "K": "Potassium",
    "Ca": "Calcium",
    "Sc": "Scandium",
    "Ti": "Titanium",
    "V": "Vanadium",
    "Cr": "Chromium",
    "Mn": "Manganese",
    "Fe": "Iron",
    "Co": "Cobalt",
    "Ni": "Nickel",
    "Cu": "Copper",
    "Zn": "Zinc",
    "Ga": "Gallium",
    "Ge": "Germanium",
    "As": "Arsenic",
    "Se": "Selenium",
    "Br": "Bromine",
    "Kr": "Krypton",
    "Rb": "Rubidium",
    "Sr": "Strontium",
    "Y": "Yttrium",
    "Zr": "Zirconium",
    "Nb": "Niobium",
    "Mo": "Molybdenum",
    "Tc": "Technetium",
    "Ru": "Ruthenium",
    "Rh": "Rhodium",
    "Pd": "Palladium",
    "Ag": "Silver",
    "Cd": "Cadmium",
    "In": "Indium",
    "Sn": "Tin",
    "Sb": "Antimony",
    "Te": "Tellurium",
    "I": "Iodine",
    "Xe": "Xenon"
}
def startFunction():
    print("Get READY! Start in:")
    print("3")
    tt.sleep(1)
    print("2")
    tt.sleep(1)
    print("1")
    tt.sleep(0.5)
    print("GO!")


def symbolsQuiz():
    score = 0
    questionsGotThrough = 0
    numberOfElements = 54

    symbols = elementsDictionary.keys()
    symbolsList = list(symbols)
    
    while questionsGotThrough < 54:
        randomSymbolChosen = rr.choice(symbolsList)
        symbolsList.remove(randomSymbolChosen)
        elementAnswer = elementsDictionary[randomSymbolChosen]
        print("What is the symbol for this element: {}?".format(elementAnswer))
        answer = input("Enter answer here: ")
        if answer == randomSymbolChosen:
            questionsGotThrough += 1
            score += 1
            print("You got it right. Your score is:", score,"out of 54. only",numberOfElements - questionsGotThrough,"left.")
        elif answer != randomSymbolChosen:
            questionsGotThrough += 1
            print("Sorry, incorrect. The correct answer was:", randomSymbolChosen, "Your score is:", score,"out of 54. only",numberOfElements - questionsGotThrough,"left.")
    print("Good job. you got", score,"correct.")
    returnInput = int(input("to go back to welcome interface, press 1, press 2 to QUIT PROGRAM"))
    if returnInput == 1:
        print("Returning to welcome interface in 3 seconds.")
        tt.sleep(3)
        welcomeInterface()
    else:
        print("Program quit successfully. See ya.")

def elementsQuiz():
    score = 0
    questionsGotThrough = 0
    numberOfElements = 54
    
    symbols = elementsDictionary.keys()
    symbolsList = list(symbols)
        
    while questionsGotThrough < 54:
        randomSymbolChosen = rr.choice(symbolsList)
        symbolsList.remove(randomSymbolChosen)
        elementAnswer = elementsDictionary[randomSymbolChosen]
        print("What is this element's symbol: {}?".format(elementAnswer))
        answer = input("Enter answer here: ")
        if answer == randomSymbolChosen:
            questionsGotThrough += 1
            score += 1
            print("You got it right. Your score is:", score,"out of 54. only",numberOfElements - questionsGotThrough,"left.")
        elif answer != randomSymbolChosen:
            questionsGotThrough += 1
            print("Sorry, incorrect. The correct answer was", randomSymbolChosen, "Your score is:", score,"out of 54. only",numberOfElements - questionsGotThrough,"left.")
    print("Good job. you got", score,"correct.")
    returnInput = int(input("to go back to welcome interface, press 1, press 2 to QUIT PROGRAM"))
    if returnInput == 1:
        print("Returning to welcome interface in 3 seconds.")
        tt.sleep(3)
        welcomeInterface()
    else:
        print("Program quit successfully. See ya.")

def welcomeInterface():
    print("Welcome to the elements study guide so you can pass johnsons class lol")
    tt.sleep(0.5)
    print("press 1 to take symbols quiz, 2 to take elements quiz, 3 to QUIT PROGRAM")
    tt.sleep(0.5)
    welcome = int(input("Enter Response Number: "))
    if welcome == 1:
        print("You chose the symbols quiz.")
        tt.sleep(0.5)
        startFunction()
        symbolsQuiz()
    elif welcome == 2:
        print("You chose the elements quiz.")
        tt.sleep(0.5)
        startFunction()
        elementsQuiz()
    elif welcome == 3:
        print("Program ended successfully.")
        tt.sleep(1)
        print("See ya next time")
    else:
        print("please enter a valid option.")
        welcomeInterface()

welcomeInterface()