import random
EASY_LEVEL = 10
HARD_LEVEL = 5
continue_game = True

def ask_for_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL

def check_answer(guess, comp_guess, lives):
        if guess == comp_guess:
            print(f"You got it, the anwser is {comp_guess}!!")
        elif guess > comp_guess:
            print("Too high")
            return lives - 1
            
        elif guess < comp_guess:
            print("Too low")
            return lives - 1
                
        else:
            print("Invalid reponse")
def game():
    print("Welcome to the Number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    comp_guess = random.randint(1,100)
    print(comp_guess)

    lives = ask_for_level()
    guess = 0
    while guess != comp_guess:
            print(f"You have {lives} attempts remaining to guess the number.")
            guess = int(input("What is your guess?\n"))
            lives = check_answer(guess,comp_guess,lives)
            if lives == 0:
                print("You have got no turns, you lose")
                return
            elif guess != comp_guess:
                print("You lost a life, guess again")

game()