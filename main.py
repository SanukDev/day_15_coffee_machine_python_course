from menu_data import MENU, resources


def check_resources(drink_choice):
    """this function  check the resources"""
    if drink_choice != 'off':
        if drink_choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}ml")
        else:
            water_resources = resources['water']
            coffee_resources = resources['coffee']
            water_choice = MENU[drink_choice]['ingredients']['water']
            if drink_choice == 'cappuccino' or drink_choice == 'latte':
                milk_choice = MENU[drink_choice]['ingredients']['milk']
                milk_resources = resources['milk']
                if milk_choice > milk_resources:
                    print(f"Sorry there is not enough milk")
            coffee_choice = MENU[drink_choice]['ingredients']['coffee']
            if water_choice > water_resources:
                print(f"Sorry there is not enough water")
            elif coffee_choice > coffee_resources:
                print(f"Sorry there is not enough coffee")
            else:
                return 0


def calculate_coins(quarter, dimes, nickles, pennies):
    """This function calculate the coins"""
    total = quarter * QUARTER + dimes * DIMES + nickles * NICKLES + pennies * PENNIES
    return total

def check_transaction(total,drink_choice):
    """The function validate the buy of the coffee"""
    value_coffe = MENU[drink_choice]['cost']
    if total < value_coffe:
        print("Sorry that's not enough money. Money refunded")
    elif total >= value_coffe:
        return_money = total - value_coffe
        resources['money'] = value_coffe
        print(f"Here is {return_money:.2f} dollars in change.")
        return 0
def use_resources(transaction_true, drink_choice):
    """this function use the resources avalable"""
    if transaction_true == 0:
        water_choice = MENU[drink_choice]['ingredients']['water']
        coffee_choice = MENU[drink_choice]['ingredients']['coffee']
        if drink_choice == 'cappuccino' or drink_choice == 'latte':
            milk_choice = MENU[drink_choice]['ingredients']['milk']
            resources['milk'] -= milk_choice
        resources['water'] -= water_choice
        resources['coffee'] -= coffee_choice
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {resources['money']:.2f}")

def end_game_func(drink_choice):
    """checks whether user wants turn off the coffee machine"""
    if drink_choice == 'off':
        return 1

# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
QUARTER = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
end_game = False
while end_game == False:
    drink_choice = str(input("What would you like? (espresso/latte/cappuccino)"))
    ver = check_resources(drink_choice)
    end_game_check = end_game_func(drink_choice)
    if end_game_check == 1:
        end_game = True
    else:
        if ver == 0:
            quarter = int(input("How many quaters? :"))
            dimes = int(input("How many dimes? :"))
            nickles = int(input("How many nickles? :"))
            pennies = int(input("How many pennies? :"))
            total = calculate_coins(quarter, dimes, nickles, pennies)
            transaction_true = check_transaction(total,drink_choice)
            if transaction_true == 0:
                use_resources(transaction_true,drink_choice)
                for x in MENU:
                    if x == drink_choice:
                        print(f"Here is your {x}. Enjoy")

