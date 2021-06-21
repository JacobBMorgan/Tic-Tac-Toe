import random


def print_game_board():
    print(" ", gameBoard[1], " | ", gameBoard[2], " | ", gameBoard[3])
    print("-----------------")
    print(" ", gameBoard[4], " | ", gameBoard[5], " | ", gameBoard[6])
    print("-----------------")
    print(" ", gameBoard[7], " | ", gameBoard[8], " | ", gameBoard[9])


def check_game_state():
    # Row win conditions
    if gameBoard[1] == gameBoard[2] and gameBoard[2] == gameBoard[3] and gameBoard[2] != ' ':
        if currentPlayer == 'O':
            print("You have won!")
            return True
        if currentPlayer == 'X':
            print("You have lost to the computer.")
            return True
        else:
            pass

    if gameBoard[4] == gameBoard[5] and gameBoard[5] == gameBoard[6] and gameBoard[5] != ' ':
        if currentPlayer == 'O':
            print("You have won!")
            return True
        if currentPlayer == 'X':
            print("You have lost to the computer.")
            return True
        else:
            pass

    if gameBoard[7] == gameBoard[8] and gameBoard[8] == gameBoard[9] and gameBoard[8] != ' ':
        if currentPlayer == 'O':
            print("You have won!")
            return True
        if currentPlayer == 'X':
            print("You have lost to the computer.")
            return True
        else:
            pass

    # Column win conditions
    if gameBoard[1] == gameBoard[4] and gameBoard[4] == gameBoard[7] and gameBoard[4] != ' ':
        if currentPlayer == 'O':
            print("You have won!")
            return True
        if currentPlayer == 'X':
            print("You have lost to the computer.")
            return True
        else:
            pass

    if gameBoard[2] == gameBoard[5] and gameBoard[5] == gameBoard[8] and gameBoard[5] != ' ':
        if currentPlayer == 'O':
            print("You have won!")
            return True
        if currentPlayer == 'X':
            print("You have lost to the computer.")
            return True
        else:
            pass

    if gameBoard[3] == gameBoard[6] and gameBoard[6] == gameBoard[9] and gameBoard[6] != ' ':
        if currentPlayer == 'O':
            print("You have won!")
            return True
        if currentPlayer == 'X':
            print("You have lost to the computer.")
            return True
        else:
            pass

    # Diagonal win conditions
    if gameBoard[1] == gameBoard[5] and gameBoard[5] == gameBoard[9] and gameBoard[5] != ' ':
        if currentPlayer == 'O':
            print("You have won!")
            return True
        if currentPlayer == 'X':
            print("You have lost to the computer.")
            return True
        else:
            pass

    if gameBoard[3] == gameBoard[5] and gameBoard[5] == gameBoard[7] and gameBoard[5] != ' ':
        if currentPlayer == 'O':
            print("You have won!")
            return True
        if currentPlayer == 'X':
            print("You have lost to the computer.")
            return True
        else:
            pass


# Introductory text
print("Welcome to Tic-Tac-Toe!")
print("You are O's, the computer is X's.")
print("The game board will look like this:")
print(" ", "1", " | ", "2", " | ", "3")
print("-----------------")
print(" ", "4", " | ", "5", " | ", "6")
print("-----------------")
print(" ", "7", " | ", "8", " | ", "9")
print("When prompted for input, select the numeric value that corresponds to the space you would like to claim.")
print("For example, if you want to claim the middle space, you would enter 5 when prompted.")

# Outer game loop; initializes conditions and allows for replay.
while True:
    # Initializing conditions
    currentPlayer = ''
    gameBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    spacesFilled = 0

    # Determining play order
    print("Player order will be decided randomly.")
    playOrder = random.randint(1, 2)
    if playOrder == 1:
        print("The player will go first.")
        currentPlayer = 'O'
    elif playOrder == 2:
        print("The computer will go first.")
        currentPlayer = 'X'
    else:
        print("This is an error handling message. Something strange happened.")

    print("Beginning a new game...")
    print_game_board()

    # Inner game loop; contains logic for turns and checks game state.
    while True:
        # Draw condition
        if spacesFilled == 9:
            print("The game has resulted in a draw.")
            break

        # Player turn
        elif currentPlayer == 'O':
            # Get the player's move selection.
            playerInput = int(input("Which space would you like to claim? "))

            # Legal move
            if gameBoard[playerInput] == ' ':
                gameBoard[playerInput] = 'O'
                spacesFilled = spacesFilled + 1
                print_game_board()
                check_game_state()
                if check_game_state() is True:
                    break
                currentPlayer = 'X'

            # Illegal move
            elif gameBoard[playerInput] != ' ':
                print("Invalid move; the space is already occupied. Try again.")
                continue

        # Computer turn
        elif currentPlayer == 'X':
            # A random move is produced
            fillBoard = random.randint(1, 9)

            # Legal move is found
            if gameBoard[fillBoard] == ' ':
                print("The computer will now make their move.")
                gameBoard[fillBoard] = 'X'
                spacesFilled = spacesFilled + 1
                print_game_board()
                check_game_state()
                if check_game_state() is True:
                    break
                currentPlayer = 'O'

            # Legal move is not found
            elif gameBoard[fillBoard] != ' ':
                continue

        # Error handling?
        else:
            print("This is an error handling message. Something strange happened.")

    # Play again?
    playAgain = input("Would you like to play again? Enter yes or no: ")
    if playAgain == "yes":
        print("\n")
        continue
    elif playAgain == "no":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid selection! Try again.")
