class Solution():
    """
    https://www.codewars.com/kata/conways-game-of-life

    In this finite version of Conway's Game of Life (here is an excerpt of the rules) ...

    The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells,
    each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours,
     which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time,
     the following transitions occur:

    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overcrowding.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    The initial pattern constitutes the seed of the system.
    The first generation is created by applying the above rules simultaneously to every cell in the seed—births and
    deaths occur simultaneously,
    and the discrete moment at which this happens is sometimes called a tick
    (in other words, each generation is a pure function of the preceding one)
    ...implement your own method which will take the initial state as an NxM array of 0's (dead cell) and
    1's (living cell) and return an equally sized array representing the next generation.
    Cells outside the array must be considered dead. Cells that would born out of the array boundaries should be
    ignored (universe never grows beyond the initial NxM grid).
    N.B.: for illustration purposes, 0 and 1 will be represented as ░ and ▓ blocks respectively.
    You can take advantage of the 'htmlize' function to get a text representation of the universe:
    eg:
    print htmlize(cells)
    """

    def __init__(self):
        pass

    def next_gen_01(self, cells):
        """
        intuitive
        """
        if not cells:
            return []
        n_rows, n_cols = len(cells), len(cells[0])
        if n_cols == 0:
            return cells

        rows, cols = list(range(n_rows)), list(range(n_cols))
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

        return cells_next

    def next_gen_02(self, cells):
        """
        compact
        """
        if not cells:
            return []
        n_rows, n_cols = len(cells), len(cells[0])
        if n_cols == 0:
            return cells

        def cell(cells, x, y):
            return cells[y][x] if 0 <= x < n_cols and 0 <= y < n_rows else 0

        def n_neighbors(cells, x, y):
            return sum(cell(cells, x + i, y + j) for (i, j) in
                       ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)))

        def cell_next(cells, x, y):
            return int(n_neighbors(cells, x, y) in ((2, 3) if cells[y][x] else (3,)))

        return [[cell_next(cells, x, y) for x in range(n_cols)] for y in range(n_rows)]

    def next_gen_03(self, cells):
        """
        compact
        """
        if not cells:
            return []
        n_rows, n_cols = len(cells), len(cells[0])
        if n_cols == 0:
            return cells

        def n_neighbors(cells, x, y):
            return sum(
                cells[i][j] for i, j in (
                    (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                    (x, y - 1), (x, y + 1),
                    (x + 1, y - 1), (x + 1, y), (x + 1, y + 1),
                )
                if 0 <= i < n_rows and 0 <= j < n_cols
            )

        cells_next = [[None for _ in range(n_cols)] for _ in range(n_rows)]
        for x in range(n_rows):
            for y in range(n_cols):
                n_nbrs = n_neighbors(cells, x, y)
                if cells[x][y]:
                    cells_next[x][y] = int(2 <= n_nbrs <= 3)
                else:
                    cells_next[x][y] = int(n_nbrs == 3)
        return cells_next


def sets_gen(next_gen):
    import random
    test_sets = []
    for i in range(1000):
        n_rows, n_cols = random.randint(3, 6), random.randint(3, 6)
        cells = [[random.randint(0, 1) for _ in range(n_cols)] for _ in range(n_rows)]
        match = next_gen(cells)
        test_sets.append((
            (cells,),
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
