#Number Guessing Game

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
Difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

import random 
answer = random.randint(1, 100)

def decrease_turns():
  global turns
  turns -= 1
  print(f"You have {turns} attempts to guess the right number.")

if Difficulty == "easy":
  print("You have 10 turns good luck!")
  turns = 10
  while turns > 0:
    guess = int(input("Make a guess: "))
    if guess > answer:
      print("Too high.")
      print("Guess again.")
      decrease_turns()
    elif guess < answer:
      print("Too low.")
      print("Guess again.")
      decrease_turns()
    elif guess == answer:
      print("You got it!")
      break
    if turns == 0:
      print("You lost!")


elif Difficulty == "hard":
  print("You have 5 turns good luck!")
  turns = 5
  while turns > 0:
    guess = int(input("Make a guess: "))
    if guess > answer:
      print("Too high.")
      print("Guess again.")
      decrease_turns()
    elif guess < answer:
      print("Too low.")
      print("Guess again.")
      decrease_turns()
    elif guess == answer:
      print("You got it!")
      break
    if turns == 0:
      print("You lost!")