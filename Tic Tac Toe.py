#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
import unittest

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    board[position] = mark


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    for i in range(1, 10, 3):
        print(f" {board[i] if board[i] != ' ' else i} | {board[i+1] if board[i+1] != ' ' else i+1} | {board[i+2] if board[i+2] != ' ' else i+2}")
        if i < 7:
            print('---------')

# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied



def validateMove(position):

    try:
        pos = int(position)
    except ValueError:
        return False

    if 1 <= pos <= 9 and board[pos] != 'X' and board[pos] != 'O':
        return True
    return False


# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [7, 5, 3]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):

    for combo in winCombinations:
        if player == board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return True
    return False


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for i in board:
        if board[i] == " ":
            return False
    return True
        

#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
def gameplay():

    global gameEnded, currentTurnPlayer

    while not gameEnded:
        position = input(currentTurnPlayer + "'s turn, input: ")
        if validateMove(position) == True:
            position = int(position)
            markBoard(position, currentTurnPlayer)
            printBoard()
            if checkWin(currentTurnPlayer) == True:
                print("CONGRATULATIONS PLAYER {}!!\n You Won!!".format(currentTurnPlayer))
                gameEnded = True
            elif checkFull() == True:
                print("The board is full. It's a TIE!")
                gameEnded = True   
            else:
                if currentTurnPlayer == 'X':
                    currentTurnPlayer = 'O' 
                else:
                    currentTurnPlayer = 'X'
        else:
            print("Invalid move, please try again.")
    print("Would you like to play again?\n Enter 1 if yes, enter 2 if no.")
    response = input()
    if response == '2':
        print("Thank you for playing.")
    elif response == '1':
        gameEnded = False
        resetgame()
        
def resetgame():
    
    global board, gameEnded, currentTurnPlayer

    board = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'
    }

    print('Game started: \n\n' +
          ' 1 | 2 | 3 \n' +
          ' --------- \n' +
          ' 4 | 5 | 6 \n' +
          ' --------- \n' +
          ' 7 | 8 | 9 \n')
    gameplay()

gameplay() 

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
