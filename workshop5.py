import random


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)

    while tries != 0:
        guess = int(input("Enter a guess: "))
        if guess == random_number:
            print("Congrats, you guessed the correct number!")
            return
        elif guess < random_number:
            print("Guess higher!")
        else:
            print("Guesss lower!")
        tries -= 1

        print("Sorry, you were unable to guess the right number.")


"""
guess_random_number(5, 0, 10)"""


def guess_random_num_linear(tries, start, stop):
    target_num = random.randint(start, stop)
    print("The target number is: ", target_num)

    for num in range(start, stop):
        tries -= 1
        print("The number of tries left: ", tries)
        print("The computer is guessing:....", num)
        if num == target_num:
            print("The computer has selected the correct answer.")
            return
        elif tries == 0:
            print("The computer has not guessed the correct answer.")
            return


"""guess_random_num_linear(5, 0, 10)
"""


def guess_random_num_binary(tries, start, stop):
    target_number = random.randint(start, stop)
    print("Random number to find: ", target_number)
    while tries > 0:
        mid = (start + stop) // 2
        if mid == target_number:
            print("The computer was able to guess the correct number. ", target_number)
            return
        elif mid < target_number:
            print("Guessing higher")
            start = mid + 1
        else:
            print("Guessing lower")
        tries -= 1

    print("The computer was unable to guess the correct number.")


guess_random_num_binary(5, 0, 100)
