from itertools import islice
from io import StringIO
import sys


class Solution():
    """
    https://www.codewars.com/kata/53ea3ad17b5dfe1946000278

    Write a function that takes an integer n and returns the nth iteration of the fractal known as Sierpinski's Gasket.

    Here are the first few iterations.
    The fractal is composed entirely of L and white-space characters;
    each character has one space between it and the next (or a newline).

    0:
        L

    1:
        L
        L L

    2:
        L
        L L
        L   L
        L L L L

    3:
        L
        L L
        L   L
        L L L L
        L       L
        L L     L L
        L   L   L   L
        L L L L L L L L
    """

    def __init__(self):
        pass

    def sierpinski_01(self, n):
        """
        math
        """
        pat = ['L', ]

        tmp = 1
        for _ in range(n):
            for j in range(tmp):
                pat.append(pat[j] + ' ' * ((tmp << 1) - (j << 1) - 1) + pat[j])
            tmp <<= 1

        return '\n'.join(pat)

    def sierpinski_02(self, n):
        """
        ljust, recursion
        """

        def recur(n):
            if n == 0:
                return ['L']

            last = recur(n - 1)
            tmp = 2 ** n
            return last + [row.ljust(tmp) + row for row in last]

        return '\n'.join(recur(n))

    def sierpinski_03(self, n):
        """
        ljust
        """
        pat = ['L', ]

        tmp = 1
        for _ in range(n):
            for row in pat[:tmp]:
                pat.append(row.ljust(tmp << 1) + row)
            tmp <<= 1

        return '\n'.join(pat)

    def sierpinski_04(self, n):
        """
        rule
        """
        # original rule for one dimensional Cellular Automata no 126 (http://www.wolframalpha.com/input/?i=ca+rule+126)
        # rule = {
        #  (1, 1, 1): 0,
        #  (1, 1, 0): 1,
        #  (1, 0, 1): 1,
        #  (1, 0, 0): 1,
        #  (0, 1, 1): 1,
        #  (0, 1, 0): 1,
        #  (0, 0, 1): 1,
        #  (0, 0, 0): 0
        # }
        rule = {
            (1, 1, 1): 0,
            (1, 1, 0): 0,
            (1, 0, 1): 1,
            (1, 0, 0): 1,
            (0, 1, 1): 1,
            (0, 1, 0): 1,
            (0, 0, 1): 0,
            (0, 0, 0): 0
        }

        steps = [[1]]

        for i in range(2 ** n - 1):
            laststep = [0, ] + steps[-1] + [0, 0]
            steps.append([rule[tuple(laststep[c:c + 3])] for c in range(len(laststep) - 2)])

        return '\n'.join([' '.join(['L' if c else ' ' for c in step]) for step in steps])

    def sierpinski_05(self, n):
        """
        format
        """
        rows = ['L', ]

        tmp = 1
        for i in range(n):
            padding = '{{0:{0}s}}{{0}}'.format(tmp << 1)
            rows.extend((padding.format(row) for row in islice(rows, tmp)))
            tmp *= 2

        return '\n'.join(rows)

    def sierpinski_06(self, n):
        """
        matrix, stringio
        """
        out = StringIO()

        size = 2 ** n
        for i in range(1, size + 1):
            c = 1
            for j in range(1, i):
                # print(c)
                out.write('L ' if c % 2 != 0 else '  ')
                c *= i - j
                c //= j
            out.write('L\n')

        return out.getvalue()[:-1]

    def sierpinski_07(self, n):
        """
        matrix, 0 or 1 -> ' ' or 'L'
        """
        size = 2 ** n
        m = [[1, ] + [0, ] * (size - 1) for _ in range(size)]

        for i in range(1, size):
            for j in range(1, i + 1):
                if m[i - 1][j] != m[i - 1][j - 1]:
                    m[i][j] = 1

        return '\n'.join([' '.join(['L' if c == 1 else ' ' for c in m[i][:i + 1]]) for i in range(size)])

    def sierpinski_08(self, n):
        """
        matrix
        """
        size = 2 ** n
        m = [['L', ] + [' ', ] * (size - 1) for _ in range(size)]

        for i in range(1, size):
            for j in range(1, i + 1):
                if m[i - 1][j] != m[i - 1][j - 1]:
                    m[i][j] = 'L'

        return '\n'.join([' '.join(m[i][:i + 1]) for i in range(size)])


def sets_gen(sierpinski):
    test_sets = []
    for n in range(10):
        match = sierpinski(n)
        test_sets.append((
            (n,),
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
