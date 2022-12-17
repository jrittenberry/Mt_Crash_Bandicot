import random

deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
        9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
your_hand = []
computer_hand = []

your_hand.append(random.choice(deck))
computer_hand.append(random.choice(deck))
your_hand.append(random.choice(deck))
computer_hand.append(random.choice(deck))

print("Welcome to Jamal's BlackJack Table. Where everyone is a winner........sometimes.")
print("Your hand:", your_hand)

your_count = sum(your_hand)

while True:
    choice = input("Do you want to hit or stay? ").lower()
    if choice == "hit":
        new_card = random.choice(deck)
        your_hand.append(new_card)
        your_count = sum(your_hand)
        print("Your hand:", your_hand)
        print("Your count is:", your_count)
        if your_count == 21:
            print("You hit 21! You win! Beginner's luck")
            break
        elif your_count > 21:
            print("You busted! You lose. The name of the game is to not go OVER 21")
            break
    elif choice == "stay":
        computer_count = sum(computer_hand)
        while computer_count < 17:
            new_card = random.choice(deck)
            computer_hand.append(new_card)
            computer_count = sum(computer_hand)
        print("Computer's hand:", computer_hand)
        print("Computer's count is:", computer_count)
        if computer_count == 21:
            print("Computer hit 21! Computer wins! (We promise it's not rigged.)")
            break
        elif computer_count > 21:
            print("The computer busted! You win!......for once.")
        elif computer_count > your_count:
            print("The computer wins! You should've saw this coming.")
        elif computer_count == your_count:
            print(
                "It's a tie! So, technically the computer wins, I don't make the rules.")
        else:
            print("You win! See, it happens sometimes")
        break
    else:
        print("Invalid input. Please enter 'hit' or 'stay'. Following directions is not really your thing, huh?")
