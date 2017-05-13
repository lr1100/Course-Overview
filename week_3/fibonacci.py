#Ask the user for a number
n = int(input("Enter a number: "))

#Starts off with 1 1
print("1 1", end=' ')

value1 = 1
value2 = 1
#Loop while the sum is less than or equal to inputed number
while value1 + value2 <= n:
    print (value1 + value2, end=' ')
    temp = value1 + value2 # save before we replace
    value1 = value2
    value2 = temp
