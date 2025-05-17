import random
from evaluator import Evaluator

class Individual:
    def __init__(self, evaluator=None):
        self.mutation_rate = 0.3
        if evaluator:
            self.evaluator = evaluator
        else:
            self.evaluator = Evaluator()
        self.fitness = 0

    def make_move(self, game):
        move_value = None
        next_move = game
        is_player_one = game.current_player == 'X'
        for move in game.valid_actions():
            value = self.minimax(move, float('-inf'), float('inf'), 1)
            if (
                move_value is None or
                (is_player_one and value > move_value) or
                (not is_player_one and value < move_value)
            ):
                move_value = value
                next_move = move
        
        return next_move

    def addFitness(self, score):
        self.fitness += score

    def minimax(self, state, alpha, beta, depth=0):
        if state.is_terminal() or depth == 0:
            if state.has_player_won():
                if state.current_player == 'X':
                    value = -1000
                else:
                    value = 1000
            else:
                value = self.evaluator.evaluate(state)
            return value

        if state.current_player == 'X':
            max_eval = float('-inf')
            for child in state.valid_actions():
                value = self.minimax(child, alpha, beta, depth - 1)
                max_eval = max(max_eval, value)
                alpha = max(alpha, max_eval)
                if alpha >= beta:
                    break  # Poda Alfa-Beta
            
            return max_eval
        
        else:
            min_eval = float('inf')
            for child in state.valid_actions():
                value = self.minimax(child, alpha, beta, depth - 1)
                min_eval = min(min_eval, value)
                beta = min(beta, min_eval)
                if alpha <= beta:
                    break  # Poda Alfa-Beta

            return min_eval

    def crossover(self, other):
        # crossover
        new_w = [self.evaluator.w[0], other.evaluator.w[1], self.evaluator.w[2]]
        # mutation
        for i in range(len(new_w)):
            chance = random.random()
            if (chance < self.mutation_rate):
                new_w[i] = self.apply_mutation(new_w[i])

        new_evaluator = Evaluator(new_w)
        return Individual(new_evaluator)

    def apply_mutation(self, val):
        chance = random.random()
        if (chance < 0.1): # each mutation has 10% chance to get a totally new value
            return random.random()
        elif (chance > 0.55): # 45% chance to increase slightly
            return val * 1.1
        else:# 45% chance to decrease slightly
            return val * 0.9




    def __str__(self):
        return f"{self.evaluator}, {self.fitness}"
