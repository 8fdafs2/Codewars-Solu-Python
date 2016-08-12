import math


class Solution():
    """
    https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

    Write a program that will calculate the number of trailing zeros in a factorial of a given number.

    N! = 1 * 2 * 3 * 4 ... N

    zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600
    that has 2 trailing zeros 4790016(00)

    Be careful 1000! has length of 2568 digital numbers.
    """

    def __init__(self):
        pass

    def zeros_01(self, n):
        """
        div by 5
        """
        ret = 0
        n //= 5
        while n > 0:
            ret += n
            n //= 5
        return ret

    def zeros_02(self, n):
        """
        div by 5, recursion
        """

        def recur(n):
            if n < 5:
                return 0
            n //= 5
            return n + recur(n)

        return recur(n)

    def zeros_03(self, n):
        """
        brute-force, str
        """
        # def fac(n):
        #     if n == 0:
        #         return 1
        #     else:
        #         return fac(n-1) * n
        # n_fac = fac(n)
        n_fac = str(math.factorial(n))
        return len(n_fac) - len(n_fac.rstrip('0'))

    def zeros_04(self, n):
        """
        brute-force, divmod
        """
        # def fac(n):
        #     if n == 0:
        #         return 1
        #     else:
        #         return fac(n-1) * n
        # def fac(n):
        #     ret = 1
        #     while n:
        #         ret *= n
        #         n -= 1
        #     return ret
        # n_fac = fac(n)
        n_fac = math.factorial(n)
        ret = 0
        n_fac, rem = divmod(n_fac, 10)
        while rem == 0:
            ret += 1
            n_fac, rem = divmod(n_fac, 10)
        return ret


def sets_gen(zeros):
    import random
    test_sets = []
    for _ in range(5000):
        n = random.randint(0, 1001)
        match = zeros(n)
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
