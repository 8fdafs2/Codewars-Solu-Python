from math import log2, log, sqrt


def primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2, ]

    sieve = list(range(3, n + 1, 2))
    top = len(sieve)
    for m in range(3, int(sqrt(n + 1)) + 1, 2):
        if sieve[(m - 3) // 2] != 0:
            bot = (m * m - 3) // 2
            sieve[bot::m] = [0, ] * ((top - bot - 1) // m + 1)

    return [2, ] + list(filter(None, sieve))


class Solution():
    """
    https://www.codewars.com/kata/whats-a-perfect-power-anyway

    A perfect power is a classification of positive integers:

    In mathematics,
    a perfect power is a positive integer that can be expressed as an integer power of another positive integer.
    More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.
    Your task is to check whether a given integer is a perfect power.
    If it is a perfect power, return a pair m and k with mk = n as a proof.
    Otherwise return Nothing, Nil, null, None or your language's equivalent.

    Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2,
    so (3,4) and (9,2) are valid solutions. However, the tests take care of this,
    so if a number is a perfect power, return any pair that proves it.

    Examples

    isPP(4) => [2,2]
    isPP(9) => [3,2]
    isPP(5) => None
    """

    def __init__(self):
        pass

    def isPP_01(self, n):
        """
        loop d, d-bound, k-bound, k = 2, 3, 4, 5, 6, ...
        """
        d_max = int(sqrt(n))
        k_max = int(log2(n))
        # k = 2, 3, 4, 5, 6, ...
        for d in range(2, d_max + 1):
            d_d = d * d
            if n % d_d == 0:
                _n_ = n
                _n_ //= d_d
                if _n_ == 1:
                    return [d, 2]
                for k in range(3, k_max + 1):
                    if _n_ % d != 0:
                        break
                    _n_ //= d
                    if _n_ == 1:
                        return [d, k]

    def isPP_02(self, n):
        """
        loop d, d-bound, k = 2, 3, 4, 5, 6, ...
        """
        d_max = int(sqrt(n))
        # k = 2, 3, 4, 5, 6, ...
        for d in range(2, d_max + 1):
            d_d = d * d
            if n % d_d == 0:
                _n_ = n
                _n_ //= d_d
                if _n_ == 1:
                    return [d, 2]
                k = 3
                while _n_ != 0:
                    if _n_ % d != 0:
                        break
                    _n_ //= d
                    if _n_ == 1:
                        return [d, k]
                    k += 1

    def isPP_03(self, n):
        """
        loop d, d-bound, k-bound, k = 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, ...
        """
        d_max = int(sqrt(n))
        k_max = int(log2(n))
        # k = 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, ...
        for d in range(2, d_max + 1):
            d_d = d * d
            if n % d_d == 0:
                _n_ = n
                _n_ //= d_d
                if _n_ == 1:
                    return [d, 2]
                if _n_ % d != 0:
                    continue
                _n_ //= d
                if _n_ == 1:
                    return [d, 3]
                for k in range(5, k_max + 1, 2):
                    if _n_ % d_d != 0:
                        break
                    _n_ //= d_d
                    if _n_ == 1:
                        return [d, k]

    def isPP_04(self, n):
        """
        loop d, d-bound, k = 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, ...
        """
        # k = 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, ...
        d_max = int(sqrt(n))
        for d in range(2, d_max + 1):
            d_d = d * d
            if n % d_d == 0:
                _n_ = n
                _n_ //= d_d
                if _n_ == 1:
                    return [d, 2]
                if _n_ % d != 0:
                    continue
                _n_ //= d
                if _n_ == 1:
                    return [d, 3]
                k = 5
                while _n_ != 0:
                    if _n_ % d_d != 0:
                        break
                    _n_ //= d_d
                    if _n_ == 1:
                        return [d, k]
                    k += 2

    def isPP_05(self, n):
        """
        loop d, d-bound, k = 2, 3, 5, 7
        """
        d_max = int(sqrt(n))
        _primes_ = [2, 3, 5, 7]
        for d in range(2, d_max + 1):
            d_d = d * d
            if n % d_d == 0:
                for k in _primes_:
                    _n_ = d ** k
                    if _n_ == n:
                        return [d, k]
                    if _n_ > n:
                        break

    def isPP_06(self, n):
        """
        loop d, d-bound, k-bound, k = prime
        """
        d_max = int(sqrt(n))
        k_max = int(log2(n))
        _primes_ = primes(k_max)
        for d in range(2, d_max + 1):
            if n % d == 0:
                for k in _primes_:
                    if d ** k == n:
                        return [d, k]

    def isPP_07(self, n):
        """
        loop d, d-bound, k = log(n, d)
        """
        d_max = int(sqrt(n))
        for d in range(2, d_max + 1):
            k = int(round(log(n, d)))
            if d ** k == n:
                return [d, k]

    def isPP_08(self, n):
        """
        loop k, k-bound, d = n ** (1 / k)
        """
        k_max = int(log2(n))
        for k in range(2, k_max + 1):
            d = int(round(n ** (1 / k)))
            if d ** k == n:
                return [d, k]

    def isPP_09(self, n):
        """
        loop k, d = n ** (1 / k), is_integer
        """
        d = 2
        k = 2
        while d >= 2:
            d = round(n ** (1 / k), 4)
            if d.is_integer():
                return [int(d), k]
            k += 1


def cmpr(to_match, test_set):
    args, match = test_set
    n, = args
    if to_match is not None:
        d, k = to_match
        return d ** k == n
    return match is None


def sets_gen(isPP):
    test_sets = []
    for n in range(2, 1000):
        match = isPP(n)
        test_sets.append((
            (n,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    # print(sol.isPP_01_(36))
    #
    # exit()

    tf = Test_Fixture(sol, sets_gen, cmpr)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
