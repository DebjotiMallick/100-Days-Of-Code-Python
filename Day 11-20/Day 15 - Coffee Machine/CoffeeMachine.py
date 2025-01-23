from MenuResources import MENU, resources

is_machine_off = False
money_earned = 0.0

while not is_machine_off:
    coffee_type = input("What would you like? espresso/latte/cappuccino: ").lower()
    updated_resources = resources
    can_make_coffee = True
    transaction_successful = False

    if coffee_type == "report":
        print(f"Water: {updated_resources['water']}")
        print(f"Milk: {updated_resources['milk']}")
        print(f"Coffee: {updated_resources['coffee']}")
        print(f"Money: {money_earned}")
        continue

    if coffee_type == "off":
        is_machine_off = True

    if coffee_type == "espresso":
        if updated_resources['water'] < MENU['espresso']['ingredients']['water']:
            print("Sorry there is not enough water.")
            can_make_coffee = False
        elif updated_resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            can_make_coffee = False

    if coffee_type == "latte":
        if updated_resources['water'] < MENU['latte']['ingredients']['water']:
            print("Sorry there is not enough water.")
            can_make_coffee = False
        elif updated_resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            can_make_coffee = False
        elif updated_resources['milk'] < MENU['latte']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            can_make_coffee = False

    if coffee_type == "cappuccino":
        if updated_resources['water'] < MENU['cappuccino']['ingredients']['water']:
            print("Sorry there is not enough water.")
            can_make_coffee = False
        elif updated_resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            can_make_coffee = False
        elif updated_resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            can_make_coffee = False

    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0

    if can_make_coffee:
        print("Insert coins.")
        quarters = int(input("How many quarters? : "))
        dimes = int(input("How many dimes? : "))
        nickles = int(input("How many nickles? : "))
        pennies = int(input("How many pennies? : "))

    value = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    if value < MENU[coffee_type]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        transaction_successful = True
        money_earned += MENU[coffee_type]['cost']
        if value > MENU[coffee_type]['cost']:
            change = value - MENU[coffee_type]['cost']
            print(f"${round(change, 2)} refunded.")

    if transaction_successful:
        updated_resources['water'] -= MENU[coffee_type]['ingredients']['water']
        updated_resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        updated_resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
        print(f"Here is your {coffee_type}, enjoy!")

