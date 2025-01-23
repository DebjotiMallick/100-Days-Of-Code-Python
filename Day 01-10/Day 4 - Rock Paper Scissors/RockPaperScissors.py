import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves = ["rock", "paper", "scissors"]
print("Rock Paper Scissors")

move = input("Play your move: Rock/Paper/Scissors ?\n")
move = move.lower()

computer = random.choice(moves)

print("You chose:\n")
if(move == "rock"):
    print(rock)
    print("Computer chose:\n")
    if(computer == "paper"):
        print(paper)
        print("You lost.")
    elif(computer == "rock"):
        print(rock)
        print("It's a draw.")
    else:
        print(scissors)
        print("You won.")
elif(move == "paper"):
    print(paper)
    print("Computer chose:\n")
    if (computer == "scissors"):
        print(scissors)
        print("You lost.")
    elif (computer == "paper"):
        print(paper)
        print("It's a draw.")
    else:
        print(rock)
        print("You won.")
elif(move == "scissors"):
    print(scissors)
    print("Computer chose:\n")
    if (computer == "rock"):
        print(rock)
        print("You lost.")
    elif (computer == "scissors"):
        print(scissors)
        print("It's a draw.")
    else:
        print(paper)
        print("You won.")
else:
    print("Invalid move.")

