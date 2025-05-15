from conecta4 import Connecta4
from minimax import minimax

def player_move(game, is_player_one):
    move_value = None
    next_move = game
    for move in game.valid_actions():
        value = minimax(move, float('-inf'), float('inf'), 1)
        print(f"Move: {move}, Value: {value}")
        if (
            move_value is None or
            (is_player_one and value > move_value) or
            (not is_player_one and value < move_value)
        ):
            move_value = value
            next_move = move
    
    return next_move

def main():
    game = Connecta4()
    is_player_one = True

    game = player_move(game, is_player_one)
    print(game)
    is_player_one = not is_player_one
    game = player_move(game, is_player_one)
    print(game)

    # while not game.is_terminal():

    # if game.has_player_won():
    #     print(f"Player {game.current_player} lose!")
    # else:
    #     print("It's a draw!")

if __name__ == "__main__":
    main()