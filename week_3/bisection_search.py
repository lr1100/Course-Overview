## Bisection Search to Find a Square Root
x = float(input("enter a number:"))
epsilon = 0.00001
num_guesses = 0

#If x is greater than 0, the sqaure root will be between 0 and x
if(x >= 1):
    low = 0.0
    high = x
#If x is less than 0, the square root will be between x and 1
else:
    low = x
    high = 1

ans = (high + low)/2.0 #find the middle
#Find more middles if the delta is more than our percision (epsilon)
while high - low >= 2 * epsilon:
    print("low =",low,"high =", high)
    num_guesses += 1
    #if our middle squared is less than x, we are too low
    if ans ** 2 < x:
        low = ans
    #If our middle squared is more than x, we are too high
    else:
        high = ans
    #Calculate new middle
    ans = (high + low)/2.0


print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)
