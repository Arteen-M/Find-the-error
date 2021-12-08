# FIND THE ERROR (EASY)
# NUMBER OF ERRORS THAT CRASH THE PROGRAM: 1
# NUMBER OF ERRORS TOTAL: 3
import random
p1WinCount = 0
comWinCount = 0

while True:
    p1 = input("Please Choose Rock, Paper, or Scissors\n").upper()
    if not (p1 == "rock" or p1 == "r" or p1 == "scissors" or p1 == "s" or p1 == "paper" or p1 == "p"):
        print("Invalid statement, try again\n")
        continue

    # Rock = 0, Paper = 1, Scissors = 2
    com = random.randint(0, 3)

    if com == 0:
        print("Rock")

        if p1 == "rock" or p1 == "r":
            print("Tie")
        elif p1 == "paper" or p1 == "p":
            print("You Win!")
            p1WinCount += 1
        else:
            print("You Lose")
            comWinCount += 1

    elif com == 1:
        print("Paper")

        if p1 == "rock" or p1 == "r":
            print("You Lose")
            comWinCount += 1
        elif p1 == "paper" or p1 == "p":
            print("Tie")
        else:
            print("You Win!")
            p1WinCount += 1

    elif com == 2:
        print("Scissors")

        if p1 == "rock" or p1 == "r":
            print("You Win!")
            p1WinCount += 1
        elif p1 == "paper" or p1 == "p":
            print("You Lose")
            comWinCount += 1
        else:
            print("Tie")

    if p1WinCount == 2:
        print("\nYou Win " + str(p1WinCount) + "- " + str(comWinCount))

        play_again = input("Play Again (Y/N)?").lower()
        if play_again == "no" or play_again == "n":
            break
        else:
            p1WinCount = 0
            comWinCount = 0

    elif comWinCount == 2:
        print("\nYou Lose " + str(p1WinCount) + "- " + comWinCount)

        play_again = input("Play Again (Y/N)?").lower()
        if play_again == "no" or play_again == "n":
            break
        else:
            p1WinCount = 0
            comWinCount = 0






