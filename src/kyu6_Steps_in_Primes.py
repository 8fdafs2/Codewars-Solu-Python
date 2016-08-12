import bisect
from math import sqrt
from random import randint


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
    https://www.codewars.com/kata/steps-in-primes

    The prime numbers are not regularly spaced.
    For example from 2 to 3 the step is 1. From 3 to 5 the step is 2. From 7 to 11 it is 4.
    Between 2 and 50 we have the following pairs of 2-steps primes:

    3, 5 - 5, 7, - 11, 13, - 17, 19, - 29, 31, - 41, 43

    We will write a function step with parameters:

    g (integer >= 2) which indicates the step we are looking for,

    m (integer >= 2) which gives the start of the search (m inclusive),

    n (integer >= m) which gives the end of the search (n inclusive)

    In the example above step(2, 2, 50) will return [3, 5] which is the first pair between 2 and 50 with a 2-steps.

    So this function should return the first pair of the two prime numbers spaced with
    a step of g between the limits m, n if these g-steps prime numbers exist otherwise
    nil or null or None or Nothing (depending on the language).

    Examples:

    step(2, 5, 7) --> [5, 7]

    step(2, 5, 5) --> nil

    step(4, 130, 200) --> [163, 167]

    ([193, 197] is also such a 2-steps primes between 130 and 200 but it's not the first pair).

    step(6, 100, 110) --> [101, 107] though there is a prime between 101 and 107: 103; the pair 101-103 is a 2-step.

    Note:

    The idea of "step" is close to that of "gap" but it is not exactly the same.
    For those interested they can have a look at http://mathworld.wolfram.com/PrimeGaps.html.
    A "gap" is more restrictive:
    there must be no primes in between (101-107 is a "step" but not a "gap". Next kata will be about "gaps":-).
    """

    def __init__(self):
        pass

    @staticmethod
    def step_01(g, m, n):
        """
        prime test
        """
        if g % 2 == 1:
            return

        def is_prime(n):
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True

        m |= 1
        for p in range(m, n + 1, 2):
            if is_prime(p):
                if is_prime(p + g):
                    return [p, p + g]

    @staticmethod
    def step_02(g, m, n):
        """
        prime test, cache
        """
        if g % 2 == 1:
            return

        hashtab = {}

        def is_prime(n):
            if n in hashtab:
                return hashtab[n]
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    hashtab[n] = False
                    return False
            hashtab[n] = True
            return True

        m |= 1
        for p in range(m, n + 1, 2):
            if is_prime(p):
                if is_prime(p + g):
                    return [p, p + g]

    @staticmethod
    def step_03(g, m, n):
        """
        prime series generation, full, sieves, bisect
        """
        _primes_ = primes(n)
        _len_primes_ = len(_primes_)
        i_start = bisect.bisect_left(_primes_, m, 0, _len_primes_)

        for i in range(i_start, _len_primes_ - 1):

            # j = i + 1
            # step = _primes_[j] - _primes_[i]
            # while step < g:
            #     j += 1
            #     if j == _len_primes_:
            #         return
            #     step = _primes_[j] - _primes_[i]
            # if step == g:
            #     return [_primes_[i], _primes_[j]]

            for j in range(i + 1, _len_primes_):
                step = _primes_[j] - _primes_[i]
                if step == g:
                    return [_primes_[i], _primes_[j]]
                if step > g:
                    break

    @staticmethod
    def step_04(g, m, n):
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
            for j in range(i + 1, _len_primes_):
                step = _primes_[j] - _primes_[i]
                if step == g:
                    return [_primes_[i], _primes_[j]]
                if step > g:
                    break

    @staticmethod
    def step_05(g, m, n):
        """
        prime series generation, sieves
        """
        m |= 1
        _primes_ = primes(m - 2)
        i_start = _len_primes_minus_one_ = len(_primes_)

        for _p_ in range(m, n + 1, 2):
            mroot = int(sqrt(_p_))
            for p in _primes_:
                if p <= mroot and _p_ % p == 0:
                    break
            else:
                _primes_.append(_p_)
                break

        for _p_ in range(_p_ + 2, n + 1, 2):
            mroot = int(sqrt(_p_))
            for p in _primes_:
                if p <= mroot and _p_ % p == 0:
                    break
            else:
                step = _p_ - _primes_[i_start]
                while step > g and i_start < _len_primes_minus_one_:
                    i_start += 1
                    step = _p_ - _primes_[i_start]
                if step == g:
                    return [_primes_[i_start], _p_]
                _len_primes_minus_one_ += 1
                _primes_.append(_p_)

    @staticmethod
    def step_06(g, m, n):
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

        m |= 1
        for p in range(m, n + 1, 2):
            if is_prime(p):
                if is_prime(p + g):
                    return [p, p + g]


def sets_gen(step):
    import random
    test_sets = []

    for i in range(1000):
        g = random.choice((2, 4, 6, 8, 10, 12))
        m = random.randint(1000, 2000)
        n = random.randint(m + 10, (m + 10) * 10)
        match = step(g, m, n)
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
