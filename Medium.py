# FIND THE ERROR (MEDIUM)
# NUMBER OF ERRORS THAT CRASH THE PROGRAM: 1
# NUMBER OF ERRORS TOTAL: 5

import random
p1WinCount = 0
comWinCount = 0

while True:
    while True:
        p1 = input("Please Choose Rock, Paper, or Scissors\n").lower()
        if not (p1 == "rock" or p1 == "r" or p1 == "scissors" or p1 == "s" or p1 == "paper" or p1 == "p"):
            print("Invalid statement, try again\n")
            continue

    # Rock = 0, Paper = 1, Scissors = 2
    com = random.randint(0, 2)

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

    elif cam == 1:
        print("Paper")

        if p1 == "rock" and p1 == "r":
            print("You Lose")
            comWinCount += 1
        elif p1 == "paper" and p1 == "p":
            print("Tie")
        else:
            print("You Win!")
            p1WinCount += 1

    else:
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
        if not (play_again == "no" or play_again == "n"):
            break

    elif comWinCount == 2:
        print("\nYou Lose " + str(p1WinCount) + "- " + str(comWinCount))

        play_again = input("Play Again (Y/N)?").lower()
        if play_again == "no" or play_again == "n":
            break





