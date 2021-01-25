from Helpers.helpers import get_possible_actions, convert_string_to_list, convert_list_to_string


class PegPlayer:
    def __init__(self, peg_board):
        self.peg_board = peg_board

    # Executes the provided action on the current board
    def execute_action(self, action):
        self.peg_board.execute_move(convert_string_to_list(action))
        reward = 0
        if self.game_over():
            if self.has_won():
                reward = 50
            else:
                reward = 20 - 2*self.peg_board.total_pegs_left
        return convert_list_to_string(self.peg_board.grid), reward

    # Return if the game of solitaire is won or not
    def game_over(self):
        return len(get_possible_actions(convert_list_to_string(self.peg_board.grid))) == 0

    def has_won(self):
        return self.peg_board.total_pegs_left == 1
