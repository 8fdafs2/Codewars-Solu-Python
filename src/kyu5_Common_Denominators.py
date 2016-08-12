from functools import reduce
from math import gcd


class Solution():
    """
    https://www.codewars.com/kata/common-denominators

    You will have a list of rationals in the form

        [ [numer_1, denom_1] , ... [numer_n, denom_n] ]

    where all numbers are positive ints.

    You have to produce a result in the form

        [ [N_1, D] ... [N_n, D] ]

    in which D is as small as possible and

        N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.

    Example :

        [ [1, 2], [1, 3], [1, 4] ] produces the array [ [6,12], [4,12], [3,12] ]
    """

    def __init__(self):
        pass

    @staticmethod
    def convertFracts_01(lst):
        """
        gcd local implementation, reduce
        """

        def lcm(a, b):
            a_, b_ = a, b
            while b != 0:
                a, b = b, a % b
            return a_ * b_ // a

        _lcm_ = reduce(lcm, [d for n, d in lst])
        return [[_lcm_ // d * n, _lcm_] for n, d in lst]

    @staticmethod
    def convertFracts_02(lst):
        """
        math.gcd, reduce
        """
        def lcm(a, b):
            return a * b // gcd(a, b)

        _lcm_ = reduce(lcm, [d for n, d in lst])
        return [[_lcm_ // d * n, _lcm_] for n, d in lst]

    @staticmethod
    def convertFracts_03(lst):
        """
        math.gcd, iteration
        """
        _, a = lst[0]
        for _, b in lst[1:]:
            a *= b // gcd(a, b)

        return [[a // d * n, a] for n, d in lst]


def sets_gen(convertFracts):
    import random
    test_sets = []
    for i in range(2, 100):
        lst = [[random.randint(1, 10), random.randint(1, 10)] for _ in range(i)]
        match = convertFracts(lst)
        test_sets.append((
            (lst,),
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