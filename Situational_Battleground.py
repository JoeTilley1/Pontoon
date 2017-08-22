__author__ = 'Joe'
from random import randint

games_playing = int(input("How many games are to be played: "))
five_card_games_played = 0
games_played = 0
draws = 0
AI1_wins = 0
AI2_wins = 0
AI1_busts = 0
AI2_busts = 0

while games_played < games_playing:

    situation1 = False
    situation2 = False

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

    # Defining AI1
    def ai_choice(cards_drawn, score):
        if score == 17 and cards_drawn == 3 and len(Six) == 2 and len(Five) == 3:
                return 'twist'
        if score >= 17:
            return 'stick'
        else:
            return 'twist'

    def ai1_ace_choice(score):
        if score+10 <= 21:
            return '11'
        else:
            return '1'

    # AI1 starts to play
    AI1_score = 0
    AI1_cards_drawn = 0
    choice = 'twist'                                                                                                    # To enter the while loop qualifier
    while choice == 'twist' or AI1_cards_drawn < 2:

        # Randomly generating the card number
        i = randint(0, int(len(cards_list))-1)                                                                          # Generates random number for drawn card's index
        card_drawn_number = cards_list[i]                                                                               # Defines drawn card's number
        while cards_left[card_drawn_number] == 0:                                                                       # Checks if there are any suits left of that number
            i = randint(0, int(len(cards_list))-1)                                                                      # If not, regenerates new random number if none left
            card_drawn_number = cards_list[i]                                                                           # And redefines drawn card's number
        cards_left[card_drawn_number] += -1                                                                             # Decreases drawn card's count by 1

        # Finding the card suit
        for key in card_deck:                                                                                           # For every number in the card deck
            if card_drawn_number == key:                                                                                # If the card's number matches it, then
                j = randint(0, int(len(card_deck[key]))-1)                                                              # Generate a random number to be its index in its suit list
                card_drawn_suit = card_deck[key][j]                                                                     # Define drawn card's suit
                card_deck[key].remove(card_drawn_suit)                                                                  # Remove that suit from its suit list
                AI1_score += card_number_value[key]                                                                     # Increase current score by correct amount

        AI1_cards_drawn += 1                                                                                            # Increases cards drawn tally by 1
        AI1_aces_drawn = 4-len(Ace)                                                                                     # Defines how many aces player has drawn (ignore error)
        if AI1_cards_drawn == 1:                                                                                        # For first card drawn (this part is so the AI Magnus will work)
            AI1_first_card_number = card_drawn_number                                                                   # Save the number of the card
        elif AI1_cards_drawn == 2:                                                                                      # For second card drawn
            AI1_second_card_number = card_drawn_number                                                                  # Save the number of the card


        # If statement to check if busted and asks stick/twist
        if AI1_score > 21:
            AI1_score = "Bust!"
            break
        else:
            if (AI1_score == 17 and AI1_cards_drawn == 3 and len(Six) == 2 and len(Five) == 3):
                situation1 = True
            if AI1_cards_drawn >= 2:                                                                                    # If statement to ensure at least two cards always drawn
                choice = ai_choice(AI1_cards_drawn, AI1_score)                                                          # Input of stick or twist (error catching not needed)
    else:
        # Finished drawing cards
        for n in range(1,5,1):                                                                                          # Makes n equal 1, then 2, 3, 4
            if AI1_aces_drawn >= n:                                                                                     # If you have N or more aces
                ace_choice = ai1_ace_choice(AI1_score)                                                                  # Input value wanted (error catching not needed)
                if ace_choice == '11':                                                                                  # If '11' selecting
                    AI1_score += 10                                                                                     # Add 10 to the original 1 score (to make 11)
                elif ace_choice == '1':                                                                                 # If '1' selecting
                    pass                                                                                                # Add 0 to the original 1 score (to make 1)
            else:                                                                                                       # If you don't have N or more aces
                break                                                                                                   # Don't bother trying higher N's

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

    # Defining AI2
    def ai2_choice(score):
        if score >= 17:
            return 'stick'
        else:
            return 'twist'

    def ai2_ace_choice(score):
        if score+10 <= 21:
            return '11'
        else:
            return '1'

    # AI2 starts to play
    AI2_score = 0
    AI2_cards_drawn = 0
    choice = 'twist'                                                                                                    # To enter the while loop qualifier
    while choice == 'twist' or AI2_cards_drawn < 2:

        # Randomly generating the card number
        i = randint(0, int(len(cards_list))-1)                                                                          # Generates random number for drawn card's index
        card_drawn_number = cards_list[i]                                                                               # Defines drawn card's number
        while cards_left[card_drawn_number] == 0:                                                                       # Checks if there are any suits left of that number
            i = randint(0, int(len(cards_list))-1)                                                                      # If not, regenerates new random number if none left
            card_drawn_number = cards_list[i]                                                                           # And redefines drawn card's number
        cards_left[card_drawn_number] += -1                                                                             # Decreases drawn card's count by 1

        # Finding the card suit
        for key in card_deck:                                                                                           # For every number in the card deck
            if card_drawn_number == key:                                                                                # If the card's number matches it, then
                j = randint(0, int(len(card_deck[key]))-1)                                                              # Generate a random number to be its index in its suit list
                card_drawn_suit = card_deck[key][j]                                                                     # Define drawn card's suit
                card_deck[key].remove(card_drawn_suit)                                                                  # Remove that suit from its suit list
                AI2_score += card_number_value[key]                                                                       # Increase current score by correct amount

        AI2_cards_drawn += 1                                                                                            # Increases cards drawn tally by 1
        AI2_aces_drawn = 4-len(Ace)                                                                                     # Defines how many aces player has drawn (ignore error)
        if AI1_cards_drawn == 1:                                                                                        # For first card drawn (this part is so the AI Magnus will work)
            AI2_first_card_number = card_drawn_number                                                                   # Save the number of the card
        elif AI1_cards_drawn == 2:                                                                                      # For second card drawn
            AI2_second_card_number = card_drawn_number                                                                  # Save the number of the card


        # If statement to check if busted and asks stick/twist
        if AI2_score > 21:
            AI2_score = "Bust!"
            break
        else:
            if (AI1_score == 17 and AI1_cards_drawn == 3 and len(Six) == 2 and len(Five) == 3):
                situation1 = True
            if AI2_cards_drawn >= 2:                                                                                    # If statement to ensure at least two cards always drawn
                choice = ai2_choice(AI2_score)                                                                          # Input of stick or twist (error catching not needed)
    else:
        # Finished drawing cards
        for n in range(1,5,1):                                                                                          # Makes n equal 1, then 2, 3, 4
            if AI2_aces_drawn >= n:                                                                                     # If you have N or more aces
                ace_choice = ai2_ace_choice(AI2_score)                                                                  # Input value wanted (error catching not needed)
                if ace_choice == '11':                                                                                  # If '11' selecting
                    AI1_score += 10                                                                                     # Add 10 to the original 1 score (to make 11)
                elif ace_choice == '1':                                                                                 # If '1' selecting
                    pass                                                                                                # Add 0 to the original 1 score (to make 1)
            else:                                                                                                       # If you don't have N or more aces
                break

    if situation1 is True or situation2 is True:
        five_card_games_played += 1
        if AI1_score == "Bust!":
            AI1_busts += 1
        if AI2_score == "Bust!":
            AI2_busts += 1
        if AI1_score == AI2_score:                                                                                      # If equal sscores
            draws += 1
        elif AI1_score == "Bust!":                                                                                      # If you bust (and AI doesnt, caught in previous if statement)
            AI2_wins += 1
        elif AI2_score == "Bust!":                                                                                      # If AI bust (and player doesnt, caught in first if statement)
            AI1_wins += 1
        elif AI2_score > AI1_score:                                                                                     # If neither bust and AI scores higher
            AI2_wins += 1
        elif AI1_score > AI2_score:                                                                                     # If neither bust and player scores higher
            AI1_wins += 1
        games_played += 1

    games_played += 1

print("Games played: "+str(games_played))
print("Situation games played: "+str(five_card_games_played))
print("AI1 wins: "+str(AI1_wins))
print("AI2 wins: "+str(AI2_wins))
print("Draws: "+str(draws))
print("AI1 busts: "+str(AI1_busts))
print("AI2 busts: "+str(AI2_busts))