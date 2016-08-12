from collections import defaultdict
from math import sqrt


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
    https://www.codewars.com/kata/sum-by-factors

    Given an array of positive or negative integers

    I= [i1,..,in]

    you have to produce a sorted array P of the form

    [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

    P will be sorted by increasing order of the prime numbers.
    The final result has to be given as a string in Java, C# or C++ and as an array of arrays in other languages.

    Example:

    I = [12, 15]
    result = [[2, 12], [3, 27], [5, 15]]
    [2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

    Notes: It can happen that a sum is 0 if some numbers are negative!

    Typescript return is the same as Javascript or Coffeescript return
    (Description doesn't accept reference to typescript...)

    Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result,
    the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.
    """

    def __init__(self):
        pass

    def sum_for_list_01(self, lst):
        """
        x /= p until x == 1
        """
        n = max(-min(lst), max(lst))
        _primes_ = primes(n)

        def prime_factors_of(x):
            if x < 0:
                x = -x
            ret = []
            for p in _primes_:
                if x % p == 0:
                    ret.append(p)
                    x //= p
                    while x % p == 0:
                        x //= p
                if x == 1:
                    if ret:
                        return ret
                    return [p, ]
            raise ValueError('invalid x')

        hashtab = {}
        for x in lst:
            for p in prime_factors_of(x):
                hashtab[p] = hashtab.get(p, 0) + x

        return [[key, value] for key, value in sorted(hashtab.items())]

    def sum_for_list_02(self, lst):
        """
        x /= p until x < p
        """
        n = max(-min(lst), max(lst))
        _primes_ = primes(n)

        def prime_factors_of(x):
            if x < 0:
                x = -x
            ret = []
            for p in _primes_:
                if p > x:
                    break
                if x % p == 0:
                    ret.append(p)

            return ret

        hashtab = {}
        for x in lst:
            for p in prime_factors_of(x):
                hashtab[p] = hashtab.get(p, 0) + x

        return [[key, value] for key, value in sorted(hashtab.items())]

    def sum_for_list_03(self, lst):
        """
        f in ps
        """
        n = max(-min(lst), max(lst))
        _primes_ = set(primes(n))

        def prime_factors_of(x):
            if x < 0:
                x = -x
            ret = []
            for i in range(2, x + 1):
                if x % i == 0 and i in _primes_:
                    ret.append(i)
            return ret

        hashtab = {}
        for x in lst:
            for p in prime_factors_of(x):
                hashtab[p] = hashtab.get(p, 0) + x

        return [[key, value] for key, value in sorted(hashtab.items())]

    def sum_for_list_04(self, lst):
        """
        f % f_all_rest != 0
        """
        # factors = {i for k in lst for i in range(2, abs(k) + 1) if k % i == 0}
        # prime_factors = {i for i in factors if not [j for j in factors - {i} if i % j == 0]}
        # return [[p, sum(e for e in lst if e % p == 0)] for p in sorted(prime_factors)]

        factors = set()
        for x in lst:
            for i in range(2, abs(x) + 1):
                if x % i == 0:
                    factors.add(i)

        prime_factors = set()
        for i in factors:
            for j in factors - {i}:
                if i % j == 0:
                    break
            else:
                prime_factors.add(i)

        return [[p, sum(x for x in lst if x % p == 0)] for p in sorted(prime_factors)]

    def sum_for_list_05(self, lst):
        """
        x /= f until x < f
        """
        hashtab = defaultdict(int)

        for x in lst:
            _x_ = x
            if x < 0:
                x = -x
            i = 2
            while i <= x:
                if x % i == 0:
                    hashtab[i] += _x_
                while x % i == 0:
                    x //= i
                if i == 2:
                    i = 3
                else:
                    i += 2

        return [[key, value] for key, value in sorted(hashtab.items())]


def sets_gen(sum_for_list):
    import random
    test_sets = []
    for i in range(3, 100):
        lst = [random.randint(2, 1000) * random.choice((1, -1)) for _ in range(i)]
        match = sum_for_list(lst)
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
    tf.test_spd(10, prt_docstr=True)
