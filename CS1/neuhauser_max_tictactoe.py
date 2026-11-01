""""
┌───────────────────────────────────────────────────────────────────────────┐
│                              Tic Tac Toe                                  │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Max Neuhauser                                                       │
| Course: CS2                                                               |
│ Log: 1.0 MN                                                               |
| Bugs: Doesn't clarify who is playing through the users name or            │
│       "Player 1"/"Player 2". Only uses "Player X" and "Player O"          │
│ Description: Numerous functions that replicate the game of tic tac toe    |
└───────────────────────────────────────────────────────────────────────────┘
""" 
def color_text(text, color_name):
    """
    Print the given text in a specified color.
    
    Args:
        text (str): The text to be printed.
        color_name (str): The color of the text to be printed.
    """
        
    colors = {                                                                                                 # Dictionary mapping color names to their ANSI escape codes for terminal text coloring
        'black': '\033[30m',                                                                                   # Black text color
        'red': '\033[31m',                                                                                     # Red text color
        'green': '\033[32m',                                                                                   # Green text color
        'yellow': '\033[33m',                                                                                  # Yellow text color
        'blue': '\033[34m',                                                                                    # Blue text color
        'magenta': '\033[35m',                                                                                 # Magenta (purple) text color
        'cyan': '\033[36m',                                                                                    # Cyan text color
        'white': '\033[37m',                                                                                   # White text color
        'reset': '\033[0m',                                                                                    # Reset text color to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')                                                    # Get the ANSI color code for the given color name, defaulting to white if the color is not found
    return f"{color_code}{text}\033[0m"                                                                        # Print the text with the specified color, followed by the reset code to ensure no color leaks

def print_colored_text(text, color): 
    '''
    Prints the given text in a specified color

    Args:
        text (str): The text to be printed
        color (str): The color of the text to be printed
    Returns:
        None
    Prints:
        (color_text(text, color)): The given text in the specified color
    '''                                                                                                        # Define colored text
    print(color_text(text, color))    

def input_colored_text(text, color):   
    '''
    Prompts the user for input with colored text.
    
    Args:
        text (str): The prompt text to display to the user
        color (str): The color of the prompted text
    Returns:
        input(color_text(text, color)): The user's input as a string
    '''   
    return input(color_text(text, color)) 


def display_board(board):
    '''
    Displays the 3x3 grid board

    Args:
        board (list): 3x3 grid containing strings
    Prints:
        Tic-Tac-Toe board layout
    '''
    def format_cell(cell):
        '''
        Formats the cell value with the appropriate color (red or green) based on its content (either "X" or "O")

        Args:
            cell (str): The value of the cell in the board (either "X" or "O")
        Return:
            str(cell): The cell value with its appropriate corresponding color (red or green) based on its content (either "X" or "O")
        '''
        if cell == "X":
            return color_text(cell, "red")
        elif cell == "O":
            return color_text(cell, "green")
        return str(cell)

    b = []          
    for row in board:       
        new_row = []
        for cell in row:
            new_row.append(format_cell(cell))                                                                  # Append the formatted cell color to the new row
        b.append(new_row) 

    print("\n")
    print(f"| {b[0][0]} | {b[0][1]} | {b[0][2]} |")
    print("----+---+----")
    print(f"| {b[1][0]} | {b[1][1]} | {b[1][2]} |")
    print("----+---+----")      
    print(f"| {b[2][0]} | {b[2][1]} | {b[2][2]} |")
    print("\n")

def get_player_move(board, player):
    '''
    Gets the designated player to choose a position on the board 

    Args:
        board (list): 3x3 grid containing strings                                    
        player (str): Either player 1 or player 2 and their assigned marks (either "X" or "O"), depending on whos turn it is
    Return:
        board (list): Updated board with the players chosen move
    '''
    while True:
        try:
            choice = int(input(f"It is now Player {player}'s turn, please enter your desired move (1-9): "))
            if choice == 1: 
                row, column = 0, 0
            elif choice == 2:
                row, column = 0, 1
            elif choice == 3:
                row, column = 0, 2
            elif choice == 4:
                row, column = 1, 0
            elif choice == 5:
                row, column = 1, 1
            elif choice == 6:
                row, column = 1, 2
            elif choice == 7:
                row, column = 2, 0
            elif choice == 8:
                row, column = 2, 1
            elif choice == 9:
                row, column = 2, 2
            else:
                print("invalid input. Choose a number 1 - 9")
                continue

            if board[row][column] != "X" and board[row][column] != "O":
                board[row][column] = player
                return board
            else:
                print("That spot is already taken. Choose another available spot.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    
def check_winner(board, player):
    '''
    Checks to see if the designated player has won the game after their turn

    Args:
        board (list): 3x3 grid containing strings
        player (str): Either player 1 or player 2 and their assigned marks (either "X" or "O"), depending on whos turn it is
    Return:
        True (boolean): if three of the assigned players marks (either "X" or "O")is continuous in a horizontal, diagonal, or vertical row, then return True.
        False (boolean): if there are no three continuous marks of the assigned player (either "X" or "O") in a horizontal, diagonal, or vertical row, then return False.
    '''
    if board [0][0] == player and board [0][1] == player and board [0][2] == player:
        return True
    elif board [1][0] == player and board [1][1] == player and board [1][2] == player:
        return True
    elif board [2][0] == player and board [2][1] == player and board [2][2] == player:
        return True
    elif board [0][0] == player and board [1][0] == player and board [2][0] == player:
        return True
    elif board [0][1] == player and board [1][1] == player and board [2][1] == player:
        return True
    elif board [0][2] == player and board [1][2] == player and board [2][2] == player:
        return True
    elif board [0][2] == player and board [1][1] == player and board [2][0] == player:
        return True
    elif board [0][0] == player and board [1][1] == player and board [2][2] == player:
        return True
    else:
        return False

def is_draw(board):
    '''
    Checks to see if the game was a draw

    Args:
        board (list): 3x3 grid containing strings
    Return:
        True (boolean): if the board is completed with "X" and "O" but there is still no winner, then return True.
        False (boolean): if the board is not completed with "X" and "O" (there are still remaining spots), then return False.
    '''
    count = 0
    for row in range(0, 3):
        for column in range(0,3):
            if board[row][column] == "X" or board[row][column] == "O":
                count += 1
                    
    if count == 9:
        return True
    else:
        return False 

def choose_player():
    '''
    Chooses who is player 1 and player 2 with their corresponding marks (either "X" or "O")
    Args:
        None
    Return:
        player_1, player_2, "X", "O" (str): assigns corresponding marks ("X" and "O") to the players, respectively. 
        player_1, player_2, "O", "X" (str): assings corresponding marks ("O" and "X") to the players, respectively.
    '''
    player_1 = input("Player 1, please enter your name: ")
    player_2 = input("Player 2, please enter your name: ")
    while True:
        choose_piece = input(f"{player_1}, choose if you would like to be 'X' or 'O': ").upper()
        if choose_piece == "X":
            return player_1, player_2, "X", "O"
        elif choose_piece == "O":
            return player_1, player_2, "O", "X"
        else:
            print("Invalid choice. Please enter 'X' or 'O' ")

def main():
    while True:
        board = [[ '1' , '2' , '3' ], 
                 [ '4' , '5' , '6' ], 
                 [ '7' , '8' , '9' ]]
        p1_name, p2_name, p1_piece, p2_piece = choose_player()
        turns = 1
    
        while not is_draw(board):
            display_board(board)
            if turns % 2 == 1:                                                                                 # if the number of turns is odd (% 2 == 1), it is player 1's turn. If the number of turns is even, it is player 2's turn.
                current_player_name = p1_name
                current_piece = p1_piece
            else:
                current_player_name = p2_name
                current_piece = p2_piece
            
            board = get_player_move(board, current_piece)
            
            if check_winner(board, current_piece):
                display_board(board)
                print(f"{current_player_name} (Player {current_piece}) has won the game!")
                break
                
            turns += 1
        else:
            display_board(board)
            print( "The game is a draw, no one has won." )

        play_again = input_colored_text("Do you want to play again? (y/n): ", "cyan").lower()
        if play_again != 'y':                                                                                  # if the user does not enter 'y', the game will end and break the loop. If the user enters 'y', the game will restart and the loop will continue.
            print_colored_text('Thanks for playing!', 'magenta')
            break 

main()
