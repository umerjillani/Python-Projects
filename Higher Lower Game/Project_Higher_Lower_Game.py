from art import Higher_Lower_logo
import random 
import os 
from game_data import data
clear = lambda: os.system('cls')

def select_random_account():
    """Selects a random account from the game data."""
    return random.choice(data)

def formate_data(account):
    """Formate the game data in printable."""
    name = account['name']
    description = account["description"]
    country = account["country"]
    
    return f"{name}, a {description}, from {country}"

def validate_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

#main body 
print(Higher_Lower_logo)

score = 0
should_continue = True

account_b = select_random_account()   

while should_continue:
    
    account_a = account_b
    account_b = select_random_account()
    if account_a == account_b: 
        account_b = select_random_account() 

    a_followers_count = account_a["follower_count"] 
    b_followers_count = account_b["follower_count"] 

    print(f"A: {formate_data(account_a)}\n")
    print(f"B: {formate_data(account_b)}\n") 

    user_guess = input("Enter your choice, 'A' or 'B': ").lower()

    is_correct = validate_answer(user_guess, a_followers_count, b_followers_count) 

    clear() 
    print(Higher_Lower_logo)
        
    if is_correct:
        score += 1
        print(f"\n======================================\nYou guessed it Right! Your score is {score}.\n======================================\n\n")
    else:
        print(f"\n======================================\nYou failed! Your Final score is {score}.\n======================================")     
        should_continue = False 