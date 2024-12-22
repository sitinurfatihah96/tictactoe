# import libraries
import unittest

# The Game Board 
def initialize_board():
    return [' '] * 9  # Initial board as a list to represent the 9 positions

# Print the game board
def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print(' --------- ')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print(' --------- ')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

# Check for a win
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check for a tie
def check_tie(board):
    return all(cell != ' ' for cell in board)

# Function to play the game
def play_game():
    board = initialize_board()
    currentTurnPlayer = 'X'
    gameEnded = False

    # Game start message
    print('Game started: \n\n' +
          ' 1 | 2 | 3 \n' +
          ' --------- \n' +
          ' 4 | 5 | 6 \n' +
          ' --------- \n' +
          ' 7 | 8 | 9 \n')

    # Main game loop
    while not gameEnded:
        try:
            # Ask for user input
            move = int(input(f"{currentTurnPlayer}'s turn, choose a position (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please choose a number between 1 and 9.")
                continue
            
            # Check if the position is already taken
            if board[move - 1] != ' ':
                print("Position already taken. Choose another.")
                continue
            
            # Update the board
            board[move - 1] = currentTurnPlayer
            print_board(board)

            # Check for a win or tie
            if check_winner(board, currentTurnPlayer):
                print(f"Player {currentTurnPlayer} wins!")
                gameEnded = True
            elif check_tie(board):
                print("It's a tie!")
                gameEnded = True
            else:
                # Switch players
                currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask to restart the game
    while True:
        restart = input("Do you want to play again? (y/n): ").lower()
        if restart == 'y':
            play_game()  # Restart the game
            break
        elif restart == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Start the game
play_game()

