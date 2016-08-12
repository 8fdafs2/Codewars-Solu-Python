class Solution():
    """
    https://www.codewars.com/kata/efficient-power-modulo-n

    Your task is to create a new implementation of modpow so that it computes (x^y)%n for large y.
    The problem with the current implementation is that
    the output of Math.pow is so large on our inputs that it won't fit in a 64-bit float.

    You're also going to need to be efficient, because we'll be testing some pretty big numbers.
    """

    def __init__(self):
        pass

    @staticmethod
    def power_mod_01(x, y, n):
        """
        built-in
        """
        return pow(x, y, n)

    @staticmethod
    def power_mod_02(x, y, n):
        """
        x ** y % n
        """
        return x ** y % n

    @staticmethod
    def power_mod_03(x, y, n):
        """
        exponentiation by squaring, iteration
        """
        if n == 1:
            return 0
        ret = 1
        x %= n
        while y != 0:
            if y & 1 == 1:
                ret = ret * x % n
            y >>= 1
            x = x * x % n

        return ret

    @staticmethod
    def power_mod_04(x, y, n):
        """
        exponentiation by squaring, recursion
        """

        def recur(x, y, n):
            if y == 0:
                return 1

            if y & 1 == 0:
                ret = recur(x, y >> 1, n)
                return ret * ret % n
            ret = recur(x, y >> 1, n)
            return ret * ret * x % n

        if n == 1:
            return 0
        return recur(x, y, n)


def sets_gen(power_mod):
    import random
    test_sets = []
    for _ in range(1000):
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        n = random.randint(1, 1000)
        match = power_mod(x, y, n)
        test_sets.append((
            (x, y, n),
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
