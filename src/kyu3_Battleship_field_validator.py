class Solution():
    """
    https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

    Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

    Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.


    Before the game begins, players set up the board and place the ships accordingly to the following rules:
    There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
    Each ship must be a straight line, except for submarines, which are just single cell.

    The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

    This is all you need to solve this kata. If you're interested in more information about the game, visit this link.
    """

    def __init__(self):
        pass

    @staticmethod
    def validateBattlefield_01(field):
        """
        intuitive
        """
        f = [r[:] for r in field]
        ret = []
        for i in range(10):
            for j in range(10):
                if f[i][j]:
                    if ((j < 9 and f[i][j + 1] and i < 9 and f[i + 1][j]) or
                        (i < 9 and j > 0 and f[i + 1][j - 1]) or
                            (i > 0 and j < 9 and f[i - 1][j + 1])):
                        return False
                    f[i][j] = 0
                    c = 1
                    for k in range(i + 1, 10):
                        if not f[k][j]:
                            break
                        if (j < 9 and k < 9 and f[k + 1][j + 1]):
                            return False
                        f[k][j] = 0
                        c += 1
                    if c != 1:
                        if c > 4:
                            return False
                        ret.append(c)
                        continue
                    for k in range(j + 1, 10):
                        if not f[i][k]:
                            break
                        if ((i < 9 and k < 9 and f[i + 1][k + 1]) or
                                (i > 0 and k < 9 and f[i - 1][k + 1])):
                            return False
                        f[i][k] = 0
                        c += 1
                    if c > 4:
                        return False
                    ret.append(c)
        return sorted(ret) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

    @staticmethod
    def validateBattlefield_02(field):
        """

        """
        def cell(i, j):
            if i < 0 or j < 0 or i > 9 or j > 9:
                return 0
            return field[i][j]

        def find(i, j):
            if cell(i + 1, j - 1) or cell(i + 1, j + 1):
                return 10086
            if cell(i, j + 1) and cell(i + 1, j):
                return 10086
            field[i][j] = 2
            if cell(i, j + 1):
                return find(i, j + 1) + 1
            if cell(i + 1, j):
                return find(i + 1, j) + 1
            return 1
        num = [0] * 5
        for i in range(10):
            for j in range(10):
                if cell(i, j) == 1:
                    r = find(i, j)
                    if r > 4:
                        return False
                    num[r] += 1
        [tmp, submarines, destroyers, cruisers, battleship] = num
        return battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4

    @staticmethod
    def validateBattlefield_03(field):
        """

        """
        from scipy.signal import convolve2d as conv
        b = [[[[1 for j in range(i)]], [[1] for j in range(i)]] for i in range(1, 5)]
        b += [[[[1, 0], [0, 1]], [[0, 1], [1, 0]]]]
        count = [1, 2, 3, 4, 2]
        c = [40, 10, 4, 1, 0]
        for i in range(5):
            c0 = conv(field, b[i][0])
            c1 = conv(field, b[i][1])
            if sum([list(j).count(count[i]) for j in c0]) + sum([list(j).count(count[i]) for j in c1]) != c[i]:
                return False
        return True

    @staticmethod
    def validateBattlefield_04(field):
        """

        """
        field = [r[:] for r in field]

        SHIPS = {4: 1, 3: 2, 2: 3, 1: 4}

        def scan(c, field, x=1):
            n_c = []
            field[c[0]][c[1]] = 0
            for i in range(max(0, c[0] - 1), min(9, c[0] + 2)):
                for j in range(max(0, c[1] - 1), min(9, c[1] + 2)):
                    if field[i][j] == 1:
                        if abs(i + j) - abs(c[0] + c[1]) == 2:
                            return False
                        n_c += [i, j]
                        if len(n_c) != 2:
                            return False
            if len(n_c) != 0:
                return scan(n_c, field, x + 1)
            SHIPS.update({x: SHIPS.get(x) - 1})

        for i in range(10):
            for j in range(10):
                if field[i][j] == 1 and scan([i, j], field) is False:
                    return False
        for x in SHIPS:
            if SHIPS.get(x) != 0:
                return False
        return True


def sets_gen(subsol):

    fields = [

        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

    ]

    import random
    test_sets = []
    for field in fields:
        match = subsol(field)
        test_sets.append((
            (field,),
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
