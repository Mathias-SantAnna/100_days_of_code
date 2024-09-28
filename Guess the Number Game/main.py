from random import randint
from art import logo, win

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def restart():
            play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
            if play_again == 'yes':
                game()
            else:
                print("Thanks for playing! Goodbye.")
                return

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("\nToo high.")
        return turns -1
    elif user_guess < actual_answer:
        print("\nToo low.")
        return turns -1
    else:
        print(win)
        print(f"The answer was {actual_answer}")
        restart()


def set_difficulty():
    level = input("Choose a difficulty, Type 'easy or hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number guessing game!")
    print("I'm thinking of a number between 1 and 100")

    answer = randint(1, 100)    
    #print(f"Pssst, the correct answer is {answer}.")

    turns =  set_difficulty()
  
    guess = 0
    while guess != answer:
        
        print(f"You have {turns} attempts remaining to guess the correct number.\n")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you loose.\n")
            restart()
        elif guess != answer:
            print ("Guess again.")


game()