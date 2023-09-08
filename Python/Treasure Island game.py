print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_option = input("You're at a crossroad, where do you want to go? left or right? press left or right. ")
if first_option == "left" or first_option == "Left" or first_option == "LEFT":
  print("Move on.")
  second_option = input("You reached a like. Would you like to swim or wait for a boat? press wait or swim. ")
  if second_option == "wait" or second_option == "Wait" or second_option == "WAIT":
    print("Move on.")
    third_option = input("You arrived at the island, you reached a temple with 3 doors. Which door would you like to open? Red, Blue, or Yellow? ")
    if third_option == "yellow" or third_option == "Yellow" or third_option == "YELLOW":
      print("You found the treasure! You won!")
    elif third_option == "red" or third_option == "Red" or third_option == "RED":
      print("You opened the door and fell into a lava. Game over.")
    elif third_option == "blue" or third_option == "Blue" or third_option == "BLUE":
      print("You opened the door and got freezed. Game over.")
  elif second_option == "swim" or second_option == "Swim" or second_option == "SWIM":
    print("You got killed by a hippo. Game over.")
elif first_option == "right" or first_option == "Right" or first_option == "Right":
  print("You ran into a tribe of cannibals and got eaten. Game over.")