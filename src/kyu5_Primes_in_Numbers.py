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
    https://www.codewars.com/kata/primes-in-numbers

    Given a positive number n > 0 (Javascript n >= 0) find the prime factor decomposition of n.
    The result will be a string with the following form :

     "(p1**n1)(p2**n2)...(pk**nk)"
    with the p(i) in increasing order and n(i) empty if n(i) is 1.

    Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
    """

    def __init__(self):
        pass

    def primeFactors_01(self, n):
        """
        """
        _primes_ = primes(n)

        ret = ''
        for p in _primes_:
            if n % p == 0:
                n //= p
                e = 1
                while n % p == 0:
                    n //= p
                    e += 1
                if e == 1:
                    ret += '({})'.format(p)
                else:
                    ret += '({}**{})'.format(p, e)
            if n == 1:
                return ret

    def primeFactors_02(self, n):
        """
        """
        ret = ''
        i = 2
        while i <= n:
            if n % i == 0:
                n //= i
                e = 1
                while n % i == 0:
                    n //= i
                    e += 1
                if e == 1:
                    ret += '({})'.format(i)
                else:
                    ret += '({}**{})'.format(i, e)

            if i == 2:
                i = 3
            else:
                i += 2

        return ret

    def primeFactors_03(self, n):
        """
        """
        e = 0
        while n % 2 == 0:
            e += 1
            n //= 2
        if e == 1:
            ret = '({})'.format(2)
        elif e > 1:
            ret = '({}**{})'.format(2, e)
        else:
            ret = ''

        for m in range(3, n + 1, 2):
            e = 0
            while n % m == 0:
                e += 1
                n //= m
            if e == 1:
                ret += '({})'.format(m)
            elif e > 1:
                ret += '({}**{})'.format(m, e)
            if n == 1:
                break

        return ret


def sets_gen(primeFactors):
    test_sets = []
    for n in range(2, 1001):
        match = primeFactors(n)
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
