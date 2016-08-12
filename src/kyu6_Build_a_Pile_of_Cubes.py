import math


class Solution():
    """
    https://www.codewars.com/kata/5592e3bd57b64d00f3000047

    Your task is to construct a building which will be a pile of n cubes.
    The cube at the bottom will have a volume of n^3,
    the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

    You are given the total volume m of the building.
    Being given m can you find the number n of cubes you will have to build?

    The parameter of the function findNb (find_nb, find-nb) will be an integer m and
    you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m
    if such a n exists or -1 if there is no such n.

    Examples:

        findNb(1071225) --> 45
        findNb(91716553919377) --> -1
    """
    def __init__(self):
        pass

    def find_nb_01(self, m):
        """
        brute force
        """
        s = 1
        i = 1
        while s < m:
            i += 1
            s += i * i * i
        if s == m:
            return i
        return -1

    def find_nb_02(self, m):
        """
        solve n: n^2 + n - 2*sqrt(Sn) = 0
        """
        # (n(n+1)/2)^2 = Sn
        # n^2 + n - 2*sqrt(Sn) = 0
        # a = 1; b = 1; c = -2*sqrt(Sn)
        n = int(-1 + math.sqrt(1 + 8 * math.sqrt(m))) >> 1
        if ((n * (n + 1)) >> 1) ** 2 == m:
            return n
        return -1

    def find_nb_03(self, m):
        """
        solve n: n(n+1) = 2*sqrt(Sn)
        """
        # (n(n+1)/2)^2 = Sn
        # n(n+1) = 2*sqrt(Sn)
        n = int(math.sqrt(2 * math.sqrt(m)))
        if ((n * (n + 1)) >> 1) ** 2 == m:
            return n
        return -1


def sets_gen(find_nb):
    import random
    test_sets = []
    for i in range(1000):
        m = random.randint(1, 100000000000)
        match = find_nb(m)
        test_sets.append((
            (m,),
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
