class Solution():
    """
    https://www.codewars.com/kata/make-a-spiral

    Your task, is to create a NxN spiral with a given size.

    For example, spiral with size 5 should look like this:

    00000
    ....0
    000.0
    0...0
    00000

    and with the size 10:

    0000000000
    .........0
    00000000.0
    0......0.0
    0.0000.0.0
    0.0..0.0.0
    0.0....0.0
    0.000000.0
    0........0
    0000000000

    Return value should contain array of arrays, of 0 and 1,
    for example for given size * result should be:
    size 3:
    [[1,1,1],
     [0,0,1],
     [1,1,1]]

    size 4:
    [[1,1,1,1],
     [0,0,0,1],
     [1,0,0,1],
     [1,1,1,1]]

    size 5:
    [[1,1,1,1,1],
     [0,0,0,0,1],
     [1,1,1,0,1],
     [1,0,0,0,1],
     [1,1,1,1,1]]

    size 6:
    [[1,1,1,1,1,1],
     [0,0,0,0,0,1],
     [1,1,1,1,0,1],
     [1,0,0,1,0,1],
     [1,0,0,0,0,1],
     [1,1,1,1,1,1]]

    size 7:
    [[1,1,1,1,1,1,1],
     [0,0,0,0,0,0,1],
     [1,1,1,1,1,0,1],
     [1,0,0,0,1,0,1]
     [1,0,1,1,1,0,1],
     [1,0,0,0,0,0,1],
     [1,1,1,1,1,1,1]]

    size 8:
    [[1,1,1,1,1,1,1,1],
     [0,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,0,1],
     [1,0,0,0,0,1,0,1],
     [1,0,1,0,0,1,0,1],
     [1,0,1,1,1,1,0,1],
     [1,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,1,1]]

    size 9:
    [[1,1,1,1,1,1,1,1,1],
     [0,0,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,1,0,1],
     [1,0,0,0,0,0,1,0,1],
     [1,0,1,1,1,0,1,0,1],
     [1,0,1,0,0,0,1,0,1],
     [1,0,1,1,1,1,1,0,1],
     [1,0,0,0,0,0,0,0,1],
     [1,1,1,1,1,1,1,1,1]]

    Because of the edge-cases for tiny spirals, the size will be at least 5.

    General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.

    """

    def __init__(self):
        pass

    def spiralize_01(self, size):
        """
        top -> center <- bot
        """
        if size == 0:
            return []
        if size == 1:
            return [[1, ]]
        if size == 2:
            return [[1, 1], [0, 1]]

        flag = size % 4
        size_h = size // 2

        if flag == 0:
            a, b = size_h, size_h - 2
        elif flag == 1:
            a, b = size_h, size_h - 1
        elif flag == 2:
            a, b = size_h - 1, size_h - 1
        else:
            a, b = size_h, size_h - 1

        ret_l = [[1, ] * size, ]
        ret_u = [[1, ] * size,
                 [0, ] * (size - 1) + [1, ]]

        val = 1
        for i in range(1, a):
            val = 0 if val == 1 else 1
            r = ret_l[-1]
            ret_l.append(r[:i] + [val, ] * (size - i - i) + r[-i:])
        ret_l.reverse()
        if b > 0:
            val = 1
            ret_u.append([1, ] * (size - 2) + [0, 1])
            for i in range(1, b):
                val = 0 if val == 1 else 1
                r = ret_u[-1]
                ret_u.append(r[:i] + [val, ] * (size - i - i - 2) + r[-i - 2:])

        return ret_u + ret_l

    def spiralize_02(self, size):
        """
        rings -> half diagonal invert
        """
        spiral = []
        for i in range(size):
            spiral.append([])
            for j in range(size):
                spiral[-1].append(1 - min(i, j, size - max(i, j) - 1) % 2)

        for i in range(size // 2 - (size % 4 == 0)):
            spiral[i + 1][i] = 1 - spiral[i + 1][i]
        return spiral

    def spiralize_03(self, size):
        """
        rings -> half diagonal invert
        """
        spiral = [[0, ] * size for _ in range(size)]

        for i in range(0, (size + 1) // 2, 2):
            size_i = size - i
            for j in range(i, size_i):
                spiral[i][j] = spiral[j][i] = spiral[size_i - 1][j] = spiral[j][size_i - 1] = 1

        for i in range(size // 2 - (size % 4 == 0)):
            spiral[i + 1][i] = 1 - spiral[i + 1][i]

        return spiral

    def spiralize_04(self, size):
        """
        binary bitwise
        """
        if size == 0:
            return []

        if size % 2 != 0:
            j = [1, ]
        elif size % 4 != 0:
            j = [3, 1]
        else:
            j = [3, 3]

        for s in reversed(range(size, 2, -2)):
            # print('s:', s)
            j = [2 ** s - 1] + \
                list(
                    map(
                        (lambda a, b, c: c or (a ^ (b << 1))),
                        [2 ** s - 1] * (s - 2),
                        j,
                        [1, ] + [0, ] * (s - 3),
                    )
                ) + \
                [2 ** s - 1]
            # print(j)

        return [list(map(int, '{{:0>{:d}b}}'.format(size).format(row))) for row in j]

    def spiralize_05(self, size):
        """
        outer -> inner
        """
        _spirals_ = {
            0: [],
            1: [[1]],
            2: [[1, 1],
                [0, 1]],
            3: [[1, 1, 1],
                [0, 0, 1],
                [1, 1, 1]],
            4: [[1, 1, 1, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 1, 1, 1]]
        }

        def recur(size):
            if size in _spirals_:
                return _spirals_[size]

            spiral_inner = recur(size - 4)
            spiral = [
                         [1, ] * size,
                         [0, ] + [0, ] * (size - 2) + [1, ],
                         [1, 1] + spiral_inner[0] + [0, 1],
                     ] + [
                         [1, 0] + spiral_inner[i] + [0, 1] for i in range(1, size - 4)
                         ] + [
                         [1, ] + [0, ] * (size - 2) + [1, ],
                         [1, ] * size,
                     ]
            # the line below caches the result which is useless in current context
            # _spirals_[size] = spiral
            return spiral

        return recur(size)

    def spiralize_06(self, size):
        """
        game play, snake::1, pre-calc
        """
        if size == 0:
            return []
        if size == 1:
            return [[1, ]]

        # Fill top row with '1's and rest with '0's
        spiral = [
                     [1, ] * size,
                 ] + [
                     [0, ] * size for _ in range(size - 1)
                     ]
        # Locations and directions
        row, col = 0, size - 1
        hor, ver = 0, 1
        # Loop for the length of the spiral's arm
        for n in range(size - 1, 0, -2):
            # Loop for the number of arms of this length
            m = 2 if n > 2 else n
            for _ in range(m):
                # Loop for each '1' in this arm
                for _ in range(n):
                    row += ver
                    col += hor
                    spiral[row][col] = 1
                # Change direction
                hor, ver = -ver, hor

        return spiral

    def spiralize_07(self, size):
        """
        game play, snake::0, no turning control
        """

        def is_one(y, x):
            return 0 <= y < size and 0 <= x < size and spiral[y][x] == 1

        spiral = [[1, ] * size for _ in range(size)]
        y, x = 1, -1
        dy, dx = 0, 1

        y_dy, x_dx = y + dy, x + dx
        while is_one(y_dy, x_dx):
            if is_one(y_dy + dy, x_dx + dx):
                y += dy
                x += dx
            else:
                dx, dy = -dy, dx
            spiral[y][x] = 0
            y_dy, x_dx = y + dy, x + dx

        return spiral

    def spiralize_08(self, size):
        """
        game play, snake::1, turning control
        """

        def is_one(x, y):
            return 0 <= x < size and 0 <= y < size and spiral[y][x] == 1

        def can_move(x, y, dx, dy):
            x, y = x + dx, y + dy
            return 0 <= x < size and 0 <= y < size and not is_one(x + dx, y + dy)

        def can_turn(x, y, dx, dy):
            x, y = x - dy, y + dx
            return 0 <= x < size and 0 <= y < size and not (is_one(x - dy, y + dx) or is_one(x - dx, y - dy))

        spiral = [[0, ] * size for _ in range(size)]
        x, y = -1, 0
        dx, dy = 1, 0

        while True:
            if can_move(x, y, dx, dy):
                x += dx
                y += dy
                spiral[y][x] = 1
                continue
            if can_turn(x, y, dx, dy):
                dx, dy = -dy, dx
                continue
            break

        return spiral

    def spiralize_09(self, size):
        """
        coordinate peel rot
        """

        range_size = list(range(size))

        def _rot(arr, i=0):

            if not arr or (len(arr) < 2 and i == min(size, 3)):
                return ()

            if i == min(size, 3):
                return arr[0][:-1] + _rot(list(zip(*arr[1:]))[::-1][1:], i)

            return arr[0] + _rot(list(zip(*arr[1:]))[::-1], i + 1)

        a = [tuple([(i, j) for j in range_size]) for i in range_size]

        pos = set(_rot(a))  # hashtab

        return [[1 if (i, j) in pos else 0 for j in range_size] for i in range_size]


def spr_prt(spiral):
    print('-' * len(spiral))
    for r in spiral:
        print(r)
    print('-' * len(spiral))


def sets_gen(spiralize):
    test_sets = []
    for size in range(0, 51):
        match = spiralize(size)
        test_sets.append((
            (size,),
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
