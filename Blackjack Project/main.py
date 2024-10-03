from art import logo;
import random

def deal_card():
    """Returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    #check for blackjack a hand with only 2 cards and return 0 instead of actual score
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    #check for an 11 (ace) if score is over 21 replace it with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
"""
def game():
    print(logo)
    print("\nWelcome to Blackjack, Do you want to start? Type 'y' or 'no': ")

    #input("Type 'y' to get another card, type 'no'to pass: ")
game()
"""