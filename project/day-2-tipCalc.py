print("Welcome to the tip calculator")

total = input("What was the total bill? $")

tip_percent = input(
    "What percentage tip you would like to give? 10, 12 or 15?")

people = input('How many peaople to split the bill?')

total = float(total)
tip_percent = int(tip_percent)
people = int(people)

tip =  ( tip_percent / total) * 100

total_bill = total + tip

per_person = round(total_bill / people, 2)

print(f"Each person should pay {per_person}")
