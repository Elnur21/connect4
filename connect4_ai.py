class Alpha_Beta:
    def turning(self, board):
        for i in range(5):
            for j in board[:][i]:
                if j == 0:
                    return i

    def alpha_beta_decision(self, board, turn, ai_level, queue, max_player):
        possible_moves = board.get_possible_moves()
        best_move = possible_moves[0]
        best_value = -float('inf') if max_player else float('inf')
        alpha = -float('inf')
        beta = float('inf')

        for move in possible_moves:
            updated_board = board.copy()

            if max_player:
                index = self.turning(updated_board.grid)
            else:
                index = 5

            if updated_board.grid[move][index] == 0:
                updated_board.grid[move][index] = turn % 2 + 1
                value = self.min_value_ab(updated_board, turn + 1, ai_level, alpha, beta, 0)
                if max_player and value > best_value:
                    best_value = value
                    best_move = move
                    alpha = max(alpha, best_value)
                elif not max_player and value < best_value:
                    best_value = value
                    best_move = move
                    beta = min(beta, best_value)

        queue.put(best_move)

    def max_value_ab(self, board, turn, ai_level, alpha, beta, index):
        if board.check_victory():
            return -1
        if turn > 42:
            return 0

        possible_moves = board.get_possible_moves()
        value = -float('inf')

        for move in possible_moves:
            updated_board = board.copy()
            if updated_board.grid[move][index] == 0:
                updated_board.grid[move][index] = turn % 2 + 1
                value = max(value, self.min_value_ab(updated_board, turn, ai_level, alpha, beta, index))
                if value >= beta:
                    return value
                alpha = max(alpha, value)

        return value

    def min_value_ab(self, board, turn, ai_level, alpha, beta, index):
        if board.check_victory():
            return 1
        if turn > 42:
            return 0

        possible_moves = board.get_possible_moves()
        value = float('inf')

        for move in possible_moves:
            updated_board = board.copy()
            if updated_board.grid[move][index] == 0:
                updated_board.grid[move][index] = turn % 2 + 1
                value = min(value, self.max_value_ab(updated_board, turn, ai_level, alpha, beta, index))
                if value <= alpha:
                    return value
                beta = min(beta, value)

        return value
