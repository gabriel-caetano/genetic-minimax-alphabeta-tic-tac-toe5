import random
import time

class Evaluator:
    def __init__(self, weights=None):
        if weights:
            self.w_centro = weights[0]
            self.w_tres_em_linha = weights[1]
            self.w_dois_em_linha = weights[2]
        else:
            self.w_centro = random.uniform(0, 1)
            self.w_tres_em_linha = random.uniform(0, 1)
            self.w_dois_em_linha = random.uniform(0, 1)
    
    def evaluate(self, state):

        score = 0

        # Característica 1: Controle do Centro
        score += self.calculate_center_control(state) * self.w_centro

        # Característica 2: Três em linha com potencial de vitória
        score += self.count_potential_lines(state, 3) * self.w_tres_em_linha

        # Característica 3: Dois em linha com potencial de vitória
        score += self.count_potential_lines(state, 2) * self.w_dois_em_linha

        return score


    def calculate_center_control(self, state):
        control_score = 0
        for r in range(1, 4): # Linhas 1, 2, 3
            for c in range(1, 4): # Colunas 1, 2, 3
                if r == 2 and c == 2: # Peça bem no centro
                    if state.board[r][c] == 'X':
                        control_score += 3
                    else:
                        control_score -= 3
                elif r == 2 or c == 2: # Cruz central
                    if state.board[r][c] == 'X':
                        control_score += 2
                    else:
                        control_score -= 2
                else: # Outras posições do "quadrado central"
                    if state.board[r][c] == 'X':
                        control_score += 1
                    else:
                        control_score -= 1
        return control_score


    def count_potential_lines(self, state, num_pieces_in_line):
        count = 0
        # Verifica horizontalmente
        for r in range(5):
            for c in range(2):
                # print(f"checking horizontal: {r}, {c}")
                window = [state.board[r][c+i] for i in range(4)]
                if (
                    window.count('X') == num_pieces_in_line and
                    window.count(' ') == (4 - num_pieces_in_line) and
                    window.count('O') == 0
                ):
                    count += 1
                if (
                    window.count('O') == num_pieces_in_line and
                    window.count(' ') == (4 - num_pieces_in_line) and
                    window.count('X') == 0
                ):
                    count -= 1

        # Verifica verticalmente
        for c in range(5):
            for r in range(2):
                window = [state.board[r+i][c] for i in range(4)]
                if (
                    window.count('X') == num_pieces_in_line and
                    window.count(' ') == (4 - num_pieces_in_line) and
                    window.count('O') == 0
                ):
                    count += 1
                if (
                    window.count('O') == num_pieces_in_line and
                    window.count(' ') == (4 - num_pieces_in_line) and
                    window.count('X') == 0
                ):
                    count -= 1

        # Verifica diagonal principal ( \ )
        for r in range(2):
            for c in range(2):
                window = [state.board[r+i][c+i] for i in range(4)]
                if (
                    window.count('X') == num_pieces_in_line and
                    window.count(' ') == (4 - num_pieces_in_line) and
                    window.count('O') == 0
                ):
                    count += 1
                if (
                    window.count('O') == num_pieces_in_line and
                    window.count(' ') == (4 - num_pieces_in_line) and
                    window.count('X') == 0
                ):
                    count -= 1

        # Verifica diagonal secundaria ( / )
        for r in range(2):
            for c in range(5-r):
                window = [state.board[r+i][c-i] for i in range(4)]
                if (
                    window.count('X') == num_pieces_in_line and
                    window.count(' ') == (4 - num_pieces_in_line) and
                    window.count('O') == 0
                ):
                    count += 1
                if (
                    window.count('O') == num_pieces_in_line and
                    window.count(' ') == (4 - num_pieces_in_line) and
                    window.count('X') == 0
                ):
                    count -= 1

        return count
