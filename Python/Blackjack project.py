############### Blackjack Project #####################

import random

# Define the deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Return a random card from the deck."""
    return random.choice(cards)

def calculate_score(hand):
    """Calculate the score of a hand. Handle Ace as 11 or 1."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    
    return sum(hand)

def blackjack_game():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    game_over = False
    
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")
        
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
            if should_continue == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True
    
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
    
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    
    if player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score == 0:
        return "Blackjack! You win!"
    elif dealer_score == 0:
        return "Dealer got a blackjack. You lose!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

# Start the game
print("Welcome to Blackjack!")
while input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ").lower() == 'y':
    print("\n" + blackjack_game())
    