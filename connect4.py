
#                  board
#        0     1     2     3     4   
#     +-----+-----+-----+-----+-----+
#  0  |     |     |     |     |     |
#     +-----+-----+-----+-----+-----+
#  1  |     |     |     |     |     |
#     +-----+-----+-----+-----+-----+
#  2  |     |     |     |     |     |
#     +-----+-----+-----+-----+-----+
#  3  |     |     |     |     |     |
#     +-----+-----+-----+-----+-----+
#  4  |     |     |     |     |     |
#     +-----+-----+-----+-----+-----+

class Connect4:
    def __init__(self):
        self.board = [[' ']*5 for _ in range(5)]
        self.current_player = 'X'
        self.count_moves = 0
        self.moves_log = ''

    def is_full_board(self):
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == ' ':
                    return False
        return True

    def is_terminal(self):
        player_won = self.has_player_won()
        full_board = self.is_full_board()
        if player_won or full_board:
            return True
        
    def valid_actions(self):
        res = []
        # cortando fora estados espelhados
        if (self.count_moves == 0) or (self.count_moves == 1 and self.board[2][2] != ' '):
            for row in range(3):
                for col in range(row+1):
                    new_state = self.apply_action(row, col)
                    if (new_state):
                        res.append(new_state)

        else:
            is_mid_col = self.board[0][2] != ' ' or self.board[1][2] != ' ' or self.board[3][2] != ' '  or self.board[4][2] != ' ' 
            is_main_diag = self.board[0][0] != ' ' or self.board[1][1] != ' ' or self.board[3][3] != ' '  or self.board[4][4] != ' '
            is_sec_diag = self.board[4][0] != ' ' or self.board[3][1] != ' ' or self.board[1][3] != ' '  or self.board[4][0] != ' '

            if is_mid_col and self.count_moves == 1:
                for row in range(5):
                    for col in range(3):
                        new_state = self.apply_action(row, col)
                        if (new_state):
                            res.append(new_state)

            is_mid_row = self.board[2][0] != ' ' or self.board[2][1] != ' ' or self.board[2][3] != ' '  or self.board[2][4] != ' ' 
            if is_mid_row and self.count_moves == 1:
                for row in range(3):
                    for col in range(5):
                        new_state = self.apply_action(row, col)
                        if (new_state):
                            res.append(new_state)

            elif is_main_diag and self.count_moves == 1:
                for row in range(5):
                    for col in range(row+1):
                        new_state = self.apply_action(row, col)
                        if (new_state):
                            res.append(new_state)

            elif is_sec_diag and self.count_moves == 1:
                col_lim = 5
                for row in range(5):
                    for col in range(col_lim):
                        new_state = self.apply_action(row, col)
                        if (new_state):
                            res.append(new_state)
                    col_lim -= 1

            else:
                for row in range(5):
                    for col in range(5):
                        new_state = self.apply_action(row, col)
                        if (new_state):
                            res.append(new_state)

        return res

    def apply_action(self, row: int, column: int):
        if self.board[row][column] != ' ':
            return None
 
        new_state = Connect4()
        new_board = [row.copy() for row in self.board]

        new_board[row][column] = self.current_player
        new_state.current_player = 'O' if self.current_player == 'X' else 'X'

        new_state.board = new_board
        new_state.count_moves = self.count_moves + 1
        new_state.moves_log = self.moves_log + f"{self.current_player} on {row},{column}\n"
        return new_state
    
    def has_player_won(self):
        # Verifica vitória horizontal
        for row in range(5):
            for col in range(2):  # Colunas 0, 1 (permite 4 peças)
                if (self.board[row][col] != ' ' and
                    self.board[row][col] == self.board[row][col+1] ==
                    self.board[row][col+2] == self.board[row][col+3]):
                    return True

        # Verifica vitória vertical
        for col in range(5):
            for row in range(2):  # Linhas 0, 1 (permite 4 peças)
                if (self.board[row][col] != ' ' and
                    self.board[row][col] == self.board[row+1][col] ==
                    self.board[row+2][col] == self.board[row+3][col]):
                    return True

        # Verifica diagonais decrescente (direita)
        for row in range(2):
            for col in range(2):
                if (self.board[row][col] != ' ' and
                    self.board[row][col] == self.board[row+1][col+1] ==
                    self.board[row+2][col+2] == self.board[row+3][col+3]):
                    return True

        # Verifica diagonais decrescente (esquerda)
        for row in range(2):
            for col in range(3, 5):  # Colunas 3, 4
                if (self.board[row][col] != ' ' and
                    self.board[row][col] == self.board[row+1][col-1] ==
                    self.board[row+2][col-2] == self.board[row+3][col-3]):
                    return True

        return False
    
    def __str__(self):
        result = ["       0     1     2     3     4"]
    
        result.append("    +-----+-----+-----+-----+-----+")
        
        for i in range(5):
            row = f" {i}  |  "
            row += "  |  ".join(f"{self.board[i][j]}" for j in range(5))
            row += "  |"
            result.append(row)
            result.append("    +-----+-----+-----+-----+-----+")
        
        return "\n" + "\n".join(result) + "\n"
