#Enter a number
n = int(input("Enter a number: "))

length_of_level = n * 3
middle_of_level = int(length_of_level / 2)

previous_list = [" "] * length_of_level

#Create n levels
for level in range(n):
    #Initialize level
    current_list = [" "] * length_of_level

    #Fill in the ones which go on the outside
    current_list[middle_of_level - (level)] = "1"
    current_list[middle_of_level + (level)] = "1"
    
    #Loop through positions, checking to see if there are numbers in previous
    #list to add up. if " ", don't add
    for position in range(length_of_level):
        if previous_list[position-1] != " " and previous_list[position+1] != " ":
            current_list[position] = str(int(previous_list[position-1]) + \
                                         int(previous_list[position+1]))
    print(''.join(current_list))
    previous_list = current_list
