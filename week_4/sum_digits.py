def sum_digits(number):
    """returns the sum of the digits of the input"""
    #Check to see if number is negative
    negative = False
    if(number < 0):
        negative = True
        number_string = str(number)[1:] #remove the negative sign
    else:
        #Not a negative number
        number_string = str(number) #make number a string so we can iterate over it
    #Check to see if the number is only 1 digits
    #Works for both negative and positive numbers
    if(len(number_string.replace("-","")) == 1):
        if negative:
            return -1 * int(number_string)
        else:
            return int(number_string)
    #Number is more than one digit
    else:
        #Sum the digits togeter
        total = 0
        for i in map(int,number_string):
            total += i
        #If it was negative at beginning, make it negative
        if negative:
            return -1 * total
        else:
            return total

def diff_sum_digits(number):
    """the value of number_string minus the sum of its digits"""
    return number - sum_digits(number)


def wraps(number):
    """Loops"""
    while(len(str(number).replace("-","")) > 1):
        number = diff_sum_digits(number)
        #if it still more than 1 digit in length
        if(len(str(number).replace("-","")) > 1):
            number = sum_digits(number)
    return number

def main():
    print("in main")
    number = int(input("Enter a number: "))

    print(wraps(number))


if __name__ == "__main__":
    main()
