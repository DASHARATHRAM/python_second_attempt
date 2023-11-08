import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def user_level():
    if input("Choose a difficulty. Type 'easy' or 'hard': hard - ") == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def check_answer(user_guess,computer_guess,attempts):
    if user_guess == computer_guess:
        print(f"You got it! The answer was {computer_guess}.")
    elif user_guess < computer_guess:
        print("Too low.")
        return attempts - 1
    elif user_guess > computer_guess:
        print("Too high.")
        return attempts - 1
    else:
        print("You have entered an invalid response")



def game():
    print("Welcome to the Number Guessing Game!")
    computer_guess = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100.")
    print(computer_guess)

    attempts = user_level()

    user_guess = 0
    while user_guess != computer_guess:
        print(f"You have {attempts} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        attempts = check_answer(user_guess,computer_guess,attempts)
        if attempts == 0:
            print("You have got no turns, you lose")
            return
        elif user_guess != computer_guess:
            print("Guess again")
game()
