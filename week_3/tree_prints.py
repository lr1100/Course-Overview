#Ask user for tree size
n = int(input("Enter a size: "))

length_of_string = ((n*2) - 1)
middle_of_string = int(length_of_string / 2)

#Build Tree
tree_level=1
while tree_level <= n:
    #Initial level string
    level_string = [" "] * ((n*2) - 1)
    #Fill in numbers
    #Tree level is in th middle, (1 - Tree Level) is middle -1 and middle -2
    #(2 - Tree level) is middle -2 and middle + 2
    i = tree_level
    while i > 0:
        level_string[middle_of_string + (tree_level - i)] = str(i)
        level_string[middle_of_string - (tree_level - i)] = str(i)
        i -= 1

    print(''.join(level_string))
    tree_level += 1
