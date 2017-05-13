#Enter the size of board
n = int(input("Enter a board size: "))

#Create a square Chess Baord
chess_board = [[0 for x in range(n)] for y in range(n)]

#Check to see if chess board is big enough for next steps
if(len(chess_board[0]) > 1):

    #Initialize
    chess_board[0][0] = 1
    start_position = (0,0)
    next_steps = []
    next_steps.append((start_position[0]+1,start_position[1]))
    next_steps.append((start_position[0]+1,start_position[1]+1))
    temp = []
    print("\t",next_steps)

    #Loop through next_steps
    while next_steps != []:
        #loop through next_steps
        for position in next_steps:

            #Incriment chess board
            print(position)
            x,y = position
            chess_board[x][y] += 1

            #Check to see if next steps is off the board
            if(position[0] + 1 < n):
                temp.append((position[0] + 1, position[1]))
                temp.append((position[0] + 1, position[1] + 1))
                print("\t",temp)

        #Update next steps from temp
        next_steps = temp.copy()
        temp.clear()


print(chess_board)
