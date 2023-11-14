import random
from os import system, name
from blackjack_project_art import logo

def clear(): 
    _ = system('clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

def compare(user_score, cpu_score):
        if user_score == 0:
            return "Win with a Blackjack"
        elif cpu_score == 0:
            return "Lose, opponent has Blackjack"
        elif user_score > 21:
            return "You went over. You lose"
        elif cpu_score > 21:
            return "Opponent went over. You win"
        elif user_score == cpu_score:
            return "Draw"
        elif user_score > cpu_score:
            return "You win"
        else:
            return "You lose"

def play_game():

    print(logo)

    user_cards = []
    cpu_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: [{cpu_cards[0]}, 🂠]")
        if user_score == 0 or cpu_score == 0 or user_score > 21:
            is_game_over = True
        else:
            call_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if call_card == 'y':    
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)

    print(f"    Player's final cards: {user_cards}, final score: {user_score}")
    print(f"    Computer's final cards: {cpu_cards}, final score: {cpu_score}")
    print(compare(user_score, cpu_score))

clear()
while input("Would you like to play Blackjack? Type 'y' or 'n': ").lower() == "y":
    clear()
    play_game()
