price = float(input("Enter the price of a meal: "))

tip = price * 0.16
total = tip + price

print ("A 16% tip would be $", round(tip,2))
print ("The total including tip would be $", round(tip + total, 2))
