class Solution():
    """
    https://www.codewars.com/kata/529bf0e9bdf7657179000008

    Sudoku Background

    Sudoku is a game played on a 9x9 grid.
    The goal of the game is to fill all cells of the grid with digits from 1 to 9,
    so that each column, each row, and each of the nine 3x3 sub-grids
    (also known as blocks) contain all of the digits from 1 to 9.
    (More info at: http://en.wikipedia.org/wiki/Sudoku)

    Sudoku Solution Validator

    Write a function validSolution that accepts a 2D array representing a Sudoku board,
    and returns true if it is a valid solution, or false otherwise.
    The cells of the sudoku board may also contain 0's,
    which will represent empty cells.
    Boards containing one or more zeroes are considered to be invalid solutions.

    Examples:

    validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                   [3, 4, 5, 2, 8, 6, 1, 7, 9]])
    //Example 1 should return true

    validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                   [6, 7, 2, 1, 9, 0, 3, 4, 8],
                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                   [3, 0, 0, 4, 8, 1, 1, 7, 9]])
    //Example 2 should returns false
    """

    def __init__(self):
        pass

    @staticmethod
    def subsol_01(board):
        """
        intuitive
        """
        for row in board:
            if 0 in row or len(set(row)) != 9:
                return False

        for col in zip(*board):
            if 0 in col or len(set(col)) != 9:
                return False

        for i_row_set in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            for i_col_set in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
                blk = [board[i_row][i_col]
                       for i_col in i_col_set for i_row in i_row_set]
                if len(set(blk)) != 9:
                    return False

        return True

    @staticmethod
    def subsol_02(board):
        """
        hashtab
        """
        for i in range(9):
            row = {}
            col = {}
            blk = {}
            for j in range(9):
                ele = board[i][j]
                if ele == 0 or ele in row:
                    return False
                row[ele] = None
                ele = board[j][i]
                if ele == 0 or ele in col:
                    return False
                col[ele] = None
                # i // 3 * 3    -> 0, 0, 0, 3, 3, 3, 6, 6, 6
                # j // 3        -> 0, 0, 0, 1, 1, 1, 2, 2, 2
                # +             -> 0, 0, 0, 4, 4, 4, 8, 8, 8
                # i % 3 * 3     -> 0, 3, 6, 0, 3, 6, 0, 3, 6
                # j % 3         -> 0, 1, 2, 0, 1, 2, 0, 1, 2
                # +             -> 0, 4, 8, 0, 4, 8, 0, 4, 8
                ele = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
                if ele == 0 or ele in blk:
                    return False
                blk[ele] = None

        return True

    @staticmethod
    def subsol_03(board):
        """
        hashtab
        """
        valid_set = set(range(1, 10))
        blks = [
            [board[x + a][y + b] for a in (0, 1, 2) for b in (0, 1, 2)]
            for x in (0, 3, 6) for y in (0, 3, 6)
        ]
        return not any(set(x) != valid_set for x in board + list(zip(*board)) + blks)

    @staticmethod
    def subsol_04(board):
        """
        hashtab
        """
        # return all(len(set(x)) == 9                             \
        #     for x in chain(board, zip(*board),                   \
        #         chain.from_iterable(                              \
        #             tuple(tuple(chain.from_iterable(               \
        #                 row[j : j + 3]                              \
        #                     for row in threeRows))                   \
        #                         for j in (0, 3, 6))                   \
        #                             for threeRows in (board[i : i + 3] \
        #                                 for i in (0, 3, 6)))))
        from itertools import chain
        valid_set = set(range(1, 10))
        return any(
            set(x) != valid_set for x in chain(
                board, zip(*board), chain.from_iterable(
                    (
                        chain.from_iterable(row[j: j + 3] for row in three_rows) for j in (0, 3, 6)
                    ) for three_rows in (board[i: i + 3] for i in (0, 3, 6))
                )
            )
        )


def sets_gen(subsol):
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
    test_sets = []
    for i in range(len(boards)):
        board = boards[i]
        match = subsol(board)
        test_sets.append((
            (board,),
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
