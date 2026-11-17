import random
import time

Lives = 5

WordsAndLettersDictionary = {"Apple" : 5, "House" : 5, "River" : 5, "Planet" : 6, "Garden" : 6, "School" : 6, "Rainbow" : 7, "Mountain" : 8, "Sunshine" : 8, "Computer" : 8}
WordUnderscores = ["_ _ _ _ _", "_ _ _ _ _ _", "_ _ _ _ _ _ _", "_ _ _ _ _ _ _ _"]

#edfegfdsgfdgfdsgdfsgdfsgdfsg
def welcomeInterface():
    Play1 = input("Press 1 to start, or type 'QUIT' at any time to end program ")
    Play1 = Play1.capitalize()
    if Play1 == "1":
        Words = WordsAndLettersDictionary.keys()
        Words = list(Words)
        RandomWord = random.choice(Words)
        Words.remove(RandomWord)
        LetterCount = WordsAndLettersDictionary[RandomWord]
        if LetterCount == 5:
            RandomLetterCount = 0
        elif LetterCount == 6:
            RandomLetterCount = 1
        elif LetterCount == 7:
            RandomLetterCount = 2
        elif LetterCount == 8:
            RandomLetterCount = 3
        while Lives > 0:
            print("You have", Lives, "Game starts in...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(0.5)
            print("GO!")
            print(WordUnderscores[RandomLetterCount])
            LetterGuessOrWordGuess = input("Press 1 if you would like to guess the letter or 2 to guess the word: ")
            LetterGuessOrWordGuess = LetterGuessOrWordGuess.capitalize()
            if LetterGuessOrWordGuess == "1":
                LetterGuess = input("Enter your guess: ")
            elif LetterGuessOrWordGuess == "2":
                WordGuess = input("Enter your guess: ")
            elif LetterGuessOrWordGuess == "QUIT":
                print("Program ended successfully.")
                break
            else:
                print("program ended successfully")
                break
    elif Play1 == "QUIT":
        print("Program ended.")
    else:
        print("Please enter a proper option.")
        welcomeInterface()


