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


import random
rule = input("What do you choose?, Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
if rule == "0":
  print(rock)
elif rule == "1":
  print(paper)
elif rule == "2":
  print(scissors)


computer_choice = random.randint(0, 2)
print("computer chose:")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)


if rule == "0" and computer_choice == 0:
  print("It's a draw.")
elif rule == "0" and computer_choice == 1:
  print("Yow lose.")
elif rule == "0" and computer_choice == 2:
  print("You won!")

if rule == "1" and computer_choice == 0:
  print("You won!")
elif rule == "1" and computer_choice == 1:
  print("It's a draw.")
elif rule == "1" and computer_choice == 2:
  print("You lose.")

if rule == "2" and computer_choice == 0:
  print("You lose.")
elif rule == "2" and computer_choice == 1:
  print("You won!")
elif rule == "2" and computer_choice == 2:
  print("It's a draw.")
    

  