gallons = float(input("Input the number of gallons of gasoline to convert: "))
print("# of gallons of gasoline to convert: ", gallons)

print("\t in liters: ", gallons * 3.7854)
print("\t # of barrels of oil: ", gallons / 19.5)
print("\t price in US Dollars: $%.2f" % gallons * 3.65)
