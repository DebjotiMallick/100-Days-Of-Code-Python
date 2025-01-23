from Functions import add, subtract, multiply, divide
from Operations import operations

keep_calculating = True
while keep_calculating:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("+ - * /")
    symbol = input("Enter a symbol: ")
    operating_function = operations[symbol]
    answer = operating_function(num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")
    keep_calculate = input("Do you want to perform another calculation? yes/no: ").lower()
    if keep_calculate == "yes":
        keep_calculating = True
    else:
        keep_calculating = False
        print("Goodbye.")