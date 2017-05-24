def reciprocal():
    try:
        x = float(input("Enter a number: "))
        print("The reciprocal of your number is", 1/x)
    except ValueError:
        print("You did not enter a valid number.")
        reciprocal() #Ask the user for a number again
    except ZeroDivisionError:
        print("Zero does not have a reciprocal")
    except:
        print("something else went wrong.")

def main():
    reciprocal()

if __name__ == "__main__":
    main()
