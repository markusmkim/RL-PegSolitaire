from SimWorld.peg_board import PegBoard
import random


class PegPlayer:
    def __init__(self, peg_board):
        self.peg_board = peg_board

    # Decides the next action to be executed
    def decide_next_action(self):
        all_possible_actions = self.peg_board.all_possible_actions()
        if len(all_possible_actions) == 0:
            return False
        return all_possible_actions[random.randrange(len(all_possible_actions))]

    # Executes the provided action on the current board
    def execute_action(self, action):
        self.peg_board.execute_action(action)

    # Return if the game of solitaire is won or not
    def has_won(self):
        return self.peg_board.total_pegs_left == 1 and self.peg_board.target_nodes_contain_peg


if __name__ == '__main__':
    peg_board = PegBoard(4, True, [[3, 3]])
    peg_player = PegPlayer(peg_board)

    game_over = False

    while not game_over:
        peg_board.print_board()
        print("")
        action = peg_player.decide_next_action()
        if action:
            peg_player.execute_action(action)
        else:
            game_over = True

    if peg_player.has_won():
        print("Du har vunnet!")
    else:
        print("Du vant dessverre ikke denne gang.")

