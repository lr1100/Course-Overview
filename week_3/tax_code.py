#Get users income
income = int(input("Please enter your income: "))

#Apply Tax Rate
#First $1000 at 5%, second $1000 at 10%, the rest at 15%
tax_amount = 0
if income <= 1000:
    tax_amount = income * .05
elif income <= 2000:
    tax_amount = 1000 * .05 + (income - 1000) * .10
else:
    tax_amount = 1000 * .05 + 1000 * .10 + (income - 2000) * .15

print("$" + str(tax_amount))
