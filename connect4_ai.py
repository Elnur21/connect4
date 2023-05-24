import random as rnd


class Alpha_Beta:
    def turning(self, board):
        for i in range(5):
            for j in board[:][i]:
                if j == 0:
                    return i
    # we have 5 parameter for creating alpha beta ai
    def alpha_beta_decision(self,board, turn, ai_level, queue, max_player):
        # here we get possible moves from board
        possible_moves = board.get_possible_moves()
        best_move = possible_moves[0]
        best_value = -ai_level
        alpha = -ai_level
        beta = ai_level

        # we created this number to use every move in possible_moves
        random_num = int(rnd.randint(-1, 5))

        # we created this to define this to do useful every rows
        define_row = int(rnd.randint(-1, 5))

        
        if max_player:
            for move in possible_moves:
                # we used the copy of the board for ai to check all the possible moves inside
                updated_board = board.copy()
                # if random_num is 1 then ai will be able to play on the left side
                # if random_num == 1 and move>=3:
                    # if there is an empty(playable) field, AI will fill it in automatically
                if updated_board.grid[move][self.turning(updated_board.grid)]==0:
                    updated_board.grid[move][self.turning(updated_board.grid)] = turn % 2 + 1
                    # we got this value from min_value_ab function like tic-tac-toe
                    value = self.min_value_ab(updated_board, turn+1,ai_level, alpha, beta, 0)
                    # compare our getting value and best value 
                    if value > best_value:
                        # if it is bigger than best value, best value will be this value
                        best_value = value
                        best_move = move
                # if random_num is not 1 then ai will be able to play on the right side
                # else:
                #     # if there is an empty(playable) field, AI will fill it in automatically
                #     if updated_board.grid[move][define_row] == 0:
                #         updated_board.grid[move][define_row] = turn % 2 + 1
                #         # we got this value from min_value_ab function like tic-tac-toe
                #         value = self.min_value_ab(updated_board, turn+1,ai_level, alpha, beta, 0)
                #         # compare our getting value and best value 
                #         if value > best_value:
                #              # if it is bigger than best value, best value will be this value
                #             best_value = value
                #             best_move = move
        else:
            for move in possible_moves:
                updated_board = board.copy()
                if updated_board.grid[move][5] == 0:
                    updated_board.grid[move][5] = turn % 2 + 1
                    value = self.max_value_ab(updated_board, turn+1,ai_level, alpha, beta, 0)
                    if value > best_value:
                        best_value = value
                        best_move = move
                else:
                    continue
        # our best move is applied to game by using this code 
        queue.put(best_move)




    def max_value_ab(self,board, turn,ai_level, alpha, beta, index):
        # if board.check_victory() is true then ai will stop
        if board.check_victory():
            return -1
        # if turn is bigger than 42 then ai will stop
        if turn > 42:
            return 0
        possible_moves = board.get_possible_moves()
        for move in possible_moves:
            value = -ai_level
            updated_board = board.copy()
            if updated_board.grid[move][index] == 0:
                updated_board.grid[move][index] = turn % 2 + 1
                value = self.min_value_ab(updated_board, turn,ai_level, alpha, beta, index)
                if value >= beta:
                    return value
                alpha = max(alpha, value)
            else:
                continue
        return value

    def min_value_ab(self,board, turn,ai_level, alpha, beta, index):
        # if board.check_victory() is true then ai will stop
        if board.check_victory():
            return 1
        # if turn is bigger than 42 then ai will stop
        if turn > 42:
            return 0
        possible_moves = board.get_possible_moves()
        for move in possible_moves:
            value = ai_level
            updated_board = board.copy()
            if updated_board.grid[move][index] == 0:
                updated_board.grid[move][index] = turn % 2 + 1
                value = self.min_value_ab(updated_board, turn,ai_level, alpha, beta, index)
                if value <= alpha:
                    return value
                beta = min(beta, value)
            else:
                continue
        return value


