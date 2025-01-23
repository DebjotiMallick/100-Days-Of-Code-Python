import random, os

play_again = True
while play_again:
    print("Welcome to the number guessing game.")
    print("I am thinking a number between 1 and 100.")
    choice = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    computer_guess = random.randint(1, 101)
    if choice == "easy":
        chances = 10
    elif choice == "hard":
        chances = 5
    else:
        print("Wrong choice.")

    while chances != 0:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > computer_guess:
            print("Too high, try again.")
        elif guess < computer_guess:
            print("Too low, try again.")
        else:
            print("Correct guess, you won.")
            break
        chances -= 1
        if chances == 0:
            print("Out of attempts, you lost.")

    play = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play == "yes":
        play_again = True
        os.system('cls')
    elif play == "false":
        play_again = False
    else:
        print("Incorrect choice.")