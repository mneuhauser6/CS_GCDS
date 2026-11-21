""""
┌───────────────────────────────────────────────────────────────────────────┐
│                                 Dot Wars                                  │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Max Neuhauser                                                       │
| Course: CS2                                                               |
│ Log: 1.0 MN                                                               |
| Bugs:                                                                     │
│ Description: Numerous functions that replicate a simplified game of       |
|              Battleship                                                   |
└───────────────────────────────────────────────────────────────────────────┘
""" 

def display_board_shoot(board_shoot):
    '''
    Displays the 5x5 grid board

    Args:
        board (list): 5x5 grid containing strings
    Prints:
        Dot Wars board layout
    '''

    print("\n")
    print("     1   2   3   4   5 ")
    print(f" A | {board_shoot[0][0]} | {board_shoot[0][1]} | {board_shoot[0][2]} | {board_shoot[0][3]} | {board_shoot[0][4]} |")
    print("   ----+---+---+---+----")
    print(f" B | {board_shoot[1][0]} | {board_shoot[1][1]} | {board_shoot[1][2]} | {board_shoot[1][3]} | {board_shoot[1][4]} |")
    print("   ----+---+---+---+----")      
    print(f" C | {board_shoot[2][0]} | {board_shoot[2][1]} | {board_shoot[2][2]} | {board_shoot[2][3]} | {board_shoot[2][4]} |")
    print("   ----+---+---+---+----")
    print(f" D | {board_shoot[3][0]} | {board_shoot[3][1]} | {board_shoot[3][2]} | {board_shoot[3][3]} | {board_shoot[3][4]} |")
    print("   ----+---+---+---+----")
    print(f" E | {board_shoot[4][0]} | {board_shoot[4][1]} | {board_shoot[4][2]} | {board_shoot[4][3]} | {board_shoot[4][4]} |")
    print("\n")

def display_board_choose(board_choose):
    '''
    Displays the 5x5 grid board
    
    Args:
        board (list): 5x5 grid containing strings
    Prints:
        Dot Wars board layout
    '''
    
    print("\n")
    print("     1   2   3   4   5 ")
    print(f" A | {board_choose[0][0]} | {board_choose[0][1]} | {board_choose[0][2]} | {board_choose[0][3]} | {board_choose[0][4]} |")
    print("   ----+---+---+---+----")
    print(f" B | {board_choose[1][0]} | {board_choose[1][1]} | {board_choose[1][2]} | {board_choose[1][3]} | {board_choose[1][4]} |")
    print("   ----+---+---+---+----")      
    print(f" C | {board_choose[2][0]} | {board_choose[2][1]} | {board_choose[2][2]} | {board_choose[2][3]} | {board_choose[2][4]} |")
    print("   ----+---+---+---+----")
    print(f" D | {board_choose[3][0]} | {board_choose[3][1]} | {board_choose[3][2]} | {board_choose[3][3]} | {board_choose[3][4]} |")
    print("   ----+---+---+---+----")
    print(f" E | {board_choose[4][0]} | {board_choose[4][1]} | {board_choose[4][2]} | {board_choose[4][3]} | {board_choose[4][4]} |")
    print("\n")

def count_available_space(board_choose):
    space = 25
    while True:
        if is_valid_cell == False:
            space -= 1
        else:
            return space


def is_valid_cell(board_shoot, row, col):
    for row in range(0, 5):
            for col in range(0, 5):
                if board_shoot[row][col] == "⛴":
                    return False
                else:
                    return True



def place_ships(board_choose, player): #FINISH THIS CODE
    '''
    Gets the designated player to place their ship position on the board 

    Args:
        board (list): 5x5 grid containing strings                                    
        player (str): The current player (1 or 2) who is making a move
    Return:
        board (list): Updated board with the players chosen move
    '''
    count = 0
    while count < 6:
        try:
            choice = input(f"It is now Player {player}'s turn, please enter your five desired ship placement (e.g. A1, B3, C5, etc.): ").lower()
            if choice == "a1": 
                row, column = 0, 0
            elif choice == "a2":
                row, column = 0, 1
            elif choice == "a3":
                row, column = 0, 2
            elif choice == "a4":
                row, column = 0, 3
            elif choice == "a5":
                row, column = 0, 4
            elif choice == "b1":
                row, column = 1, 0
            elif choice == "b2":
                row, column = 1, 1
            elif choice == "b3":
                row, column = 1, 2
            elif choice == "b4":
                row, column = 1, 3
            elif choice == "b5":
                row, column = 1, 4
            elif choice == "c1":
                row, column = 2, 0
            elif choice == "c2":
                row, column = 2, 1
            elif choice == "c3":
                row, column = 2, 2
            elif choice == "c4": 
                row, column = 2, 3
            elif choice == "c5": 
                row, column = 2, 4
            elif choice == "d1":
                row, column = 3, 0
            elif choice == "d2":
                row, column = 3, 1
            elif choice == "d3":
                row, column = 3, 2
            elif choice == "d4":
                row, column = 3, 3
            elif choice == "d5":
                row, column = 3, 4
            elif choice == "e1": 
                row, column = 4, 0
            elif choice == "e2":
                row, column = 4, 1
            elif choice == "e3":
                row, column = 4, 2
            elif choice == "e4":
                row, column = 4, 3
            elif choice == "e5":
                row, column = 4, 4
            else:
                print("invalid input. Please enter a valid input (e.g. A1, B3, C5, etc.)")
                continue

            count += 1

            if is_valid_cell == True:
                board_choose[row][column] = player
                return board_choose  
            else:
                return board_choose, True 
        except ValueError:
            print("Invalid input. Please enter a valid input (e.g. A1, B3, C5, etc.).")   

