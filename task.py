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

options_list = ["Rock", "Paper", "Scissors"]

enemy_option = random.choice(options_list)

my_option = input("Choose Rock, Paper, Scissors ")

if my_option == "Rock":
    print(f"Your option: {rock}")
    if enemy_option == "Rock":
        print(f"Enemy's option: {rock}")
        print("Tie")
    elif enemy_option == "Paper":
        print(f"Enemy's option: {paper}")
        print("You Lose")
    else:
        print(f"Enemy's option: {scissors}")
        print("You Win")
elif my_option == "Paper":
    print(f"Your option: {paper}")
    if enemy_option == "Rock":
        print(f"Enemy's option: {rock}")
        print("You Win")
    elif enemy_option == "Paper":
        print(f"Enemy's option: {paper}")
        print("Tie")
    else:
        print(f"Enemy's option: {scissors}")
        print("You Lost")
else:
    print(f"Your option: {scissors}")
    if enemy_option == "Rock":
        print(f"Enemy's option: {rock}")
        print("You Lost")
    elif enemy_option == "Paper":
        print(f"Enemy's option: {paper}")
        print("You Win")
    else:
        print(f"Enemy's option: {scissors}")
        print("Tie")