import sys
from math import sqrt
from random import randint, sample, randrange


class Solution():
    """
    """

    def __init__(self):
        pass

    @staticmethod
    def is_prime_01(n):
        """
        """
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_prime_02(n):
        """
        Fermat's litte theorem.
        """
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for _ in range(7):
            if pow(randint(1, n - 1), n - 1, n) != 1:
                return False
        return True

    @staticmethod
    def is_prime_03(n, k=7):
        """
        Rabin-Miller
        """
        if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
            return [False, False, True, True, False, True][n]
        elif n & 1 == 0:  # should be faster than n % 2
            return False
        else:
            s, d = 0, n - 1
            while d & 1 == 0:
                s, d = s + 1, d >> 1
            # Use random.randint(2, n-2) for very large numbers
            # for a in [random.randint(2, n - 2) for _ in range(k)]:
            for a in sample(range(2, min(n - 2, sys.maxsize)), min(n - 4, k)):
                x = pow(a, d, n)
                if x != 1 and x + 1 != n:
                    for r in range(1, s):
                        x = pow(x, 2, n)
                        if x == 1:
                            return False  # composite for sure
                        elif x == n - 1:
                            a = 0  # so we know loop didn't continue to end
                            break  # could be strong liar, try another a
                    if a != 0:
                        return False  # composite if we reached end of this loop
            return True  # probably prime if reached end of outer loop

    @staticmethod
    def is_prime_04(n, _mrpt_num_trials=5):
        """
        Miller-Rabin, rosetta, probably correct answers
        """
        # This versions will give answers with a very small probability of being false.
        # That probability being dependent on _mrpt_num_trials and
        # the random numbers used for name a passed to function try_composite.
        assert n >= 2
        # special case 2
        if n == 2:
            return True
        # ensure n is odd
        if n % 2 == 0:
            return False
        # write n-1 as 2**s * d
        # repeatedly try to divide n-1 by 2
        s = 0
        d = n - 1
        while True:
            quotient, remainder = divmod(d, 2)
            if remainder == 1:
                break
            s += 1
            d = quotient
        assert (2 ** s * d == n - 1)

        # test the base a to see whether it is a witness for the compositeness of n
        def try_composite(a):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2 ** i * d, n) == n - 1:
                    return False
            return True  # n is definitely composite

        for i in range(_mrpt_num_trials):
            a = randrange(2, n)
            if try_composite(a):
                return False

        return True  # no base tested showed n as composite

    @staticmethod
    def is_prime_05(n, _precision_for_huge_n=16):
        """
        Miller-Rabin, rosetta, give correct answers for n less than 341550071728321
        """

        # This versions will give correct answers for n less than 341550071728321 and then
        # reverting to the probabilistic form of the first solution.
        # By selecting predetermined values for the a values to use instead of random values,
        # the results can be shown to be deterministically correct below certain thresholds.
        # For 341550071728321 and beyond,
        # I have followed the pattern in choosing a from the set of prime numbers.
        # While this uses the best sets known in 1993,
        # there are better sets known, and at most 7 are needed for 64-bit numbers.

        if n in _known_primes or n in (0, 1):
            return True
        if any((n % p) == 0 for p in _known_primes):
            return False
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1

        def _try_composite(a, d, n, s):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2 ** i * d, n) == n - 1:
                    return False
            return True  # n  is definitely composite

        # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
        if n < 1373653:
            return not any(_try_composite(a, d, n, s) for a in (2, 3))
        if n < 25326001:
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
        if n < 118670087467:
            if n == 3215031751:
                return False
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
        if n < 2152302898747:
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
        if n < 3474749660383:
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
        if n < 341550071728321:
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
        # otherwise
        return not any(_try_composite(a, d, n, s)
                       for a in _known_primes[:_precision_for_huge_n])


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if Solution.is_prime_05(x)]


def sets_gen(is_prime):
    test_sets = []
    for n in range(2, 100000):
        match = is_prime(n)
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
    tf.test_spd(2, prt_docstr=True)
