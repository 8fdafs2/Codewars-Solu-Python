from math import log


class Solution():
    """
    https://www.codewars.com/kata/highest-number-with-two-prime-factors

    The numbers 6, 12, 18, 24, 36, 48 have a common property.
    They have the same two prime factors that are 2 and 3.

    If we see their prime factorization we will see it more clearly:

        6 = 2 * 3
        12 = 2^2 * 3
        18 = 2 * 3^2
        24 = 2^3 * 3
        36 = 2^2 * 3^2
        48 = 2^4 * 3

    48 is the maximum of them bellow the value 50

    We may see another cases,
    for numbers that have another two prime factors like: 5, 11, but bellow (or equal) a maximum value 1000

        55 = 5 * 11
        275 = 5^2 * 11
        605 = 5 * 11^2

    In this case 605 is the highest possible number bellow 1000.

    Make the function highest_biPrimefac(),
    that receives two primes as arguments and a maximum limit, nMax (found numbers should be less or equal to nMax).
    The function should output a list with three elements in this order:
    highest found number, the exponent corresponding to the smaller prime and the exponent for the biggest prime.

    Representing the features for this function:

        highest_biPrimefac(p1, p2, nMax) -------> [max.number, k1, k2]
        max.number = p1^k1 * p2^k2 <= nMax
        p1 < p2 and k1 >= 1, k2 >= 1

    Let's see the cases we have above:

        highest_biPrimefac(2, 3, 50) ------> [48, 4, 1]
        highest_biPrime(5, 11, 1000) ------> [605, 1, 2]

    Enjoy it and happy coding!
    """

    def __init__(self):
        pass

    @staticmethod
    def highest_biPrimefac_01(p1, p2, n):  # p1, p2 primes and p1 < p2
        """
        brute force
        """
        e1 = int(log(n, p1))
        e2 = int(log(n, p2))

        rets = []
        for _e1_ in range(1, e1 + 1):
            for _e2_ in range(1, e2 + 1):
                rets.append([p1 ** _e1_ * p2 ** _e2_, _e1_, _e2_])

        rets.sort(reverse=True)
        for ret in rets:
            if ret[0] <= n:
                return ret

    @staticmethod
    def highest_biPrimefac_02(p1, p2, n):  # p1, p2 primes and p1 < p2
        """
        brute force
        """
        _n_ = n
        e1 = 0
        while _n_ >= p1:
            _n_ //= p1
            e1 += 1

        _n_ = n
        e2 = 0
        while _n_ >= p2:
            _n_ //= p2
            e2 += 1

        rets = []

        p1_e1 = 1
        for _e1_ in range(1, e1 + 1):
            p1_e1 *= p1
            p2_e2 = 1
            for _e2_ in range(1, e2 + 1):
                p2_e2 *= p2
                ret = p1_e1 * p2_e2
                if ret <= n:
                    rets.append([ret, _e1_, _e2_])
        if rets:
            return max(rets)

    @staticmethod
    def highest_biPrimefac_03(p1, p2, n):
        """
        prime factor
        """

        def prime_fac(n):
            hashtab = {}
            p = 2
            while p <= n:
                if n % p == 0:
                    n //= p
                    e = 1
                    while n % p == 0:
                        n //= p
                        e += 1
                    hashtab[p] = e
                if p == 2:
                    p = 3
                else:
                    p += 2
            return hashtab

        for n in range(n, 0, -1):
            if n % p1 == n % p2 == 0:
                fac = prime_fac(n)
                if len(fac) == 2:
                    return [n, fac[p1], fac[p2]]


def sets_gen(highest_biPrimefac):
    import random
    primes = [2, 3, 5, 7, 11]
    test_sets = []
    for n in range(1000, 5001):
        p1, p2 = random.sample(primes, 2)
        if p1 > p2:
            p1, p2 = p2, p1
        match = highest_biPrimefac(p1, p2, n)
        test_sets.append((
            (p1, p2, n),
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
