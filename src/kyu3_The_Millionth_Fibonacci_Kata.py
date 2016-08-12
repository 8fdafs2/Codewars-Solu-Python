class Solution():
    """
    https://www.codewars.com/kata/53d40c1e2f13e331fc000c26

    In this kata you will have to calculate fib(n) where:

    fib(0) := 0
    fib(1) := 1
    fin(n + 2) := fib(n + 1) + fib(n)

    Write an algorithm that can handle n where 1000000 ≤ n ≤ 1500000.

    Your algorithm must output the exact integer answer, to full precision.
    Also, it must correctly handle negative numbers as input.

    HINT I: Can you rearrange the equation
        fib(n + 2) = fib(n + 1) + fib(n) to find fib(n)
        if you already know fin(n + 1) and fib(n + 2)?
        Use this to reason what value fib has to have for negative values.
    HINT II: See http://mitpress.mit.edu/sicp/chapter1/node15.html
    """

    def __init__(self):
        pass

    def fib_01(self, n):
        """
        for-loop, intuitive
        """
        if n == 0:
            return 0
        if n > 0:
            fib1, fib2 = 0, 1
            for i in range(2, n + 1):
                fib1, fib2 = fib2, fib1 + fib2
            return fib2
        fib1, fib2 = 1, 0
        for i in range(2, 2 - n):
            fib1, fib2 = fib2, fib1 - fib2
        return fib2

    def fib_02(self, n):
        """
        for-loop, intuitive, symmetric negative side
        """
        if n == 0:
            return 0
        fib1, fib2 = 0, 1
        if n < 0:
            for i in range(2, 1 - n):
                fib1, fib2 = fib2, fib1 + fib2
            if n % 2 == 0:
                return -fib2
            return fib2
        for i in range(2, n + 1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2

    def fib_03(self, n):
        """
        recursion, matrix
        """
        if n == 0 or n == 1:
            return n
        # |fib(k+2)| = |1, 1| * |fib(k+1)|
        # |fib(k+1)|   |1, 0|   |fib(k)  |
        # |a, b| * |1, 1| = |a + b, a|
        # |c, d|   |1, 0|   |c + d, c|
        if n > 0:
            def recur(a, b, c, d, n):
                if n == 1:
                    return a, b, c, d
                if n % 2 == 0:
                    a, b, c, d = recur(a, b, c, d, n // 2)
                    b_c = b * c
                    return a * a + b_c, a * b + b * d, a * c + c * d, b_c + d * d
                a, b, c, d = recur(a, b, c, d, n - 1)
                return b, a + b, d, c + d

            return recur(0, 1, 1, 1, n - 1)[-1]

        def recur(a, b, c, d, n):
            if n == 1:
                return a, b, c, d
            if n % 2 == 0:
                a, b, c, d = recur(a, b, c, d, n // 2)
                b_c = b * c
                return a * a + b_c, a * b + b * d, a * c + c * d, b_c + d * d
            a, b, c, d = recur(a, b, c, d, n - 1)
            return b, a - b, d, c - d

        return recur(0, 1, 1, -1, -n)[1]

    def fib_04(self, n):
        """
        recursion, matrix, symmetric negative side
        """
        if n == 0 or n == 1:
            return n
        if n == -1:
            return 1
        # |fib(k+2)| = |1, 1| * |fib(k+1)|
        # |fib(k+1)|   |1, 0|   |fib(k)  |
        # |a, b| * |1, 1| = |a + b, a|
        # |c, d|   |1, 0|   |c + d, c|

        def recur(a, b, c, d, n):
            if n == 1:
                return a, b, c, d
            if n % 2 == 0:
                a, b, c, d = recur(a, b, c, d, n // 2)
                b_c = b * c
                return a * a + b_c, a * b + b * d, a * c + c * d, b_c + d * d
            a, b, c, d = recur(a, b, c, d, n - 1)
            return b, a + b, d, c + d

        if n < 0:
            if n % 2 == 0:
                return -recur(0, 1, 1, 1, -n - 1)[-1]
            return recur(0, 1, 1, 1, -n - 1)[-1]
        return recur(0, 1, 1, 1, n - 1)[-1]

    def fib_06(self, n):
        """
        recursion, https://mitpress.mit.edu/sicp/chapter1/node15.html, symmetric negative side
        """
        def recur(a, b, p, q, n):
            if n == 0:
                return b
            if n % 2 == 0:
                q_q = q * q
                return recur(a, b, p * p + q_q, 2 * p * q + q_q, n // 2)
            a_q = a * q
            return recur(b * q + a_q + a * p, b * p + a_q, p, q, n - 1)

        if n < 0:
            if n % 2 == 0:
                return -recur(1, 0, 0, 1, -n)
            return recur(1, 0, 0, 1, -n)
        return recur(1, 0, 0, 1, n)


def sets_gen(fib):
    test_sets = []
    for n in range(-1000, 1001, 3):
        match = fib(n)
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
    tf.test_spd(100, prt_docstr=True)
