import random
from SimWorld.helpers import get_possible_actions


class PegPlayer:
    def __init__(self, peg_board):
        self.peg_board = peg_board

    # Decides the next action to be executed
    def decide_next_action(self):
        all_possible_actions = get_possible_actions(self.peg_board.grid)
        if len(all_possible_actions) == 0:
            return False
        return all_possible_actions[random.randrange(len(all_possible_actions))]

    # Executes the provided action on the current board
    def execute_action(self, action):
        self.peg_board.execute_action(action)

    # Return if the game of solitaire is won or not
    def has_won(self):
        return self.peg_board.total_pegs_left == 1



