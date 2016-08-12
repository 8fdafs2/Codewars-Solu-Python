from functools import reduce
from itertools import chain, islice, zip_longest
from collections import Counter


class Solution():
    """
    https://www.codewars.com/kata/dont-drink-the-water

    Don't Drink the Water

    Given a two-dimensional array representation of a glass of mixed liquids,
    sort the array such that the liquids appear in the glass based on their density.
    (Lower density floats to the top) The width of the glass will not change from top to bottom.

    ======================
    |   Density Chart    |
    ======================
    | Honey   | H | 1.36 |
    | Water   | W | 1.00 |
    | Alcohol | A | 0.87 |
    | Oil     | O | 0.80 |
    ----------------------

    [                            [
     ['H', 'H', 'W', 'O'],        ['O','O','O','O']
     ['W', 'W', 'O', 'W'],  =>    ['W','W','W','W']
     ['H', 'H', 'O', 'O']         ['H','H','H','H']
     ]                           ]

    The glass representation may be larger or smaller.
    If a liquid doesn't fill a row, it floats to the top and to the left.
    """

    def __init__(self):
        pass

    def separate_liquids_01(self, glass):
        """
        chain + recreate + slice
        """
        if not glass:
            return []

        n_cols = len(glass[0])

        c = Counter(chain(*glass))
        liquids = list(c['O'] * 'O' + c['A'] * 'A' + c['W'] * 'W' + c['H'] * 'H')

        return [liquids[i:i + n_cols] for i in range(0, len(liquids), n_cols)]

    def separate_liquids_02(self, glass):
        """
        sum + dict + islice
        """
        if not glass:
            return []

        densitytab = {
            'H': 1.36,
            'W': 1.00,
            'A': 0.87,
            'O': 0.80,
        }

        n_cols = len(glass[0])

        liquids = sum(glass, [])
        liquids.sort(key=lambda x: densitytab[x])

        def chunks(it, n):
            item = list(islice(it, n))
            while item:
                yield item
                item = list(islice(it, n))

        return list(chunks(iter(liquids), n_cols))

    def separate_liquids_03(self, glass):
        """
        reduce + index + slice
        """
        if not glass:
            return []

        n_rows = len(glass)
        n_cols = len(glass[0])

        liquids = reduce(list.__add__, glass)
        liquids.sort(key=lambda x: 'OAWH'.index(x))

        return [liquids[i * n_cols:(i + 1) * n_cols] for i in range(n_rows)]

    def separate_liquids_04(self, glass):
        """
        join + replace + zip_longest
        """
        if not glass:
            return []

        n_cols = len(glass[0])

        liquids = ''.join([''.join(r) for r in glass])
        liquids = sorted(liquids.replace('H', '3').replace('W', '2').replace('A', '1').replace('O', '0'))
        liquids = ''.join([''.join(r) for r in liquids])
        liquids = list(liquids.replace('3', 'H').replace('2', 'W').replace('1', 'A').replace('0', 'O'))

        return [list(r) for r in zip_longest(*[iter(liquids)] * n_cols)]


def sets_gen(separate_liquids):
    import random
    test_sets = []
    componets = 'OAWH'
    for i in range(0, 101):
        n_rows = n_cols = i
        glass = [[random.choice(componets) for _ in range(n_cols)] for _ in range(n_rows)]
        match = separate_liquids(glass)
        test_sets.append((
            (glass,),
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
