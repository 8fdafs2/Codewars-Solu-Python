import numpy as np


class Solution():
    """
    https://www.codewars.com/kata/did-i-finish-my-sudoku

    Write a function done_or_not passing a board (list[list_lines]) as parameter.
    If the board is valid return 'Finished!', otherwise return 'Try again!'

    Sudoku rules:

        Complete the Sudoku puzzle so that each and every row, column,
        and region contains the numbers one through nine only once.

    Rows:

        There are 9 rows in a traditional Sudoku puzzle.
        Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        There may not be any duplicate numbers in any row.
        In other words, there can not be any rows that are identical.

        In the illustration the numbers 5, 3, 1, and 2 are the "givens".
        They can not be changed.
        The remaining numbers in black are the numbers that you fill in to complete the row.

    Columns:

        There are 9 columns in a traditional Sudoku puzzle.
        Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

        In the illustration the numbers 7, 2, and 6 are the "givens".
        They can not be changed.
        You fill in the remaining numbers as shown in black to complete the column.

    Regions

        A region is a 3x3 box like the one shown to the left.
        There are 9 regions in a traditional Sudoku puzzle.

        Like the Sudoku requirements for rows and columns,
        every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        Duplicate numbers are not permitted in any region.
        Each region will differ from the other regions.

        In the illustration the numbers 1, 2, and 8 are the "givens".
        They can not be changed. Fill in the remaining numbers as shown in black to complete the region.

    Valid board example:

        For those who don't know the game,
        here are some information about rules and how to play Sudoku:
        http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/
    """

    def __init__(self):
        pass

    def done_or_not_01(self, board):
        """
        intuitive
        """

        validset = set([i for i in range(1, 10)])

        for row in board:
            if set(row) != validset:
                return 'Try again!'

        for col in zip(*board):
            if set(col) != validset:
                return 'Try again!'

        for blk in [board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
                    for i in [0, 3, 6] for j in [0, 3, 6]]:
            if set(blk) != validset:
                return 'Try again!'

        return 'Finished!'

    def done_or_not_02(self, board):
        """
        numpy
        """
        board = np.array(board)

        rows = [board[i, :] for i in range(9)]
        cols = [board[:, j] for j in range(9)]
        blks = [board[i:i + 3, j:j + 3].flatten() for i in [0, 3, 6] for j in [0, 3, 6]]

        for view in np.vstack((rows, cols, blks)):
            if len(np.unique(view)) != 9:
                return 'Try again!'

        return 'Finished!'

    def done_or_not_03(self, board):
        """
        numpy
        """
        rows = np.array(board)
        cols = np.transpose(rows)
        blks = [np.ndarray.flatten(rows[i:i + 3, j:j + 3]) for i in [0, 3, 6] for j in [0, 3, 6]]

        vaildset = list(range(1, 10))

        for test in [rows, cols, blks]:
            for group in test:
                if sorted(group) != vaildset:
                    return 'Try again!'

        return 'Finished!'


def sets_gen(done_or_not):
    test_sets = []
    boards = [
        [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]],
        [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 0, 3, 4, 9],
         [1, 0, 0, 3, 4, 2, 5, 6, 0],
         [8, 5, 9, 7, 6, 1, 0, 2, 0],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 0, 1, 5, 3, 7, 2, 1, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 0, 0, 4, 8, 1, 1, 7, 9]],
        [[1, 3, 2, 5, 7, 9, 4, 6, 8],
         [4, 9, 8, 2, 6, 1, 3, 7, 5],
         [7, 5, 6, 3, 8, 4, 2, 1, 9],
         [6, 4, 3, 1, 5, 8, 7, 9, 2],
         [5, 2, 1, 7, 9, 3, 8, 4, 6],
         [9, 8, 7, 4, 2, 6, 5, 3, 1],
         [2, 1, 4, 9, 3, 5, 6, 8, 7],
         [3, 6, 5, 8, 1, 7, 9, 2, 4],
         [8, 7, 9, 6, 4, 2, 1, 5, 3]],
        [[1, 3, 2, 5, 7, 9, 4, 6, 8],
         [4, 9, 8, 2, 6, 1, 3, 7, 5],
         [7, 5, 6, 3, 8, 4, 2, 1, 9],
         [6, 4, 3, 1, 5, 8, 7, 9, 2],
         [5, 2, 1, 7, 9, 3, 8, 4, 6],
         [9, 8, 7, 4, 2, 6, 5, 3, 1],
         [2, 1, 4, 9, 3, 5, 6, 8, 7],
         [3, 6, 5, 8, 1, 7, 9, 2, 4],
         [8, 7, 9, 6, 4, 2, 1, 3, 5]],
        [[1, 3, 2, 5, 7, 9, 4, 6, 8],
         [4, 9, 8, 2, 6, 0, 3, 7, 5],
         [7, 0, 6, 3, 8, 0, 2, 1, 9],
         [6, 4, 3, 1, 5, 0, 7, 9, 2],
         [5, 2, 1, 7, 9, 0, 8, 4, 6],
         [9, 8, 0, 4, 2, 6, 5, 3, 1],
         [2, 1, 4, 9, 3, 5, 6, 8, 7],
         [3, 6, 0, 8, 1, 7, 9, 2, 4],
         [8, 7, 0, 6, 4, 2, 1, 3, 5]],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9],
         [2, 3, 4, 5, 6, 7, 8, 9, 1],
         [3, 4, 5, 6, 7, 8, 9, 1, 2],
         [4, 5, 6, 7, 8, 9, 1, 2, 3],
         [5, 6, 7, 8, 9, 1, 2, 3, 4],
         [6, 7, 8, 9, 1, 2, 3, 4, 5],
         [7, 8, 9, 1, 2, 3, 4, 5, 6],
         [8, 9, 1, 2, 3, 4, 5, 6, 7],
         [9, 1, 2, 3, 4, 5, 6, 7, 8]],
    ]
    for b in boards:
        match = done_or_not(b)
        test_sets.append((
            (b,),
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
