import random

# track the score of user and computer
user_score = 0
computer_score = 0

# get a list of all the 3 options in a list
options = ["rock", "paper", "scissors"]


# compare the user and computer
def compare(u_choice, c_choice):
    """takes all the inputs and compares"""
    if u_choice == c_choice:
        return "It's a draw"
    elif u_choice == "rock" and c_choice == "scissors":
        return "You won"
    elif u_choice == "scissors" and c_choice == "paper":
        return "You won"
    elif u_choice == "paper" and c_choice == "rock":
        return "You won"
    elif u_choice == "scissors" and c_choice == "rock":
        return "You lost"
    else:
        return "You lost"



    # assign them to the computers pick
comp_pick = random.randint(0, 2)
comp_choice = options[comp_pick]
print(comp_choice)
    # get the user pick
user_choice = ""
user_pick = int(input("What is your choice: type Rock - 0/ Paper - 1/ Scissors - 2/ or 3 to quit - "))
if user_pick == 3:
    print("Good bye and Good day")
    quit()
elif user_pick in range(0, 2):
    user_choice = options[user_pick]

final = compare(user_choice, comp_choice)
if final == "You won":
    user_score += 1
elif final == "You lost":
    computer_score += 1
elif final == "It's a draw":
    print("It's a draw")
print(f"Your score is: {user_score}")
print(f"Computer score: {computer_score}")
    
    