def get_player_move(board_shoot, player):
    '''
    Gets the designated player to choose a position on the board 

    Args:
        board (list): 5x5 grid containing strings                                    
        player (str): The current player (1 or 2) who is making a move
    Return:
        board (list): Updated board with the players chosen move
    '''
    while True:
        try:
            choice = input(f"It is now Player {player}'s turn, please enter your desired move (e.g. A1, B3, C5, etc.): ").lower()
            if choice == "a1": 
                row, column = 0, 0
            elif choice == "a2":
                row, column = 0, 1
            elif choice == "a3":
                row, column = 0, 2
            elif choice == "a4":
                row, column = 0, 3
            elif choice == "a5":
                row, column = 0, 4
            elif choice == "b1":
                row, column = 1, 0
            elif choice == "b2":
                row, column = 1, 1
            elif choice == "b3":
                row, column = 1, 2
            elif choice == "b4":
                row, column = 1, 3
            elif choice == "b5":
                row, column = 1, 4
            elif choice == "c1":
                row, column = 2, 0
            elif choice == "c2":
                row, column = 2, 1
            elif choice == "c3":
                row, column = 2, 2
            elif choice == "c4": 
                row, column = 2, 3
            elif choice == "c5": 
                row, column = 2, 4
            elif choice == "d1":
                row, column = 3, 0
            elif choice == "d2":
                row, column = 3, 1
            elif choice == "d3":
                row, column = 3, 2
            elif choice == "d4":
                row, column = 3, 3
            elif choice == "d5":
                row, column = 3, 4
            elif choice == "e1": 
                row, column = 4, 0
            elif choice == "e2":
                row, column = 4, 1
            elif choice == "e3":
                row, column = 4, 2
            elif choice == "e4":
                row, column = 4, 3
            elif choice == "e5":
                row, column = 4, 4
            else:
                print("invalid input. Please enter a valid input (e.g. A1, B3, C5, etc.)")
                continue

            if is_valid_cell == True: 
                board_shoot[row][column] = player
                return board_shoot, False # false means it is a miss --> define in main
            else:
                return board_shoot, True # true means the player hit --> define in main
        except ValueError:
            print("Invalid input. Please enter a valid input (e.g. A1, B3, C5, etc.).")

def print_status(board_choose, row, col, shipsLeft):
    shipsLeft = 5
    for row in range(0,5):
        for col in range(0, 5):
            if board_choose[row][col] != "⛴":
                shipsLeft += 0
                return shipsLeft
            else:
                shipsLeft -= 1
                return shipsLeft

#def report_result(result):
    #dothis


def is_game_over(shipsLeft):
    if print_status == 0:
        shipsLeft = 0
        return True
    else:
        shipsLeft > 0 and shipsLeft < 6
        return False
    
def choose_player():
    '''
    Chooses who is player 1 and player 2 )
    Args:
        None
    Return:
    
    '''
    player_1 = input("Player 1, please enter your name: ")
    player_2 = input("Player 2, please enter your name: ")
    return player_1
    return player_2

def reset_board(board_shoot, board_choose):
    for row in range(0, 5):
        for col in range (0,5):
            if board_choose[row][col] != "-":
                board_choose[row][col] == "-"
                return board_choose 
            if board_shoot [row][col] != "-":
                board_shoot[row][col] == "-"
                return board_shoot 
def main():
    board_shoot = [[ '-' , '-' , '-' , '-' , '-' ], 
                   [ '-' , '-' , '-' , '-' , '-' ], 
                   [ '-' , '-' , '-' , '-' , '-' ],
                   [ '-' , '-' , '-' , '-' , '-' ],
                   [ '-' , '-' , '-' , '-' , '-' ]]
    board_choose = [[ '-' , '-' , '-' , '-' , '-' ], 
                    [ '-' , '-' , '-' , '-' , '-' ], 
                    [ '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' ],
                    [ '-' , '-' , '-' , '-' , '-' ]]
    p1_name, p2_name, p1_piece, p2_piece = choose_player()
    turns = 1
    while not is_game_over(shipsLeft):
        if turns % 2 == 1:                                                                                 # if the number of turns is odd (% 2 == 1), it is player 1's turn. If the number of turns is even, it is player 2's turn.
            current_player_name = p1_name
            current_piece = p1_piece
        else:
            current_player_name = p2_name
            current_piece = p2_piece

        print(place_ships(board_choose, player))
        print("Choose your five spots for ships!")


    print(display_board_choose(board_choose))
    print(display_board_shoot(board_shoot))
    get_player_move(board_choose, player)

main()