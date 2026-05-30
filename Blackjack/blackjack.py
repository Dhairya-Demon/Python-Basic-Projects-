import art

choice = input("Type 'y' if you want to play the game of blackjack otherwise 'n'...")
if choice == "y":
     game = True
else:
    game = False

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
import random

while game is True:
    print(art.logo)
    your_cards = [random.choice(cards),random.choice(cards)]
    current_score = your_cards[0] + your_cards[1]
    print(f"Your cards : {your_cards}")
    print(f"current score  :  {current_score}")
    computer_first_card = random.choice(cards)
    print(f" computer's first card is : {computer_first_card}")
    Hit = input("type 'y' to get another card , type 'n' to pass ")
    if Hit == "y":
        your_cards = [your_cards[0],your_cards[1],random.choice(cards)]
        current_score += your_cards[2]
        if current_score > 21:
            print("SINCE ITS A BUST SO .....")
            print("YOU LOSE ")
            print("\n" * 30)
        else:
            print(f"your cards are : {your_cards}")
            print(f"your score are : {current_score}")
            computer_second_card = random.choice(cards)
            print(f"computer's second card is : {computer_second_card}")
            print(f"computers hand is : [{computer_first_card},{computer_second_card}] ")
            computer_hand = [computer_first_card,computer_second_card]
            computer_score = computer_hand[0] + computer_hand[1]
            print(f"computer's score is : {computer_score}")
            if computer_score > current_score:
                print("YOU LOSE")
                print("\n" * 30)
            else:
                print("YOU WIN ")
                print("\n" * 30)
    else:
        computer_second_card = random.choice(cards)
        print(f"computer's second card is : {computer_second_card}")
        print(f"computers hand is : [{computer_first_card},{computer_second_card}] ")
        computer_hand = [computer_first_card, computer_second_card]
        computer_score = computer_hand[0] + computer_hand[1]
        print(f"computer's score is : {computer_score}")
        if computer_score > current_score:
            print("YOU LOSE")
            print("\n" * 30)
        else:
            print("YOU WIN ")
            print("\n" * 30)

if game is False:
    print("GOOD BYE ")