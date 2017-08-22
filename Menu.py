__author__ = 'Joe'
 
again = 'y'
print("RULES")
print("")
print("This is a system which allows you to play pontoon against an AI.")
print("Pontoon is similar to blackjack. Each player receives two cards, then chooses to draw another or stick with the score they have.")
print("If they score over 21, they automatically lose. ")
print("Aces count as a score of either 1 or 11 to be chosen by the player once they declare they have stopped drawing cards.")
print("There are no splits, and the five-card-trick rule is not active.")
print("")
while again == 'y':
    start_choice = str(input("Do you want to play first? Enter (y/n): "))
    while start_choice != 'y' and start_choice != 'n':
        start_choice = str(input("That's not a valid answer, type 'y' or 'n' exactly. Enter again: "))
    if start_choice == 'y':
        print("")
        import AI_goes_second
    else:
        print("")
        import AI_goes_first
    print("")
    again = str(input("Do you want to play again? Enter (y/n): "))
    while again != 'y' and start_choice != 'n':
        again = str(input("That's not a valid answer, type 'y' or 'n' exactly. Enter again: "))
else:
    print("")
    print("You have finished playing pontoon with the AI.")
