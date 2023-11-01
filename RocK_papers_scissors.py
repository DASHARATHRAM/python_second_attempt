import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock,paper,scissors]

you_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if you_chose < 0 or you_chose >=3:
    print("You have entered an invalid response, so WTF...You lost")
else:
    print("You chose:\n")
    print(choices[you_chose])
    comp_chose = random.randint(0,2)

    print("Computer chose:\n")
    print(choices[comp_chose])


    if comp_chose > you_chose:
        print("You lost")
    elif comp_chose < you_chose:
        print("You won")
    elif comp_chose == 0 and you_chose == 2:
        print("You lost")
    elif comp_chose == 2 and you_chose == 0:
        print("You lost")
    elif comp_chose == you_chose:
        print("It's a draw")

