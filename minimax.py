
from evaluator import Evaluator
evaluator = Evaluator(weights=[1,1,1])


def minimax(state, alpha, beta, depth=0):
    if state.is_terminal() or depth == 0:
        if state.has_player_won():
            if state.current_player == 'X':
                value = -1000
            else:
                value = 1000
        else:
            value = evaluator.evaluate(state)
        return value

    
    if state.current_player == 'X':
        max_eval = float('-inf')
        for child in state.valid_actions():
            value = minimax(child, alpha, beta, depth - 1)
            max_eval = max(max_eval, value)
            alpha = max(alpha, max_eval)
            if beta >= alpha:
                break  # Poda Alfa-Beta
        
        return max_eval
    
    else:
        min_eval = float('inf')
        for child in state.valid_actions():
            value = minimax(child, alpha, beta, depth - 1)
            min_eval = min(min_eval, value)
            beta = min(beta, min_eval)
            if beta <= alpha:
                break  # Poda Alfa-Beta

        return min_eval