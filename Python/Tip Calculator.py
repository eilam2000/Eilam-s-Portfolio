print("Welcome to the tip calculator.")
Bill = input("What was the total bill? $")
Tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ") 
People = input("How many people to split the bill? ")
Pay = float(Bill) + float(Bill) * (float(Tip_percentage) / 100)
Pay_per_person = round(Pay / int(People), 2)
print(f"${Pay_per_person}")
