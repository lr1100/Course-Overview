#2x2 Matrix Inversion Function
def invertMatrix(matrix):
    """
    Return the inversion of the 2x2 matrix
    """
    #Calculate the scalar
    scalar = 1/(matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])

    #Rearrange the matrix
    inverse = [[matrix[1][1],-matrix[0][1]],[-matrix[1][0],matrix[0][0]]]
    print(inverse)
    #Calculate the values
    for i in range(len(inverse)):
        for j in range(len(inverse[i])):
            inverse[i][j] = scalar * inverse[i][j]

    return tuple(inverse)

#Ask the user to input 4 numbers seperated by spaces
numbers = input("Enter four numbers seperated by spaces: ").split()
print(numbers)

#Create individual tuples (a,b) and (c,d)
try:
    a = float(numbers[0])
    b = float(numbers[1])
    c = float(numbers[2])
    d = float(numbers[3])
    ab = (a, b)
    cd = (c, d)
except:
    print("Error: Input was malformed")
    exit()

#Create a tupe containing the individual tuples ((a,b),(c,d))
abcd = ((ab,cd))

#Print the matrix to invert
print("matrix: " + str(abcd))

#Invert the matrix
inverse = invertMatrix(abcd)

#Print the inverse
print("inverse: " + str(inverse))
