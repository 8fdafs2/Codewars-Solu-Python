from collections import deque
import decimal
import numpy as np
from functools import reduce
from itertools import product

context = decimal.getcontext()
context.prec = 24
one = decimal.Decimal(1)
dot_five = decimal.Decimal(0.5)
sqrt_five = decimal.Decimal(5).sqrt()

portion_00 = (one / sqrt_five)
portion_01 = ((one + sqrt_five) * dot_five)
portion_02 = ((one - sqrt_five) * dot_five)


class Solution():
    """
    https://www.codewars.com/kata/529adbf7533b761c560004e5

    The Fibonacci sequence is traditionally used to explain tree recursion.

    def fibonacci(n):
        if n in [0, 1]:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    This algorithm serves welll its educative purpose but it's tremendously inefficient,
    not only because of recursion, but because we invoke the fibonacci function twice,
    and the right branch of recursion (i.e. fibonacci(n-2))
    recalculates all the Fibonacci numbers already calculated by
    the left branch (i.e. fibonacci(n-1)).
    This algorithm is so inefficient that the time to calculate
    any Fibonacci number over 50 is simply too much.
    You may go for a cup of coffee or go take a nap while you wait for the answer.
    But if you try it here in Code Wars you will most likely get a code timeout before any answers.

    For this particular Kata we want to implement the memoization solution.
    This will be cool because it will let us keep using the tree recursion algorithm
    while still keeping it sufficiently optimized to get an answer very rapidly.

    The trick of the memoized version is that we will keep a cache data structure
    (most likely an associative array) where we will store
    the Fibonacci numbers as we calculate them.
    When a Fibonacci number is calculated, we first look it up in the cache,
    if it's not there, we calculate it and put it in the cache,
    otherwise we returned the cached number.

    Refactor the function into a recursive Fibonacci function
    that using a memoized data structure avoids the deficiencies of tree recursion
    Can you make it so the memoization cache is private to this function?
    """

    def __init__(self):
        pass

    def fibonacci_01(self, n):
        """
        recursion, hashtab to memorize
        """
        hashtab = {0: 0, 1: 1}

        def recur(n):
            if n in hashtab:
                return hashtab[n]
            hashtab[n] = recur(n - 1) + hashtab[n - 2]
            return hashtab[n]

        return recur(n)

    def fibonacci_02(self, n):
        """
        recursion, list to memorize
        """
        cache = [0, 1]

        def recur(n):
            if n < len(cache):
                return cache[n]
            cache.append(recur(n - 1) + cache[n - 2])
            return cache[n]

        return recur(n)

    def fibonacci_03(self, n):
        """
        for-loop, list to memorize
        """
        cache = [0, 1]

        for i in range(2, n + 1):
            cache.append(cache[i - 1] + cache[i - 2])

        return cache[n]

    def fibonacci_04(self, n):
        """
        recursion, counter
        """

        def recur(n, fib1, fib2):
            if n == 0:
                return fib1
            return recur(n - 1, fib2, fib1 + fib2)

        return recur(n, 0, 1)

    def fibonacci_05(self, n):
        """
        recursion, hashtab to memorize, wrapper
        """

        def memoized(f):
            hashtab = {0: 0, 1: 1}

            def wrapped(n):
                fib_n = hashtab.get(n)
                if fib_n is None:
                    fib_n = hashtab[n] = f(n)
                return fib_n

            return wrapped

        @memoized
        def recur(n):
            return recur(n - 1) + recur(n - 2)

        return recur(n)

    def fibonacci_06(self, n):
        """
        for-loop, deque to memorize
        """
        if n == 0:
            return 0

        cache = deque([0, 1])

        for i in range(2, n + 1):
            cache.append(cache[1] + cache[0])
            cache.popleft()

        return cache[-1]

    def fibonacci_07(self, n):
        """
        for-loop, intuitive
        """
        if n == 0:
            return 0

        fib1, fib2 = 0, 1
        for i in range(2, n + 1):
            fib1, fib2 = fib2, fib1 + fib2

        return fib2

    def fibonacci_08(self, n):
        """
        for-loop, matrix multiplication
        """
        if n == 0:
            return 0
        # |fib(k+2)| = |1, 1| * |fib(k+1)|
        # |fib(k+1)|   |1, 0|   |fib(k)  |
        # |a, b| * |1, 1| = |a + b, a|
        # |c, d|   |1, 0|   |c + d, c|
        a, b, c, d = 0, 1, 1, 1
        for i in range(n - 2):
            # a, b, c, d = b, a + b, d, c + d
            a, b = b, a + b
            c, d = d, c + d

        return d

    def fibonacci_09(self, n):
        """
        recursion, matrix multiplication, reduced by even
        """
        if n == 0 or n == 1:
            return n

        def recur(a, b, c, d, n):
            if n == 1:
                return a, b, c, d
            if n % 2 == 0:
                a, b, c, d = recur(a, b, c, d, n // 2)
                return a * a + b * c, a * b + b * d, a * c + c * d, b * c + d * d
            a, b, c, d = recur(a, b, c, d, n - 1)
            return b, a + b, d, c + d

        return recur(0, 1, 1, 1, n - 1)[-1]

    def fibonacci_10(self, n):
        """
        recursion, https://mitpress.mit.edu/sicp/chapter1/node15.html
        """

        def recur(a, b, p, q, n):
            if n == 0:
                return b
            if n % 2 == 0:
                q_q = q * q
                return recur(a, b, p * p + q_q, 2 * p * q + q_q, n // 2)
            a_q = a * q
            return recur(b * q + a_q + a * p, b * p + a_q, p, q, n - 1)

        return recur(1, 0, 0, 1, n)

    def fibonacci_11(self, n):
        """
        matrix, numpy.linalg.matrix_power
        """
        # if n >= 0:
        #     return (np.matrix([[0, 1], [1, 1]], object) ** n)[0, 1]
        #
        # return (np.matrix([[-1, 1], [1, 0]], object) ** -n)[0, 1]

        if n >= 0:
            return np.linalg.matrix_power(np.array([[0, 1], [1, 1]], object), n)[0, 1]

        return np.linalg.matrix_power(np.array([[-1, 1], [1, 0]], object), -n)[0, 1]

    def fibonacci_12(self, n):
        """
        recursion, fib(n) = fib(k)*fib(n-k+1) + fib(k-1)*fib(n-k)
        """

        # Solution based on relation:
        # fib(n) =   fib(n-1) +   fib(n-2)
        # fib(n) = 2*fib(n-2) +   fib(n-3)
        # fib(n) = 3*fib(n-3) + 2*fib(n-4)
        # fib(n) = 5*fib(n-4) + 3*fib(n-5)
        # fib(n) = 8*fib(n-5) + 5*fib(n-6)
        #        ...
        # fib(n) = fib(k)*fib(n-k+1) + fib(k-1)*fib(n-k)

        # F(2n-1) = F(n) x F(n) + F(n-1) x F(n-1)
        # F(2n) = (2F(n-1) + F(n)) x F(n)
        def recur(n):
            if n in (0, 1):
                return n

            k = n // 2
            f0 = recur(k)
            f1 = recur(k - 1)
            if n % 2 == 0:
                # f0 * f0 + 2 * f0 * f1
                return f0 * (f0 + f1 + f1)
            f0_f1 = f0 + f1
            return f0 * f0 + f0_f1 * f0_f1
            # 2 * f0 * f0 + 2 * f0 * f1 + f1 * f1
            # f0 ** 2 + (f0 + f1) ** 2

        return recur(n)

    def fibonacci_13(self, n):
        """
        analytic function, decimal
        """
        n = decimal.Decimal(n)

        return (portion_00 * (context.power(portion_01, n) - context.power(portion_02, n))).
        to_integral_value()

    def fibonacci_14(self, n):
        """
        lucas numbers
        """
        if n == 0:
            return 0

        def lucas(n):
            if n == 1:
                return 1, 1
            l, f = lucas(n >> 1)
            l, f = (l * l + 5 * f * f) >> 1, l * f

            if n & 1:
                return (l + 5 * f) >> 1, (l + f) >> 1
            return l, f

        if n & 1:
            return lucas(n)[1]
        # return reduce(int.__mul__, lucas(n >> 1))
        # return reduce(lambda l, f: l * f, lucas(n // 2))
        # fib = 1
        # for i in lucas(n >> 1):
        #     fib *= i
        # return fib
        l, f = lucas(n >> 1)
        return l * f


def sets_gen(fibonacci):
    test_sets = []
    for n in range(1, 100):
        match = fibonacci(n)
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
    tf.test_spd(50, prt_docstr=True)
