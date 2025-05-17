import random

class Evaluator:
    def __init__(self, weights=None):
        self.w_len = 3
        self.w = []
        if weights:

            self.w.append(weights[0])
            self.w.append(weights[1])
            self.w.append(weights[2])
        else:
            self.w.append(random.random())
            self.w.append(random.random())
            self.w.append(random.random())
    
    def evaluate(self, state):
        center_score = self.calculate_center_control(state) * self.w[0]

        tree_lines_score = self.count_potential_lines(state, 3) * self.w[1]

        two_lines_score = self.count_potential_lines(state, 2) * self.w[2]

        return center_score + tree_lines_score + two_lines_score


    def calculate_center_control(self, state):
        control_score = 0
        for r in range(1, 4): # Linhas 1, 2, 3
            for c in range(1, 4): # Colunas 1, 2, 3
                if r == 2 and c == 2: # Peça bem no centro
                    if state.board[r][c] == 'X':
                        control_score += 3
                    elif state.board[r][c] == 'O':
                        control_score -= 3
                elif r == 2 or c == 2: # Cruz central
                    if state.board[r][c] == 'X':
                        control_score += 2
                    elif state.board[r][c] == 'O':
                        control_score -= 2
                else: # Outras posições do "quadrado central"
                    if state.board[r][c] == 'X':
                        control_score += 1
                    elif state.board[r][c] == 'O':
                        control_score -= 1
        return control_score


    def count_potential_lines(self, state, num_pieces_in_line):
        count = 0
        # Verifica horizontalmente
        for r in range(5):
            for c in range(2):
                window = [state.board[r][c+i] for i in range(4)]
                if (
                    window.count('X') == num_pieces_in_line and
                    window.count('O') == 0
                ):
                    count += 1
                if (
                    window.count('O') == num_pieces_in_line and
                    window.count('X') == 0
                ):
                    count -= 1

        # Verifica verticalmente
        for c in range(5):
            for r in range(2):
                window = [state.board[r+i][c] for i in range(4)]
                if (
                    window.count('X') == num_pieces_in_line and
                    window.count('O') == 0
                ):
                    count += 1
                if (
                    window.count('O') == num_pieces_in_line and
                    window.count('X') == 0
                ):
                    count -= 1

        # Verifica diagonal principal ( \ )
        for r in range(2):
            for c in range(2):
                window = [state.board[r+i][c+i] for i in range(4)]
                if (
                    window.count('X') == num_pieces_in_line and
                    window.count('O') == 0
                ):
                    count += 1
                if (
                    window.count('O') == num_pieces_in_line and
                    window.count('X') == 0
                ):
                    count -= 1

        # Verifica diagonal secundaria ( / )
        for r in range(2):
            for c in range(5-r):
                window = [state.board[r+i][c-i] for i in range(4)]
                if (
                    window.count('X') == num_pieces_in_line and
                    window.count('O') == 0
                ):
                    count += 1
                if (
                    window.count('O') == num_pieces_in_line and
                    window.count('X') == 0
                ):
                    count -= 1

        return count
    
    def __str__(self):
        return f"[{self.w[0]:.2f}, {self.w[1]:.2f}, {self.w[2]:.2f}]"
