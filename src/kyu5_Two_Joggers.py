import math


class Solution():
    """
    https://www.codewars.com/kata/two-joggers

    Bob and Charles are meeting for their weekly jogging tour.
    They both start at the same spot called "Start" and they each run a different lap,
    which may (or may not) vary in length.
    Since they know each other for a long time already, they both run at the exact same speed.

    Illustration

        Example where Charles (dashed line) runs a shorter lap than Bob:

        Example laps

    Task

        Your job is to complete the function nbrOfLaps(x, y) that,
        given the length of the laps for Bob and Charles,
        finds the number of laps that each jogger has to complete before they meet each other again,
        at the same time, at the start.

    The function takes two arguments:

        The length of Bob's lap (larger than 0)
        The length of Charles' lap (larger than 0)

    The function should return an array containing exactly two numbers:

        The first number is the number of laps that Bob has to run
        The second number is the number of laps that Charles has to run

    Examples

        nbr_of_laps(5, 3) # returns [3,5]
        nbr_of_laps(4, 6); # returns [3, 2]
    """

    def __init__(self):
        pass

    @staticmethod
    def nbr_of_laps_01(x, y):
        """
        math.gcd
        """
        _gcd_ = math.gcd(x, y)
        return [y // _gcd_, x // _gcd_]

    @staticmethod
    def nbr_of_laps_02(x, y):
        """
        gcd
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        _gcd_ = gcd(x, y)
        return [y // _gcd_, x // _gcd_]

    @staticmethod
    def nbr_of_laps_03(x, y):
        """
        gcd, args pre-ordered
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        if x < y:
            _gcd_ = gcd(y, x)
        else:
            _gcd_ = gcd(x, y)
        return [y // _gcd_, x // _gcd_]

    @staticmethod
    def nbr_of_laps_04(x, y):
        """
        gcd, bitwise
        """
        def gcd(a, b):
            if a == b:
                return a
            if a == 0:
                return b
            if b == 0:
                return a
            if ~a & 1:
                if b & 1:
                    return gcd(a >> 1, b)
                return gcd(a >> 1, b >> 1) << 1
            if ~b & 1:
                return gcd(a, b >> 1)
            if a > b:
                return gcd((a - b) >> 1, b)
            return gcd((b - a) >> 1, a)

        _gcd_ = gcd(x, y)
        return [y // _gcd_, x // _gcd_]

    @staticmethod
    def nbr_of_laps_05(x, y):
        """
        lcm
        """
        def lcm(a, b):
            a_, b_ = a, b
            while b != 0:
                a, b = b, a % b
            return a_ * b_ // a

        lcm = lcm(x, y)
        return [lcm // x, lcm // y]

    @staticmethod
    def nbr_of_laps_06(x, y):
        """
        brute force
        """
        if x < y:
            m = y
            while m % x != 0:
                m += y
        else:
            m = x
            while m % y != 0:
                m += x
        return [m // x, m // y]


def sets_gen(nbr_of_laps):
    import random
    choices = range(1, 10000)
    test_sets = []
    for i in range(1000):
        x, y = random.sample(choices, 2)
        match = nbr_of_laps(x, y)
        test_sets.append((
            (x, y),
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
