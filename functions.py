"""
functions.py
By Alexander de Groot

Functions used in tic_tac_toe.py.
"""

import os, time


def clear():
    """Clear the system console."""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def assign_markers():
    """Assign markers for player 1 and player 2."""
    
    markers = ['#', '', '']
    
    invalid_marker = True
    
    while invalid_marker:
        
        marker_player1 = input("Player 1: Select a marker for the game "
            "('X' or 'O'): ").upper()
        
        if marker_player1 not in ['X', 'O']:
            print("Please enter 'X' or 'O'.\n")
        else:
            invalid_marker = False
            
    if marker_player1 == 'X':
        markers[1] = 'X'
        markers[2] = 'O'
    else:
        markers[1] = 'O'
        markers[2] = 'X'
        
    print(f"Player 1 is assigned marker '{markers[1]}' and Player 2 is "
        f"assigned marker '{markers[2]}'. The game will start in 5 seconds.")
    
    time.sleep(5)
    
    return markers


def display_board(board):
    """Display game board."""
    
    clear()
    
    print(f'       |       |       ')
    print(f'   {board[1]}   |   {board[2]}   |   {board[3]}   ')
    print(f'       |       |       ')
    print(f'-----------------------')
    print(f'       |       |       ')
    print(f'   {board[4]}   |   {board[5]}   |   {board[6]}   ')
    print(f'       |       |       ')
    print(f'-----------------------')
    print(f'       |       |       ')
    print(f'   {board[7]}   |   {board[8]}   |   {board[9]}   ')
    print(f'       |       |       ')
    print('')


def update_board(board, markers, player): 
    """Update the game board."""
    
    invalid_position = True
    
    while invalid_position:
        
        position = input(f"Player {player}: In which position on the game "
            "board do you want to place your marker? ")
        
        if (position.isdigit() == False) or (int(position) not in range(1,10)):
            print("Please enter an integer from 1 to 9.\n")
        elif board[int(position)] in ['X', 'O']:
            print("A marker already exists in this position. Please enter a "
                "different position.\n")
        else:
            invalid_position = False
        
    board[int(position)] = markers[player]
    
    return board


def check_win(board, markers, player):
    """Check if there is a win"""
    
    return ((board[1] == board[2] == board[3] == markers[player]) or
            (board[4] == board[5] == board[6] == markers[player]) or
            (board[7] == board[8] == board[9] == markers[player]) or
            (board[1] == board[4] == board[7] == markers[player]) or
            (board[2] == board[5] == board[8] == markers[player]) or
            (board[3] == board[6] == board[9] == markers[player]) or
            (board[1] == board[5] == board[9] == markers[player]) or
            (board[3] == board[5] == board[7] == markers[player]))


def play_game_q(question):
    """
    A function that asks a player a yes or no question and returns
    TRUE for yes and FALSE for no.
    """
    
    invalid_response = True
    
    while invalid_response:
        
        response = input(question + ' ').upper()
        
        if response not in ['YES', 'NO', 'Y', 'N']:
            print("Invalid response. Please enter 'Yes' or 'No'.\n")
        else:
            invalid_response = False
                  
    return response in ['YES', 'Y']


def check_positions_available(board):
    """Check if positions are available on the game board."""
    
    available_positions = []

    for i in range(1, 10):
        available_positions.append(board[i] not in ['X', 'O'])
        
    return any(available_positions)

    # return (board[1] not in ['X', 'O'] or
    #         board[2] not in ['X', 'O'] or
    #         board[3] not in ['X', 'O'] or
    #         board[4] not in ['X', 'O'] or
    #         board[5] not in ['X', 'O'] or
    #         board[6] not in ['X', 'O'] or
    #         board[7] not in ['X', 'O'] or
    #         board[8] not in ['X', 'O'] or
    #         board[9] not in ['X', 'O'])