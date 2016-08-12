from functools import reduce
from math import gcd


class Solution():
    """
    Write a function that calculates the least common multiple of its arguments;
    each argument is assumed to be a non-negative integer.
    """

    def __init__(self):
        pass

    @staticmethod
    def lcm_01(*args):
        """
        gcd local implementation, reduce
        """

        def _lcm_(a, b):
            a_, b_ = a, b
            while b != 0:
                a, b = b, a % b
            return a_ * b_ // a

        return reduce(_lcm_, args)

    @staticmethod
    def lcm_02(*args):
        """
        math.gcd, reduce
        """

        def _lcm_(a, b):
            return a * b // gcd(a, b)

        return reduce(_lcm_, args)

    @staticmethod
    def lcm_03(*args):
        """
        math.gcd, recursion
        """

        def _lcm_(*args):
            if len(args) == 2:
                a, b = args
                return a * b // gcd(a, b)
            return _lcm_(args[0], _lcm_(*args[1:]))

        return _lcm_(*args)

    @staticmethod
    def lcm_04(*args):
        """
        math.gcd, iteration
        """
        a = args[0]
        for b in args[1:]:
            a *= b // gcd(a, b)
        return a


def sets_gen(lcm):
    import random
    choices = range(1, 10000)
    test_sets = []
    for i in range(1000):
        args = random.sample(choices, random.randint(2, 100))
        match = lcm(*args)
        test_sets.append((
            args,
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
