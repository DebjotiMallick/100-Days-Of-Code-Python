print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))

percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split the bill? "))

# split = "{:.2f}".format((total + percentage * total / 100) / people)
split = (total + percentage * total / 100) / people

print(f"Each person should pay: ${split:.2f}")