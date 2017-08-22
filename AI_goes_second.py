__author__ = 'Joe'
from random import randint

# Creating the initial setup
cards_left = {'2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, '10': 4, 'J': 4, 'Q': 4, 'K': 4, 'A': 4}
Two = ['H', 'D', 'C', 'S']
Three = ['H', 'D', 'C', 'S']
Four = ['H', 'D', 'C', 'S']
Five = ['H', 'D', 'C', 'S']
Six = ['H', 'D', 'C', 'S']
Seven = ['H', 'D', 'C', 'S']
Eight = ['H', 'D', 'C', 'S']
Nine = ['H', 'D', 'C', 'S']
Ten = ['H', 'D', 'C', 'S']
Jack = ['H', 'D', 'C', 'S']
Queen = ['H', 'D', 'C', 'S']
King = ['H', 'D', 'C', 'S']
Ace = ['H', 'D', 'C', 'S']
# A more sophisticated deck introduced to aid finding and fixing card suits
card_deck = {'2': Two, '3': Three, '4': Four, '5': Five, '6': Six, '7': Seven, '8': Eight, '9': Nine, '10': Ten, 'J': Jack, 'Q': Queen, 'K': King, 'A': Ace}
# Defines card values (Ace contributes as 1 to current score to prevent avoidable busts)
card_number_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
# Creates a basic list of card numbers
cards_list = list(card_deck.keys())

# Player starts the game
print("You will start first. Here are your first two cards:")
player_score = 0
player_cards_drawn = 0
choice = 'twist'                                                                                                        # To enter the while loop qualifier
while choice == 'twist' or player_cards_drawn < 2:

    # Randomly generating the card number
    i = randint(0, int(len(cards_list))-1)                                                                              # Generates random number for drawn card's index
    card_drawn_number = cards_list[i]                                                                                   # Defines drawn card's number
    while cards_left[card_drawn_number] == 0:                                                                           # Checks if there are any suits left of that number
        i = randint(0, int(len(cards_list))-1)                                                                          # If not, regenerates new random number if none left
        card_drawn_number = cards_list[i]                                                                               # And redefines drawn card's number
    cards_left[card_drawn_number] += -1                                                                                 # Decreases drawn card's count by 1

    # Finding the card suit
    for key in card_deck:                                                                                               # For every number in the card deck
        if card_drawn_number == key:                                                                                    # If the card's number matches it, then
            j = randint(0, int(len(card_deck[key]))-1)                                                                  # Generate a random number to be its index in its suit list
            card_drawn_suit = card_deck[key][j]                                                                         # Define drawn card's suit
            card_deck[key].remove(card_drawn_suit)                                                                      # Remove that suit from its suit list
            player_score += card_number_value[key]                                                                      # Increase current score by correct amount

    player_cards_drawn += 1                                                                                             # Increases cards drawn tally by 1
    print(card_drawn_number+card_drawn_suit)                                                                            # Displays the drawn card (ignore error, it is always defined)
    player_aces_drawn = 4-len(Ace)                                                                                      # Defines how many aces player has drawn
    if player_cards_drawn == 1:                                                                                         # For first card drawn (this part is so the AI Magnus will work)
        player_first_card_number = card_drawn_number                                                                    # Save the number of the card
    elif player_cards_drawn == 2:                                                                                       # For second card drawn
        player_second_card_number = card_drawn_number                                                                   # Save the number of the card



    # If statement to check if busted and asks stick/twist
    if player_score > 21:
        print("You have bust!")
        print("")
        break
    else:
        if player_cards_drawn >= 2:                                                                                     # If statement to ensure at least two cards always drawn
            choice = str(input("Stick or twist: ")).lower()                                                             # Input of stick or twist
            while choice != 'stick' and choice != 'twist':                                                              # Error catching in stick or twist answer
                choice = str(input("That's not a valid answer, type 'stick' or 'twist' exactly. Enter again: ")).lower()
else:
    # Finished drawing cards
    for n in range(1,5,1):                                                                                              # Makes n equal 1, then 2, 3, 4
        if player_aces_drawn >= n:                                                                                      # If you have N or more aces
            ace_choice = str(input("Do you want your ace to count as 1 or 11? Enter '1' or '11': "))                    # Input value wanted
            while ace_choice != '1' and ace_choice != '11':                                                             # Error catching
                ace_choice = str(input("That's not a valid answer, type '1' or '11' exactly. Enter again: "))
            if ace_choice == '11':                                                                                      # If '11' selecting
                player_score += 10                                                                                      # Add 10 to the original 1 score (to make 11)
            elif ace_choice == '1':                                                                                     # If '1' selecting
                pass                                                                                                    # Add 0 to the original 1 score (to make 1)
        else:                                                                                                           # If you don't have N or more aces
            break                                                                                                       # Don't bother trying higher N's
    print("")
    print("You have finally stuck. Your score was: "+str(player_score))                                                 # Displays player's score
    print("")

# Defining the AI
def ai_choice(score, aces):
    if player_score > 21:
        return 'stick'
    else:
        if score >= 17:
            return 'stick'
        else:
            if aces >= 1:
                if 21 >= score >= 19:
                    return 'stick'
                else:
                    return 'twist'
            else:
                return 'twist'

def ai_ace_choice(score):
        if score+10 <= 21:
            return '11'
        else:
            return '1'

# AI starts to play
print("The AI will now play. It will show all the cards it receives and the choices it makes. Here is its first two cards:")
AI_score = 0
AI_cards_drawn = 0
choice = 'twist'                                                                                                        # To enter the while loop qualifier
while choice == 'twist' or AI_cards_drawn < 2:

    # Randomly generating the card number
    i = randint(0, int(len(cards_list))-1)                                                                              # Generates random number for drawn card's index
    card_drawn_number = cards_list[i]                                                                                   # Defines drawn card's number
    while cards_left[card_drawn_number] == 0:                                                                           # Checks if there are any suits left of that number
        i = randint(0, int(len(cards_list))-1)                                                                          # If not, regenerates new random number if none left
        card_drawn_number = cards_list[i]                                                                               # And redefines drawn card's number
    cards_left[card_drawn_number] += -1                                                                                 # Decreases drawn card's count by 1

    # Finding the card suit
    for key in card_deck:                                                                                               # For every number in the card deck
        if card_drawn_number == key:                                                                                    # If the card's number matches it, then
            j = randint(0, int(len(card_deck[key]))-1)                                                                  # Generate a random number to be its index in its suit list
            card_drawn_suit = card_deck[key][j]                                                                         # Define drawn card's suit
            card_deck[key].remove(card_drawn_suit)                                                                      # Remove that suit from its suit list
            AI_score += card_number_value[key]                                                                            # Increase current score by correct amount

    AI_cards_drawn += 1                                                                                                 # Increases cards drawn tally by 1
    print(card_drawn_number+card_drawn_suit)                                                                            # Displays the drawn card (ignore error, it is always defined)
    AI_aces_drawn = 4-player_aces_drawn-len(Ace)                                                                        # Defines how many aces player has drawn (ignore error)

    # If statement to check if busted and asks stick/twist
    if AI_score > 21:
        print("The AI has bust!")
        break
    else:
        if AI_cards_drawn >= 2:                                                                                         # If statement to ensure at least two cards always drawn
            choice = ai_choice(AI_score, AI_aces_drawn)                                                                 # Input of stick or twist (error catching not needed)
            print("The AI has decided to "+choice)                                                                      # Shows the AI's choice of stick or twist
else:
    # Finished drawing cards
    for n in range(1,5,1):                                                                                              # Makes n equal 1, then 2, 3, 4
        if AI_aces_drawn >= n:                                                                                          # If you have N or more aces
            ace_choice = ai_ace_choice(AI_score)                                                                        # Input value wanted (error catching not needed)
            if ace_choice == '11':                                                                                      # If '11' selecting
                AI_score += 10                                                                                          # Add 10 to the original 1 score (to make 11)
            elif ace_choice == '1':                                                                                     # If '1' selecting
                pass                                                                                                    # Add 0 to the original 1 score (to make 1)
        else:                                                                                                           # If you don't have N or more aces
            break                                                                                                       # Don't bother trying higher N's
    print("")
    print("The AI has finally stuck. Its score was: "+str(AI_score))                                                    # Displays AI's score

# Final results
print("")
if player_score > 21:                                                                                                   # Make player score 'Bust!' if bust
    player_score = "Bust!"
if AI_score > 21:                                                                                                       # Make AI score 'Bust!' if bust
    AI_score = "Bust!"
print("The final results were:")                                                                                        # Display results
print("You: " + str(player_score))
print("AI: " + str(AI_score))
print("")
if player_score == AI_score:                                                                                            # If equal sscores
    print("You drew.")
elif player_score == "Bust!":                                                                                           # If you bust (and AI doesnt, caught in previous if statement)
    print("The AI wins.")
elif AI_score == "Bust!":                                                                                               # If AI bust (and player doesnt, caught in first if statement)
    print("You win!")
elif AI_score > player_score:                                                                                           # If neither bust and AI scores higher
    print("The AI wins.")
elif player_score > AI_score:                                                                                           # If neither bust and player scores higher
    print("You win!")
