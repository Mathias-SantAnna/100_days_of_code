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

# Function to display a final message based on the final score
def display_final_message(final_score):
    if final_score == 0:
        print("\nThat‘s a terrible score. 🫠 The average score is 3.2. Put some effort into it.")
    elif final_score < 5:
        print(f"\nErrr Ops!🫣  You scored: {final_score}. Keep practicing! ")
    elif final_score < 10:
        print(f"\nGreat! You scored: {final_score}.👏 You are pretty good! That‘s a score worth sharing ")
    elif final_score < 16:
        print(f"\Excellent!You scored: {final_score}.💪 You're a true master of the Higher Lower Game!🐐")
    else:
        print(f"\nWooooow Amazing! You scored {final_score}! your ahead of 99% of all people. Tell me now, how did you cheated? 🤨")

# Function to ask the user if they want to play again
def ask_to_play_again():
    play_again = input("\nDo you want to play again? Type 'Y' for Yes or 'N' for No: ").upper()
    while play_again not in ['Y', 'N']:
        print("Invalid input. Please type 'Y' or 'N'.")
        play_again = input("\nDo you want to play again? Type 'Y' for Yes or 'N' for No: ").upper()
    return play_again == 'Y'
    
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
    
    # Display final message based on score
    display_final_message(score)
    
    # Ask if the user
    if ask_to_play_again():
        score = 0  # Reset the score for the new game
        play_game()  # Restart the game
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
play_game()