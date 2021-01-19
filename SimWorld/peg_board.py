
class PegBoard:
    def __init__(self, size, isDiamond, empty_nodes):
        self.size = size
        self.isDiamond = isDiamond

        if isDiamond:
            self.grid = self.create_diamond_grid(size, empty_nodes)

        else:
            self.grid = self.create_triangle_grid(size, empty_nodes)



    def create_triangle_grid(self, size, empty_nodes):
        grid = []
        for i in range(size):
            row = []
            for j in range(i + 1):
                if [i, j] in empty_nodes:
                    row.append(0)
                else:
                    row.append(1)

            grid.append(row)

        return grid


    def create_diamond_grid(self, size, empty_nodes):
        grid = []
        for i in range(size):
            row = []
            for j in range(size):
                if [i, j] in empty_nodes:
                    row.append(0)
                else:
                    row.append(1)

            grid.append(row)

        return grid


    def get_possible_actions(self):
        possible_actions = []
        grid = self.grid
        size = self.size

        if self.isDiamond:
            for i in range(size):
                for j in range(size):
                    if grid[i][j] == 1:
                        if i > 1 and grid[i - 1][j] == 1 and grid[i - 2][j] == 0:
                            possible_actions.append([[i, j], [i - 1, j], [i - 2, j]])

                        if j < size - 2 and grid[i][j + 1] == 1 and grid[i][j + 2] == 0:
                            possible_actions.append([[i, j], [i, j + 1], [i, j + 2]])

                        if i < size - 2 and j < size - 2 and grid[i + 1][j + 1] == 1 and grid[i + 2][j + 2] == 0:
                            possible_actions.append([[i, j], [i + 1, j + 1], [i + 2, j + 2]])

                        if i < size - 2 and grid[i + 1][j] == 1 and grid[i + 2][j] == 0:
                            possible_actions.append([[i, j], [i + 1, j], [i + 2, j]])

                        if j > 1 and grid[i][j - 1] == 1 and grid[i][j - 2] == 0:
                            possible_actions.append([[i, j], [i, j - 1], [i, j - 2]])

                        if i > 1 and j > 1 and grid[i - 1][j - 1] == 1 and grid[i - 2][j - 2] == 0:
                            possible_actions.append([[i, j], [i - 1, j - 1], [i - 2, j - 2]])

        return possible_actions

    def execute_action(self, action):
        self.grid[action[0][0]][action[0][1]] = 0
        self.grid[action[1][0]][action[1][1]] = 0
        self.grid[action[2][0]][action[2][1]] = 1


    def print_board(self):
        for i in range(self.size):
            print(self.grid[i], i)

if __name__ == '__main__':
    board = PegBoard(4, True, [[3, 3]])

    print(board.print_board())

    print('Actions:')
    pa = board.get_possible_actions()
    for i in pa:
        print(i)

    action = [[1, 1], [2, 2], [3, 3]]
    print('Excecuting action, ', action)
    board.execute_action(action)

    print(board.print_board())




