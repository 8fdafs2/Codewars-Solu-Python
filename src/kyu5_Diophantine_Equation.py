from math import sqrt


class Solution():
    """
    In mathematics, a Diophantine equation is a polynomial equation,
    usually in two or more unknowns, such that only the integer solutions are sought or studied.

    In this kata we want to find all integers x, y (x >= 0, y >= 0) solutions of a diophantine equation of the form

     x ^ 2 - 4 * y ^ 2 = n

    where the unknowns are x and y and n is a given positive number.
    Solutions x, y will be given as an array of arrays (Ruby, Python, Clojure, JS, CS, TS)

     [[x1, y1], [x2, y2] ....]

    as an array of tuples (Haskell, C++, Elixir)

     [(x1, y1), (x2, y2) ....] or { {x1, y1}, {x2, y2} ....} or [{x1, y1}, {x2, y2} ....]

    and as a string (Java, C#)

     "[[x1, y1], [x2, y2] ....]"

    in decreasing order of the positive xi. If there is no solution returns [] or "[]".

    Examples:

    sol_equa(90005) -->  [[45003, 22501], [9003, 4499], [981, 467], [309, 37]]

    sol_equa(90002) --> []

    (Java, C#)

    solEquaStr(90005) --> "[[45003, 22501], [9003, 4499], [981, 467], [309, 37]]"

    solEquaStr(90002) --> "[]"

    Hint: x ^ 2 - 4 y ^ 2 = (x - 2y) (x + 2y).
    """

    def __init__(self):
        pass

    def sol_equa_01(self, n):
        """
        lack of i upper bound
        """

        # i = 1, 2, 3, ..., n
        # (x - 2y) = i
        # (x + 2y) = n // i

        ret = []

        for i in range(1, n + 1):
            a, b = divmod(n, i)
            if a < i:
                break
            if b == 0:
                _2x = i + a
                _4y = a - i
                if _2x % 2 == 0 and _4y % 4 == 0:
                    ret.append([_2x // 2, _4y // 4])

        return ret

    def sol_equa_01_(self, n):
        """
        i upper bound
        """

        # i = 1, 2, 3, ..., n
        # (x - 2y) = i
        # (x + 2y) = n // i

        ret = []

        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                _2x = i + n // i
                _4y = _2x - i - i
                if _2x % 2 == 0 and _4y % 4 == 0:
                    ret.append([_2x // 2, _4y // 4])

        return ret


def sets_gen(sol_equa):
    test_sets = []
    for n in range(1, 10001):
        match = sol_equa(n)
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
    tf.test_spd(10, prt_docstr=True)
