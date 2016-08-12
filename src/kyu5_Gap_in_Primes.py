from math import sqrt
from random import randint
import bisect


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
    https://www.codewars.com/kata/gap-in-primes

    The prime numbers are not regularly spaced.
    For example from 2 to 3 the gap is 1.
    From 3 to 5 the gap is 2.
    From 7 to 11 it is 4.
    Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

    A prime gap of length n is a run of n-1 consecutive composite numbers between
    two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

    We will write a function gap with parameters:

    g (integer >= 2) which indicates the gap we are looking for

    m (integer >= 2) which gives the start of the search (m inclusive)

    n (integer >= m) which gives the end of the search (n inclusive)

    In the example above gap(2, 2, 50) will return [3, 5] which is the first pair between 2 and 50 with a 2-gap.

    So this function should return the first pair of two prime numbers spaced with a gap of g between
    the limits m, n if these numbers exist otherwise nil or null or None or Nothing (depending on the language).

    Examples:

        gap(2, 5, 7) --> [5, 7]

        gap(2, 5, 5) --> nil

        gap(4, 130, 200) --> [163, 167]

        ([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)

        gap(6,100,110) --> nil : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because
        there is 103in between and 103-109is not a 6-gap because there is 107in between.

    Ref:

        https://en.wikipedia.org/wiki/Prime_gap
    """

    def __init__(self):
        pass

    @staticmethod
    def gap_01(g, m, n):
        """
        prime test
        """

        def is_prime(n):
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True

        p_last = None
        m |= 1
        for p in range(m, n + 1, 2):
            if is_prime(p):
                if p_last and p - p_last == g:
                    return [p_last, p]
                p_last = p

    @staticmethod
    def gap_02(g, m, n):
        """
        prime series generation, full, sieves, backwards search
        """
        _primes_ = primes(n)
        j = None
        for i in range(len(_primes_) - 1, -1, -1):
            if _primes_[i - 1] < m:
                if j:
                    return [_primes_[j - 1], _primes_[j]]
                return
            if _primes_[i] - _primes_[i - 1] == g:
                j = i

    @staticmethod
    def gap_03(g, m, n):
        """
        prime series generation, full, sieves, bisect
        """
        _primes_ = primes(n)
        _len_primes_ = len(_primes_)
        i_start = bisect.bisect_left(_primes_, m, 0, _len_primes_)

        for i in range(i_start, _len_primes_ - 1):
            if _primes_[i + 1] - _primes_[i] == g:
                return [_primes_[i], _primes_[i + 1]]

    @staticmethod
    def gap_04(g, m, n):
        """
        prime series generation, full, sieves, bisect local
        """
        _primes_ = primes(n)
        lo = 0
        hi = _len_primes_ = len(_primes_)

        while lo < hi:
            mid = (lo + hi) // 2
            midvar = _primes_[mid]
            if midvar < m:
                lo = mid + 1
            else:
                hi = mid

        for i in range(hi, _len_primes_ - 1):
            if _primes_[i + 1] - _primes_[i] == g:
                return [_primes_[i], _primes_[i + 1]]


    @staticmethod
    def gap_05(g, m, n):
        """
        prime series generation, sieves
        """
        m |= 1
        _primes_ = primes(m)
        for _p_ in range(m + 2, n + 1, 2):
            mroot = int(sqrt(_p_))
            for p in _primes_:
                if p <= mroot and _p_ % p == 0:
                    break
            else:
                if _primes_[-1] >= m and _p_ - _primes_[-1] == g:
                    return [_primes_[-1], _p_]
                _primes_.append(_p_)

    @staticmethod
    def gap_06(g, m, n):
        """
        prime test, unreliable
        """

        def is_prime(n):
            """
            Fermat's little theorem.
            """
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for _ in range(7):
                if pow(randint(1, n - 1), n - 1, n) != 1:
                    return False
            return True

        p_last = None
        m |= 1
        for p in range(m, n + 1, 2):
            if is_prime(p):
                if p_last and p - p_last == g:
                    return [p_last, p]
                p_last = p


def sets_gen(gap):
    import random
    test_sets = []

    for i in range(1000):
        g = random.choice((2, 4, 6, 8, 10, 12))
        m = random.randint(1000, 2000)
        n = random.randint(m + 10, (m + 10) * 10)
        match = gap(g, m, n)
        test_sets.append((
            (g, m, n),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(5, prt_docstr=True)
