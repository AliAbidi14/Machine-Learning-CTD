#Creating the grid as a list of rows.
gridList = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']] 

def take_a_turn(piece, column):
    '''take_a_turn() -> str
    returns a grid with the appropriate placement
    of a player's piece.'''
    row = 5
    while gridList[row][column] != '.':     #Find the first empty space in the given column, into which the piece falls.
        row -= 1
        if row == -1:
            print('\nThat column is full.')
            while True:
                ask_again = input('\nPlease enter a column to play in: ')    #If a column is full, ask for another input.
                #Making sure that the input is valid in the context of the grid and game.
                if ask_again.isdigit() and int(ask_again) != column and 0 <= int(ask_again) <= 6:
                    column = int(ask_again)
                    break
                elif ask_again.isdigit() == False or int(ask_again) <= -1 or int(ask_again) >= 7:
                    print('\nThat is not a valid input.')
                else:
                    print('\nThat column is full.')

    gridList[row][column] = piece    #Replace that spot as the piece.

    grid = '\n0 1 2 3 4 5 6\n'    #Print the grid with the new piece in the correct spot.
    for row in gridList:
        gridRow = ' '.join(row)
        grid += gridRow + '\n'
    return grid

def horizontal_win(piece):
    '''horizontal_win(piece) -> Bool
    returns True or False if there is a horizontal
    four-in-a-row or not, respectively.'''
    for row in gridList:
        if 4 * piece in ''.join(row):
            return True
        else:
            continue
    return False

def vertical_win(piece):
    '''vertical_win(piece) -> Bool
    returns True or False if there is a vertical
    four-in-a-row or not, respectively.'''
    #We can create a list of each column's items, and see if there is a four-in-a-row.
    columnList = []
    for column in range(7):
        for row in gridList:
            columnList += row[column]
        if 4 * piece in ''.join(columnList):
            return True
        else:
            continue
    return False

def right_diagonal_win(piece):
    '''right_diagonal_win(piece) -> Bool
    returns True or False if there is a right
    diagonal four-in-a-row or not, respectively.'''
    for row in range(6):
        for column in range(7):
            if row - 3 >= 0 and column + 3 <= 6:    #Making sure that we don't get an IndexError.
                if piece == gridList[row][column] == gridList[row-1][column+1] == gridList[row-2][column+2] == gridList[row-3][column+3]:
                    return True
                else:
                    continue
    return False

def left_diagonal_win(piece):
    '''left_diagonal_win(piece) -> Bool
    returns True or False if there is a left
    diagonal four-in-a-row or not, respectively.'''
    for row in range(6):
        for column in range(7):
            if row + 3 <= 5 and column + 3 <= 6:    #Making sure that we don't get an IndexError.
                if piece == gridList[row][column] == gridList[row+1][column+1] == gridList[row+2][column+2] == gridList[row+3][column+3]:
                    return True
                else:
                    continue
    return False

def win(piece):
    '''win(piece) -> Bool
    return True or False if there is any type of four-in-a-row or not, respectively.'''
    if horizontal_win(piece) or vertical_win(piece) or right_diagonal_win(piece) or left_diagonal_win(piece):
        return True
    return False

def valid_input(userInput):
    if not userInput.isdigit() or int(userInput) >= 7 or int(userInput) <= -1:    #Checking if the input is a number or not, and then asking until it is valid.
        while True:
            print('\nThat is not a valid input.')
            ask_again = input('\nPlease enter a column to play in: ')
            if ask_again.isdigit() and 0 <= int(ask_again) <= 6:
                userInput = int(ask_again)
                break
    return userInput
    
playerX = input('Player X, enter your name: ')
playerO = input('Player O, enter your name: ')

turn = 0    #Initializing a count of the number of turns.
grid = '\n0 1 2 3 4 5 6\n'    #Print the starting grid.
for row in gridList:
    gridRow = ' '.join(row)
    grid += gridRow + '\n'
print(grid)

#As long as there is not a win, we want to keep playing.
while True:
    placeX = input(playerX + ", you're X. What column do you want to play in? ")
    placeX = valid_input(placeX)    #Checking if the input is valid.
    print(take_a_turn('X', int(placeX)))    #Process the turn and print the new grid.
    if win('X'):    #If there's a win with X, say that and end the game.
        print('Congratulations, ' + playerX + ', you won!')
        break
        
    placeO = input(playerO + ", you're O. What column do you want to play in? ")
    placeO = valid_input(placeO)    #Checking if the input is valid.
    print(take_a_turn('O', int(placeO)))    #Process the turn and print the new grid.
    if win('O'):    #If there's a win with O, say that and end the game.
        print('Congratulations, ' + playerO + ', you won!')
        break

    turn += 1
    if turn == 21:    #If there's no win and all pieces are spent, say that it's a draw and end the game.
        print("It's a draw!")
        break