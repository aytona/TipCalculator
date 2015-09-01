# My first python program
# Tip Calculator

meal_input = input("How much was the meal?")
tax_input = input("Tax percentage?")
tip_input = input("Tip percentage?")
meal = int(meal_input)
tax = float(tax_input) / 100
tip = float(tax_input) / 100

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)