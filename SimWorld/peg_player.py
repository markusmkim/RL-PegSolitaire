from SimWorld.peg_board import PegBoard
import random
from time import sleep


# Returns all possible actions for the current board
def get_possible_actions(grid):
    possible_actions = []

    size = len(grid)

    # Checks if grid has diamond shape
    if len(grid[0]) > 1:
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 1:

                    # Direction: up
                    if i > 1 and grid[i - 1][j] == 1 and grid[i - 2][j] == 0:
                        possible_actions.append([[i, j], [i - 1, j], [i - 2, j]])

                    # Direction: right
                    if j < size - 2 and grid[i][j + 1] == 1 and grid[i][j + 2] == 0:
                        possible_actions.append([[i, j], [i, j + 1], [i, j + 2]])

                    # Direction: down & right
                    if i < size - 2 and j < size - 2 and grid[i + 1][j + 1] == 1 and grid[i + 2][j + 2] == 0:
                        possible_actions.append([[i, j], [i + 1, j + 1], [i + 2, j + 2]])

                    # Direction: down
                    if i < size - 2 and grid[i + 1][j] == 1 and grid[i + 2][j] == 0:
                        possible_actions.append([[i, j], [i + 1, j], [i + 2, j]])

                    # Direction: left
                    if j > 1 and grid[i][j - 1] == 1 and grid[i][j - 2] == 0:
                        possible_actions.append([[i, j], [i, j - 1], [i, j - 2]])

                    # Direction: up & left
                    if i > 1 and j > 1 and grid[i - 1][j - 1] == 1 and grid[i - 2][j - 2] == 0:
                        possible_actions.append([[i, j], [i - 1, j - 1], [i - 2, j - 2]])

    else:
        for i in range(size):
            for j in range(i + 1):
                if grid[i][j] == 1:

                    # Direction: up
                    if i > 1 and j < len(grid[i]) - 2 and grid[i - 1][j] == 1 and grid[i - 2][j] == 0:
                        possible_actions.append([[i, j], [i - 1, j], [i - 2, j]])

                    # Direction: right
                    if i > 1 and j < len(grid[i]) - 2 and grid[i][j + 1] == 1 and grid[i][j + 2] == 0:
                        possible_actions.append([[i, j], [i, j + 1], [i, j + 2]])

                    # Direction: down & right
                    if i < size - 2 and j < size - 2 and grid[i + 1][j + 1] == 1 and grid[i + 2][j + 2] == 0:
                        possible_actions.append([[i, j], [i + 1, j + 1], [i + 2, j + 2]])

                    # Direction: down
                    if i < size - 2 and grid[i + 1][j] == 1 and grid[i + 2][j] == 0:
                        possible_actions.append([[i, j], [i + 1, j], [i + 2, j]])

                    # Direction: left
                    if j > 1 and grid[i][j - 1] == 1 and grid[i][j - 2] == 0:
                        possible_actions.append([[i, j], [i, j - 1], [i, j - 2]])

                    # Direction: up & left
                    if i > 1 and j > 1 and grid[i - 1][j - 1] == 1 and grid[i - 2][j - 2] == 0:
                        possible_actions.append([[i, j], [i - 1, j - 1], [i - 2, j - 2]])

    return possible_actions


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
        return self.peg_board.total_pegs_left == 1 and self.peg_board.target_nodes_contain_peg


if __name__ == '__main__':
    peg_board = PegBoard(4, True, [[3, 1]])
    peg_player = PegPlayer(peg_board)

    game_over = False

    while not game_over:
        peg_board.visualize_board()
        print("")
        action = peg_player.decide_next_action()
        if action:
            peg_player.execute_action(action)
        else:
            game_over = True
        sleep(1.5)

    if peg_player.has_won():
        print("Du har vunnet!")
    else:
        print("Du vant dessverre ikke denne gang.")

