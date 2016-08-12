class Solution():
    """
    https://www.codewars.com/kata/5326ef17b7320ee2e00001df

    In this kata, you will have to implement a method solve(map, miner, exit)
    that has to return the path the miner must take to reach the exit as an array of moves,
    such as : ['up', 'down', 'right', 'left']. There are 4 possible moves, up, down, left and right, no diagonal.

    map is a 2-dimensional array of boolean values, representing squares.
    false for walls, true for open squares (where the miner can walk).
    It will never be larger than 5 x 5. It is laid out as an array of columns.
    All columns will always be the same size, though not necessarily the same size as rows
    (in other words, maps can be rectangular).
    The map will never contain any loop, so there will always be only one possible path.
    The map may contain dead-ends though.

    miner is the position of the miner at the start,
    as an object made of two zero-based integer properties, x and y.
    For example {x:0, y:0} would be the top-left corner.

    exit is the position of the exit, in the same format as miner.

    Note that the miner can't go outside the map, as it is a tunnel.

    Let's take a pretty basic example :

    map = [[True, False],
           [True, True]]

    solve(map, {'x':0,'y':0}, {'x':1,'y':1})
    // Should return ['right', 'down']
    """
    def __init__(self):
        pass

    def solve_01(self, map, miner, exit):
        """
        recursion, last step recorded, intuitive if-return combination
        """
        cp = {
            'left': 'right',
            'right': 'left',
            'up': 'down',
            'down': 'up',
        }

        s_x, s_y = miner['x'], miner['y']
        e_x, e_y = exit['x'], exit['y']
        x_max, y_max = len(map) - 1, len(map[0]) - 1

        def recur(s_x, s_y, path):

            if s_x != e_x or s_y != e_y:
                if s_x > 0 and path[-1] != cp['left'] and map[s_x - 1][s_y]:
                    _path_ = recur(s_x - 1, s_y, path + ['left', ])
                    if _path_:
                        return _path_
                if s_x < x_max and path[-1] != cp['right'] and map[s_x + 1][s_y]:
                    _path_ = recur(s_x + 1, s_y, path + ['right', ])
                    if _path_:
                        return _path_
                if s_y > 0 and path[-1] != cp['up'] and map[s_x][s_y - 1]:
                    _path_ = recur(s_x, s_y - 1, path + ['up', ])
                    if _path_:
                        return _path_
                if s_y < x_max and path[-1] != cp['down'] and map[s_x][s_y + 1]:
                    _path_ = recur(s_x, s_y + 1, path + ['down', ])
                    if _path_:
                        return _path_
            else:
                return path[1:]

        return recur(s_x, s_y, [None, ])

    def solve_02(self, map, miner, exit):
        """
        recursion, last step recorded, dict
        """
        dirs = {
            'left': {'s_xy': lambda x, y: (x - 1, y), 'dir': 'right'},
            'right': {'s_xy': lambda x, y: (x + 1, y), 'dir': 'left'},
            'up': {'s_xy': lambda x, y: (x, y - 1), 'dir': 'down'},
            'down': {'s_xy': lambda x, y: (x, y + 1), 'dir': 'up'},
        }

        s_xy = miner['x'], miner['y']
        e_xy = exit['x'], exit['y']
        x_max, y_max = len(map) - 1, len(map[0]) - 1

        def recur(s_xy, dir_last=None):

            if s_xy == e_xy:
                return []
            s_x, s_y = s_xy
            if not (0 <= s_x <= x_max and 0 <= s_y <= y_max and map[s_x][s_y]):
                return

            for dir_cp, move in list(dirs.items()):
                if dir_last != dir_cp:
                    path = recur(move['s_xy'](s_x, s_y), move['dir'])
                    if path is not None:
                        return [dir_cp, ] + path

        return recur(s_xy)

    def solve_03(self, map, miner, exit):
        """
        recursion, all steps recorded, dict
        """
        dxy2dir = {
            (-1, 0): 'up',
            (1, 0): 'down',
            (0, -1): 'left',
            (0, 1): 'right',
        }

        s_xy = miner['x'], miner['y']
        e_xy = exit['x'], exit['y']
        x_max, y_max = len(map) - 1, len(map[0]) - 1

        s_xy_past = []

        def recur(s_xy):

            if s_xy in s_xy_past:
                return
            s_xy_past.append(s_xy)

            if s_xy == e_xy:
                return []
            s_x, s_y = s_xy
            if not (0 <= s_x <= x_max and 0 <= s_y <= y_max and map[s_x][s_y]):
                return

            for (dy, dx) in dxy2dir:
                path = recur((s_x + dx, s_y + dy))
                if path is not None:
                    return [dxy2dir[(dy, dx)], ] + path

        return recur(s_xy)


def sets_gen(solve):
    test_sets = [
        [[[[1]], {'x': 0, 'y': 0}, {'x': 0, 'y': 0}], ],
        [[[[1, 0],
           [1, 1]], {'x': 0, 'y': 0}, {'x': 1, 'y': 0}], ],
        [[[[1, 0],
           [1, 1]], {'x': 0, 'y': 0}, {'x': 1, 'y': 1}], ],
        [[[[1],
           [1],
           [1],
           [1]], {'x': 0, 'y': 0}, {'x': 3, 'y': 0}], ],
        [[[[1],
           [1],
           [1],
           [1]], {'x': 3, 'y': 0}, {'x': 0, 'y': 0}], ],
        [[[[1, 1, 1],
           [0, 0, 1],
           [1, 1, 1]], {'x': 0, 'y': 0}, {'x': 2, 'y': 0}], ],
        [[[[1, 1, 0, 0, 0],
           [0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0],
           [0, 0, 0, 1, 1],
           [0, 0, 0, 0, 1]], {'x': 0, 'y': 0}, {'x': 4, 'y': 4}], ],
        [[[[1, 1, 1, 0, 1],
           [0, 0, 1, 0, 1],
           [1, 1, 1, 1, 1],
           [1, 0, 1, 0, 0],
           [0, 1, 1, 1, 1]], {'x': 0, 'y': 0}, {'x': 4, 'y': 4}], ],
    ]
    for test_set in test_sets:
        test_set.append(solve(*test_set[0]))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10000, prt_docstr=True)
