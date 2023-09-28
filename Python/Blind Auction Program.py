from replit import clear

from art import logo
print(logo)
print("Welcome to the secret auction program.")

bidders = []
while True:
  clear()
  auction = input("What is your name? ")
  bid = int(input("What's your bid?: $"))
  bidders.append({"Name": auction, "Bid": bid})
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidders == "no":
    break

clear()
highest_bidder = ""
highest_bid = 0

for bidder in bidders:
    if bidder["Bid"] > highest_bid:
        highest_bid = bidder["Bid"]
        highest_bidder = bidder["Name"]
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
