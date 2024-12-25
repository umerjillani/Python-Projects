import Resources_Data

def formate_resources(resources):
    
    return f"===============\nWater : {Resources_Data.resources["water"]} mg\nMilk : {Resources_Data.resources["milk"]} mg\nCoffee : {Resources_Data.resources["coffee"]} mg\nMoney : {Resources_Data.resources["money"]} $\n==============="



def resource_checker(ingredients_dict):
    for item in ingredients_dict:
        if ingredients_dict[item] > Resources_Data.resources[item]: 
            print(f"Sorry, not enough {item}, {ingredients_dict[item] - Resources_Data.resources[item]} ml more {item} is required.")
            return False 
    return True   


def process_coins():
    print("\n\nPlease Enter the coins, You have.")
    
    balance = 0
    balance = int(input("How many Dollars? : "))  
    balance += int(input("How many Quarters (0.25 $)? : ")) * 0.25
    balance += int(input("How many dimes (0.1 $)? : ")) * 0.1
    balance += int(input("How many nickels (0.05 $ )? : ")) * 0.05
    balance += int(input("How many pennies (0.01 $)? : ")) * 0.01
    
    return balance 


def transaction_process(money_received, drink_cost):
    if money_received >= drink_cost:
        
        Resources_Data.resources["money"] += drink_cost 
        
        change = round(money_received - drink_cost , 2) 
        print(f"\n==========================\nHere are {change}$ in change.\n==========================")  
        return True
    else:
        print(f"\n\n=================\nSorry, not enough money. {drink_cost - money_received} $ more money is required.\n=================") 
        return False


def make_coffee_ready(drink_name, drink_ingredients):
    for i in drink_ingredients:
        Resources_Data.resources[i] -= drink_ingredients[i] 
        
    print(f"\n==================================\nHere is your {drink_name}. Enjoy!\n==================================\n")  
    
    


# main body

next_customer = True

while next_customer:
    user_choice = input("What would you like? ( Espresso/  Latte /  Cappuccino): ").lower()
    
    if user_choice == "off":
        break 
    elif user_choice == "report":
        print(formate_resources(Resources_Data.resources))   
    else:
        drink = Resources_Data.MENU[user_choice] 

        if resource_checker(drink["ingredients"]):
            payment = process_coins() 
            
            if transaction_process(payment, drink["cost"]):
                make_coffee_ready(user_choice , drink["ingredients"])
            