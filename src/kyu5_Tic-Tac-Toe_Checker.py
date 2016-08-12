import re
from itertools import chain


class Solution():
    """
    https://www.codewars.com/kata/tic-tac-toe-checker

    If we were to set up a Tic-Tac-Toe game,
    we would want to know whether the board's current state is solved,
    wouldn't we? Our goal is to create a function that will check that for us!

    Assume that the board comes in the form of a 3x3 array,
    where the value is 0 if a spot is empty, 1 if it is an X, or 2 if it is an O, like so:

    [[0,0,1],
     [0,1,2],
     [2,1,0]]
    We want our function to return -1 if the board is not solved yet,
    1 if X won, 2 if O won, or 0 if it's a cat's game (i.e. a draw).

    You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
    """

    def __init__(self):
        pass

    def isSolved_01(self, board):
        """
        intuitive
        """
        for rows in (board, zip(*board), [
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]],
        ]):
            for row in rows:
                if row.count(1) == 3:
                    return 1
                elif row.count(2) == 3:
                    return 2

        if 0 in board[0] + board[1] + board[2]:
            return -1
        return 0

    def isSolved_02(self, board):
        """
        itertools.chain
        """
        board_flattened = list(chain(*board))

        for i, j, k in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if board_flattened[i] == board_flattened[j] == board_flattened[k] != 0:
                return board_flattened[i]

        return 0 if sum(board_flattened) == 13 else -1

    def isSolved_03(self, board):
        """
        regex
        """
        match = re.search(r'([12])(?:..\1..\1|.{7}\1.{7}\1|.{10}\1.{10}\1|.{13}\1.{13}\1)', str(board))

        if match:
            return int(match.group(1))
        return -int('0' in str(board))

    def isSolved_04(self, board):
        """
        intuitive
        """
        for i in range(0, 3):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != 0:
                return board[0][i]

        if board[0][0] == board[1][1] == board[2][2] != 0:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != 0:
            return board[0][2]

        if 0 not in board[0] + board[1] + board[2]:
            return 0
        return -1


def sets_gen(isSolved):
    import random
    alls = [1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0]
    test_sets = []
    for i in range(100):
        random.shuffle(alls)
        it = iter(alls)
        board = [[it.next() for _ in range(3)] for _ in range(3)]
        match = isSolved(board)
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
    tf.test_spd(100, prt_docstr=True)
