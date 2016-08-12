from functools import reduce


def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<br/>')
    return ''.join(s)


def visualize(cells):
    s = []
    for row in cells:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)


class Solution():
    """
    https://www.codewars.com/kata/52423db9add6f6fc39000354

    Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

    The rules of the game are:
        1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
        2. Any live cell with more than three live neighbours dies, as if by overcrowding.
        3. Any live cell with two or three live neighbours lives on to the next generation.
        4. Any dead cell with exactly three live neighbours becomes a live cell.

    Each cell's neighborhood is the 8 cells immediately around it.
    The universe is infinite in both the x and y dimensions and all cells are initially dead
    except for those specified in the arguments.
    The return value should be a 2d array cropped around all of the living cells.
    (If there are no living cells, then return [[]].)

    For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively.
    You can take advantage of the htmlize function to get a text representation of the universe: eg:

    print htmlize(cells)
    """

    def __init__(self):
        pass

    def get_generation_01(self, cells, generations):
        """
        intuitive
        """
        for g in range(generations):

            n_rows, n_cols = len(cells), len(cells[0])
            if n_cols == 0:
                return cells

            n_rows, n_cols = n_rows + 2, n_cols + 2
            rows, cols = list(range(n_rows)), list(range(n_cols))
            cells = [[0, ] * n_cols] + \
                    [[0, ] + row + [0, ] for row in cells] + \
                    [[0, ] * n_cols]
            cells_next = [list(row) for row in cells]

            for i_row in rows:
                for i_col in cols:
                    neighbours = 0

                    if i_row == 0:  # top
                        neighbours += cells[i_row + 1][i_col]  # bot
                        if i_col == 0:  # top-left
                            neighbours += cells[i_row][i_col + 1]  # right
                            neighbours += cells[i_row + 1][i_col + 1]  # bot-right
                        elif i_col == n_cols - 1:  # top-right
                            neighbours += cells[i_row][i_col - 1]  # left
                            neighbours += cells[i_row + 1][i_col - 1]  # bot-left
                        else:  # top-mediate
                            neighbours += cells[i_row][i_col - 1]  # left
                            neighbours += cells[i_row][i_col + 1]  # right
                            neighbours += cells[i_row + 1][i_col - 1]  # bot-left
                            neighbours += cells[i_row + 1][i_col + 1]  # bot-right

                    elif i_row == n_rows - 1:  # bot
                        neighbours += cells[i_row - 1][i_col]  # top
                        if i_col == 0:  # bot-left
                            neighbours += cells[i_row][i_col + 1]  # right
                            neighbours += cells[i_row - 1][i_col + 1]  # top-right
                        elif i_col == n_cols - 1:  # bot-right
                            neighbours += cells[i_row][i_col - 1]  # left
                            neighbours += cells[i_row - 1][i_col - 1]  # top-left
                        else:  # bot-mediate
                            neighbours += cells[i_row][i_col - 1]  # left
                            neighbours += cells[i_row][i_col + 1]  # right
                            neighbours += cells[i_row - 1][i_col - 1]  # top-left
                            neighbours += cells[i_row - 1][i_col + 1]  # top-right

                    else:  # mediate
                        neighbours += cells[i_row - 1][i_col]  # top
                        neighbours += cells[i_row + 1][i_col]  # bot
                        if i_col == 0:  # mediate-left
                            neighbours += cells[i_row][i_col + 1]  # right
                            neighbours += cells[i_row - 1][i_col + 1]  # top-right
                            neighbours += cells[i_row + 1][i_col + 1]  # bot-right
                        elif i_col == n_cols - 1:  # mediate-right
                            neighbours += cells[i_row][i_col - 1]  # left
                            neighbours += cells[i_row - 1][i_col - 1]  # top-left
                            neighbours += cells[i_row + 1][i_col - 1]  # bot-left
                        else:  # mediate-mediate
                            neighbours += cells[i_row][i_col - 1]  # left
                            neighbours += cells[i_row][i_col + 1]  # right
                            neighbours += cells[i_row - 1][i_col - 1]  # top-left
                            neighbours += cells[i_row - 1][i_col + 1]  # top-right
                            neighbours += cells[i_row + 1][i_col - 1]  # bot-left
                            neighbours += cells[i_row + 1][i_col + 1]  # bot-right

                    cell = cells[i_row][i_col]
                    if cell == 1 and (neighbours < 2 or neighbours > 3):
                        cells_next[i_row][i_col] = 0
                    elif cell == 0 and neighbours == 3:
                        cells_next[i_row][i_col] = 1

            cells = cells_next
            i_rows_alive = [any(row) for row in cells]
            if True not in i_rows_alive:
                return [[]]
            cells = cells[
                    i_rows_alive.index(True)
                    :
                    n_rows - i_rows_alive[::-1].index(True)
                    ]
            cells = [
                row[min([row.index(1) for row in cells if 1 in row])
                :
                max([n_cols - row[::-1].index(1) for row in cells if 1 in row])] for row in cells
                ]

        return cells

    def get_generation_02(self, cells, generations):
        """
        rows <=> cols, sum neighbours
        """
        for g in range(generations):

            n_rows, n_cols = len(cells), len(cells[0])
            if n_cols == 0:
                return [[]]

            # extend rows; rows <=> cols; extend rows; rows <=> cols
            for _n_cols_ in (n_cols, n_rows + 4):
                cells = list(map(list, zip(*([[0, ] * _n_cols_] * 2 + cells + [[0, ] * _n_cols_] * 2))))

            # evolve matrix
            n_rows, n_cols = n_rows + 4, n_cols + 4

            # cells_next = []
            # for x in range(n_rows)[1: -1]:
            #     cells_next.append([])
            #     for y in range(n_cols)[1: -1]:
            #         neighbours = sum(sum((cells[x_][y - 1:y + 2] for x_ in range(x - 1, x + 2)), [])) - cells[x][y]
            #         cell = (0, 0, cells[x][y], 1, 0, 0, 0, 0, 0)[neighbours]
            #         cells_next[-1].append(cell)
            # cells = cells_next

            cells = [
                [(0, 0, cells[x][y], 1, 0, 0, 0, 0, 0)[sum(
                    sum((cells[x_][y - 1:y + 2] for x_ in range(x - 1, x + 2)),
                        [])
                ) - cells[x][y]]
                 for y in range(1, n_cols - 1)] for x in range(1, n_rows - 1)
                ]

            # crop rows; rows <=> cols; crop rows; rows <=> cols
            for _n_rows_ in (n_rows - 2, n_cols - 2):
                i_rows_alive = [any(row) for row in cells]
                if True not in i_rows_alive:
                    return [[]]
                cells = list(map(list, zip(*cells[
                                            i_rows_alive.index(True)
                                            :
                                            _n_rows_ - i_rows_alive[::-1].index(True)
                                            ])))

        return cells


def sets_gen(get_generation):
    import random
    test_sets = []
    for i in range(100):
        n_rows, n_cols = random.randint(3, 6), random.randint(3, 6)
        cells = [[random.randint(0, 1) for _ in range(n_cols)] for _ in range(n_rows)]
        generations = random.randint(0, 20)
        match = get_generation(cells, generations)
        test_sets.append((
            (cells, generations),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
