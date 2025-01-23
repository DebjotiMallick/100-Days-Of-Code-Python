print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("Do you want to go left or right? ")
if(choice1.lower() == "right"):
    print("Game Over.")
elif(choice1.lower() == "left"):
    choice2 = input("Do you want to swim or wait? ")
    if(choice2.lower() == "swim"):
        print("Game Over.")
    elif(choice2.lower() == "wait"):
        choice3 = input("Which door? red, yellow or blue? ")
        if (choice3.lower() == "red" or choice3.lower() == "blue"):
            print("Game Over.")
        elif(choice3.lower() == "yellow"):
            print("You Win!")
        else:
            print("Incorrect choice, game over.")
    else:
        print("Incorrect choice, game over.")
else:
    print("Incorrect choice, game over.")