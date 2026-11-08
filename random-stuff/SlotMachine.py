import random
import time

def EndScene():
    print("Narration:", "You ran out of money. Since the owner of this slot machine is satan himself, you see him appear from the depths of hell.")
    print("you - ", "OH MY GOODNESS HELP")
    print("satan -", "you're cooked buddy. you'll pay off that debt somehow.")
    print("*gets dragged to hell*")
    print("you died lmao")

PlayerMoney = 1000
while PlayerMoney > 0:
    print("Welcome to the vegas slot machine but local. You currently have $", PlayerMoney, "in your bank account.")
    Play1 = int(input("Press 1 to play. "))
    if Play1 == 1:
        PlayerMoney -= 20
        Number1 = random.randint(1,9)
        Number2 = random.randint(1,9)
        Number3 = random.randint(1,9)
        print(Number1)
        time.sleep(0.75)
        print(Number2)
        time.sleep(0.75)
        print(Number3)
        time.sleep(0.75)
        if Number1 == 7 and Number2 == 7 and Number3 == 7:
            PlayerMoney += 100
            print("YOU GOT A BIG JACKPOT OF $100! You now have $", PlayerMoney, "in your bank account.")
            Play2 = int(input("Press 1 to keep playing."))
            if Play2 == 1:
                time.sleep(0.25)
            else:
                print("you died lmao")
                break
        elif Number1 == Number2 == Number3:
            PlayerMoney += 50
            print("You won a small jackpot of $50! You now have $", PlayerMoney, "in your bank account.")
            Play3 = int(input("Press 1 to keep playing."))
            if Play3 == 1:
                time.sleep(0.25)
            else:
                print("you died lmao")
                break
        elif Number1 == Number2 or Number2 == Number3:
            PlayerMoney += 10
            print("You won a smaller jackpot of $10! You now have $", PlayerMoney, "in your bank account.")
            Play4 = int(input("Press 1 to keep playing."))
            if Play4 == 1:
                time.sleep(0.25)
            else:
                print("you died lmao")
                break
        else:
            print("sorry, you won nothing lol. dw, you still got $", PlayerMoney, "in ur bank account.")
            Play4 = int(input("Press 1 to keep playing."))
            if Play4 == 1:
                time.sleep(0.25)
            else:
                print("you died lmao")
                break
    else:
        print("You died lmao")
        break

EndScene()