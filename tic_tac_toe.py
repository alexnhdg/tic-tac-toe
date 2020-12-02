"""
tic_tac_toe.py
By Alexander de Groot

A program to play a game of Tic-Tac-Toe with two players at the command line.
"""

import functions as f

print("WELCOME TO TIC-TAC-TOE!")
print("This game requires two players: one who will be 'X' and one who will\n"
    "be 'O'. The first player to get three in a row wins the game!\n")

game_on = f.play_game_q("Do you want to play?")



while game_on:

    f.clear()
    
    # Set up game components
    game_markers = f.assign_markers()
    game_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    player_wins = ['#', False, False]
    positions_available = True
    
    # Play the game
    while (player_wins[1] == False and player_wins[2] == False) and positions_available:
        for player in range(1,3):
            f.display_board(game_board)
            game_board = f.update_board(game_board, game_markers, player)
            player_wins[player] = f.check_win(game_board, game_markers, player)
            positions_available = f.check_positions_available(game_board)
            if player_wins[player] or positions_available == False:
                break
    
    f.display_board(game_board)
    
    if player_wins[1] == player_wins[2]:
        print("The game is tied! No one wins. Womp.\n")
    elif player_wins[1] == True:
        print("Player 1 is the winner! Congratulations!\n")
    elif player_wins[2] == True:
        print("Player 2 is the winner! Congratulations!\n")
        
    game_on = f.play_game_q("Do you want to play again?")

f.clear()

print("Thanks for playing! Good bye!")