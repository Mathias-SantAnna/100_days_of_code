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
    print(f"\nCompare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
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
#6 Return and keep result
        return score, False  # Stop the game
    return score, True  # Continue the game


def play_game():
    global score  # use Global score to keep it across rounds
    print(logo)  
    
    # Initial accounts
    account_a, account_b = deal_account()

#7 Make repeatable 
    game_should_continue = True
    while game_should_continue:
        # Display the current accounts for comparison
        display_accounts(account_a, account_b)
        
        user_guess = get_user_guess()
        
        # Compare and update score
        score, game_should_continue = compare(account_a, account_b, user_guess, score)

#8 Make account at position B become the next account at position A
        account_a = account_b
        account_b = random.choice(data)
        
        # Ensure account_b is different from account_a
        while account_a == account_b:
            account_b = random.choice(data)
    
    print("\nGame Over!")
    print(f"Your final score is {score}.")

# Start the game
play_game()game
play_game()