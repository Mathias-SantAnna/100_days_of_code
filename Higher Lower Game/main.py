# TO DOs:
#1 Display art, 
from art import logo
from data import data
import random

score = 0

#2 Generate random options for user to choose from game data
def deal_account():
    option1 = random.choice(data)
    option2 = random.choice(data)
    # To avoid choosing the same account twice
    while option1 == option2:
        option2 = random.choice(data)
    return option1, option2


#3 Format account data into printable format
def display_accounts(account_a, account_b):
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

#4 Ask the user who has more followers
def get_user_guess():
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    while user_guess not in ['A', 'B']:
        print("Invalid input. Please type 'A' or 'B'.")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return user_guess

#5 Compare A against B function 
def compare(account_a, account_b, user_guess, score):
    if account_a['follower_count'] > account_b['follower_count'] and user_guess == 'A':
        score += 1
        print(f"You're right! Current score: {score}")
    elif account_a['follower_count'] < account_b['follower_count'] and user_guess == 'B':
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return score, False  # Return False to stop the game
    return score, True  # Return True to continue the game

# Main game loop
def play_game():
    global score  # Global score to keep it across rounds
    account_a, account_b = deal_account()
    
    display_accounts(account_a, account_b)
    user_guess = get_user_guess()
    
    score = compare(account_a, account_b, user_guess, score)

# Call the game Test
play_game()


#6 Return result and keep it


#7 Make repeatable 

#8 Make account at position B become the next account at position A