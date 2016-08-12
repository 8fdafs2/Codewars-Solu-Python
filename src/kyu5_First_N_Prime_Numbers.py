from math import sqrt


class _Primes_(list):
    def __init__(self):
        super().__init__([2, 3])
        # super(Primes_, self).__init__([2, 3])

    def last(self, n):
        return self[-n:]


_primes_ = _Primes_()


class Primes_01:

    @staticmethod
    def first(n):

        if n <= len(_primes_):
            return _primes_[:n]

        m = _primes_[-1] + 2

        while n - len(_primes_) > 0:
            mroot = int(sqrt(m))
            for p in _primes_:
                if p > mroot:
                    _primes_.append(m)
                    break
                if m % p == 0:  # not-a-prime-number
                    break
            else:
                _primes_.append(m)
            m += 2

        return _primes_


class Solution():
    """
    https://www.codewars.com/kata/first-n-prime-numbers

    A prime number is an integer greater than 1 that is only evenly divisible by itself and 1.

    Write your own Primes class with class method Primes.first(n) that returns an array of the first n prime numbers.

    For example:

    Primes.first(1)
    # => [2]

    Primes.first(2)
    # => [2, 3]

    Primes.first(5)
    # => [2, 3, 5, 7, 11]

    Primes.first(20).last(5)
    # => [53, 59, 61, 67, 71]
    Note: An inefficient algorithm will time out. Memoization may help.

    More info on primes here (http://en.wikipedia.org/wiki/Prime_number).
    """

    def __init__(self):
        pass

    def subsol_01(self, n, m):
        """
        """
        return Primes_01.first(n).last(m)


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsol_01(10, 3))
