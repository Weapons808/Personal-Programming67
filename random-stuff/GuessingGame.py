import random

def GreaterThanRightAnswer():
    print("Wrong answer! Your answer was greater than the correct number. Try again.")
def LessThanRightAnswer():
    print("Wrong answer! Your answer was less than the correct number. Try again.")

print("Let's play a number guessing game, pray you don't lose to a clanker lol")
print("Your score will be calculated with the number of your guesses left x100. You start with 0 score.")
GoldenNumber = random.randint(1,10)
GuessesLeft = 5
Score = 0

def LostGame():
    print("You lost. The correct number was", GoldenNumber,".")

# print(GoldenNumber) 
#for debugging (just comment it out if you don't want it to show the number.)

while GuessesLeft > 0:
    PlayerGuess = input("Pick a number between 1 and 10: ")
    PlayerGuess = int(PlayerGuess)
    if PlayerGuess > GoldenNumber:
        GuessesLeft -= 1
        if GuessesLeft > 1:
            GreaterThanRightAnswer()
            print("You still have", GuessesLeft, "guesses left.")
        elif GuessesLeft == 1:
            GreaterThanRightAnswer()
            print("You are down to your last guess. Choose Wisely. ")
            PlayerLastGuess = int(input("Pick a number between 1 and 10: "))
            if PlayerLastGuess != GoldenNumber:
                LostGame()
                print("Your score was:", Score,".")
                break
    elif PlayerGuess < GoldenNumber:
        GuessesLeft -= 1
        if GuessesLeft > 1:
            LessThanRightAnswer()
            print("You still have", GuessesLeft, "guesses left.")
        elif GuessesLeft == 1:
            LessThanRightAnswer()
            print("You are down to your last guess. Choose Wisely. ")
            PlayerLastGuess = int(input("Pick a number between 1 and 10: "))
            if PlayerLastGuess != GoldenNumber:
                print("You lost. The correct number was", GoldenNumber,".")
                print("Your score was:", Score,".")
                break
    elif PlayerGuess == GoldenNumber:
        print("You guessed the correct number! Good boy!")
        Score = GuessesLeft * 100
        print("Your score was:", Score,".")
        break
    elif GuessesLeft == 0:
        print("You're out of lives! The correct answer was:", GoldenNumber, ".")