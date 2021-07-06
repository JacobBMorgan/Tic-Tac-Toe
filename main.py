import random


def print_game_board():
    print(" ", game_board[1], " | ", game_board[2], " | ", game_board[3])
    print("-----------------")
    print(" ", game_board[4], " | ", game_board[5], " | ", game_board[6])
    print("-----------------")
    print(" ", game_board[7], " | ", game_board[8], " | ", game_board[9])


def check_game_state():
    # Row win conditions
    if game_board[1] == game_board[2] and game_board[2] == game_board[3] and game_board[2] != ' ':
        if current_player == 'O':
            print("Player 1 wins!")
            return True
        elif current_player == 'X':
            print("Player 2 wins!")
            return True
        else:
            pass

    if game_board[4] == game_board[5] and game_board[5] == game_board[6] and game_board[5] != ' ':
        if current_player == 'O':
            print("Player 1 wins!")
            return True
        elif current_player == 'X':
            print("Player 2 wins!")
            return True
        else:
            pass

    if game_board[7] == game_board[8] and game_board[8] == game_board[9] and game_board[8] != ' ':
        if current_player == 'O':
            print("Player 1 wins!")
            return True
        elif current_player == 'X':
            print("Player 2 wins!")
            return True
        else:
            pass

    # Column win conditions
    if game_board[1] == game_board[4] and game_board[4] == game_board[7] and game_board[4] != ' ':
        if current_player == 'O':
            print("Player 1 wins!")
            return True
        elif current_player == 'X':
            print("Player 2 wins!")
            return True
        else:
            pass

    if game_board[2] == game_board[5] and game_board[5] == game_board[8] and game_board[5] != ' ':
        if current_player == 'O':
            print("Player 1 wins!")
            return True
        elif current_player == 'X':
            print("Player 2 wins!")
            return True
        else:
            pass

    if game_board[3] == game_board[6] and game_board[6] == game_board[9] and game_board[6] != ' ':
        if current_player == 'O':
            print("Player 1 wins!")
            return True
        elif current_player == 'X':
            print("Player 2 wins!")
            return True
        else:
            pass

    # Diagonal win conditions
    if game_board[1] == game_board[5] and game_board[5] == game_board[9] and game_board[5] != ' ':
        if current_player == 'O':
            print("Player 1 wins!")
            return True
        elif current_player == 'X':
            print("Player 2 wins!")
            return True
        else:
            pass

    if game_board[3] == game_board[5] and game_board[5] == game_board[7] and game_board[5] != ' ':
        if current_player == 'O':
            print("Player 1 wins!")
            return True
        elif current_player == 'X':
            print("Player 2 wins!")
            return True
        else:
            pass


# Introductory text
print("Welcome to Tic-Tac-Toe!")
print("Player 1 is O's, Player 2 is X's.")
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
    current_player = ''
    game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    spaces_filled = 0

    # Determining game mode
    print("How would you like to play?")
    print("1. Versus a computer.")
    print("2. Versus a local player.")
    game_type = int(input("Make your selection: "))
    if game_type < 1 or game_type > 2:
        print("Invalid selection; try again.")
        continue

    # Determining play order
    print("Player order will be decided randomly.")
    play_order = random.randint(1, 2)
    if play_order == 1:
        print("Player 1 will go first.")
        current_player = 'O'
    elif play_order == 2:
        print("Player 2 will go first.")
        current_player = 'X'
    else:
        print("This is an error handling message. Something strange happened. Code 2")

    print("Beginning a new game...")
    print_game_board()

    # Inner game loop; contains logic for turns and checks game state.
    while True:
        # Player versus Computer
        if game_type == 1:
            while True:
                # Draw condition
                if spaces_filled == 9:
                    print("The game has resulted in a draw.")
                    break

                # Player turn
                elif current_player == 'O':
                    # Get the player's move selection.
                    player_input = int(input("Player 1's turn, which space would you like to claim? "))

                    # Legal move
                    if game_board[player_input] == ' ':
                        game_board[player_input] = 'O'
                        spaces_filled = spaces_filled + 1
                        print_game_board()
                        check_game_state()
                        if check_game_state() is True:
                            break
                        current_player = 'X'

                    # Illegal move
                    elif game_board[player_input] != ' ':
                        print("Invalid move; the space is already occupied. Try again.")
                        continue

                # Computer turn
                elif current_player == 'X':
                    # A random move is produced
                    fill_board = random.randint(1, 9)

                    # Legal move is found
                    if game_board[fill_board] == ' ':
                        print("The computer will now make their move.")
                        game_board[fill_board] = 'X'
                        spaces_filled = spaces_filled + 1
                        print_game_board()
                        check_game_state()
                        if check_game_state() is True:
                            break
                        current_player = 'O'

                    # Legal move is not found
                    elif game_board[fill_board] != ' ':
                        continue

                # Error handling?
                else:
                    print("This is an error handling message. Something strange happened. Code 3")

        # Player versus Player
        elif game_type == 2:
            while True:
                # Draw condition
                if spaces_filled == 9:
                    print("The game has resulted in a draw.")
                    break

                # Player 1 turn
                elif current_player == 'O':
                    # Get the player's move selection.
                    player_input = int(input("Player 1's turn, which space would you like to claim? "))

                    # Legal move
                    if game_board[player_input] == ' ':
                        game_board[player_input] = 'O'
                        spaces_filled = spaces_filled + 1
                        print_game_board()
                        check_game_state()
                        if check_game_state() is True:
                            break
                        else:
                            pass
                        current_player = 'X'

                    # Illegal move
                    elif game_board[player_input] != ' ':
                        print("Invalid move; the space is already occupied. Try again.")
                        continue

                # Player 2 turn
                elif current_player == 'X':
                    # Get the player's move selection.
                    player_input = int(input("Player 2's turn, which space would you like to claim? "))

                    # Legal move
                    if game_board[player_input] == ' ':
                        game_board[player_input] = 'X'
                        spaces_filled = spaces_filled + 1
                        print_game_board()
                        check_game_state()
                        if check_game_state() is True:
                            break
                        else:
                            pass
                        current_player = 'O'

                    # Illegal move
                    elif game_board[player_input] != ' ':
                        print("Invalid move; the space is already occupied. Try again.")
                        continue

                # Error handling?
                else:
                    print("This is an error handling message. Something strange happened. Code 4")

        else:
            print("This is an error handling message. Something strange happened. Code 5")

        if check_game_state() is True or spaces_filled == 9:
            break

    play_again = int(input("Would you like to play again? Enter 1 for yes, 2 for no: "))
    if play_again == 1:
        print("\n")
        continue
    elif play_again == 2:
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid selection, try again.")
