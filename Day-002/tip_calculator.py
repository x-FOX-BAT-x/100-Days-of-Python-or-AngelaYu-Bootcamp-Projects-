#Tip Calculator

print("Welcome to the tip calculator!\n\n")
bill = float(input("What was the total bill?:\n\t$"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15:\n\t"))
people = int(input("How many people to split the bill? "))

tip_cal= round(((bill + (tip/100)) /  people),2)
print(f"Your total for each person would be: ${tip_cal}")
