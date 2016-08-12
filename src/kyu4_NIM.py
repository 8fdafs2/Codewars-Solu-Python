from functools import reduce
from operator import xor


class Solution():
    """
    https://www.codewars.com/kata/54120de842dff35232000195

    This kata explores writing an AI for a two player,
    turn based game called NIM.

    The Board
        The board starts out with several piles of straw.
        Each pile has a random number of straws.
        Pile 0: ||||
        Pile 1: ||
        Pile 2: |||||
        Pile 3: |
        Pile 4: ||||||
        ...or more concisely: [4,2,5,1,6]

    The Rules
        The players take turns picking a pile,
        and removing any number of straws from the pile they pick
        A player must pick at least one straw
        If a player picks the last straw, she wins!

    The Task
        In this kata, you have to write an AI to play the straw picking game.
        You have to encode an AI in a function choose_move that takes a board,
        represented as a list of positive integers, and returns
        (pile_index, number_of_straws)
        Which refers to an index of a pile on the board,
        and some none-zero number of straws to draw from that pile.
        The test suite is written so that your AI is expected to play 50 games and win every game it plays.
    """

    def __init__(self):
        pass

    def choose_move_01(self, game_state):
        """
        simplified
        """
        x = reduce(xor, game_state)
        
        if x == 0:
            return next((i, pile) for i, pile in enumerate(game_state) if pile > 0)

        for i, pile in enumerate(game_state):
            if xor(x, pile) < pile:
                return i, pile - xor(x, pile)

    def choose_move_02(self, game_state):
        """
        modified, https://en.wikipedia.org/wiki/Nim
        """
        x = reduce(xor, game_state)

        if x == 0:  # Will lose unless all non-empty game_state have size one
            if max(game_state) > 1:
                pass  # You will lose :(
            # Empty any (non-empty) pile
            return next((i, pile) for i, pile in enumerate(game_state) if pile > 0)

        # the most general algorithm
        pile = [xor(pile, x) < pile for pile in game_state].index(True)
        remov = game_state[pile] - xor(game_state[pile], x)

        # can be commented out since this case has already been included above
        piles_next = list(game_state)
        piles_next[pile] -= remov
        if sum([pile > 1 for pile in piles_next]) == 0:  # If move leaves no pile of size 2 or larger,
            if sum(piles_next) % 2 == 0:  # leave an even number of game_state of size 1
                return pile, remov
            return pile, game_state[pile]

        return pile, remov


def sets_gen(choose_move):
    import random
    test_sets = []
    for i in range(1000):
        game_state = [random.randint(1, 9) for _ in range(random.randint(2, 9))]
        match = choose_move(game_state)
        test_sets.append((
            (game_state,),
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

