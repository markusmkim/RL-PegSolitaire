from Helpers.helpers import get_possible_actions, convert_string_to_list, convert_list_to_string


class PegPlayer:
    def __init__(self, peg_board, reward_win, reward_lose):
        self.peg_board = peg_board
        self.reward_win = reward_win
        self.reward_lose = reward_lose

    # Executes the provided action on the current board
    def execute_action(self, action):
        self.peg_board.execute_move(convert_string_to_list(action))
        reward = 0
        if self.game_over():
            if self.has_won():
                reward = self.reward_win  # 100  # table critic works ok with 50
            else:
                reward = self.reward_lose  # max(5 - 2*self.peg_board.total_pegs_left, 0)
        return convert_list_to_string(self.peg_board.grid), reward

    # Return if the game of solitaire is won or not
    def game_over(self):
        return len(get_possible_actions(convert_list_to_string(self.peg_board.grid))) == 0

    def has_won(self):
        return self.peg_board.total_pegs_left == 1
