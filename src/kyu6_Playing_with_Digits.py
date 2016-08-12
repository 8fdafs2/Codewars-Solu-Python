class Solution():
    """
    https://www.codewars.com/kata/5552101f47fc5178b1000050

    Some numbers have funny properties. For example:

    89 --> 8¹ + 9² = 89 * 1
    695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
    46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

    Given a positive integer n written as abcd... (a, b, c, d... being digits)
    and a positive integer p we want to find a positive integer k, if it exists,
    such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words:

        Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

    If it is the case we will return k, if not return -1.

    Note: n, p will always be given as strictly positive integers.

        dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
        dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
        dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
        dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
    """

    def __init__(self):
        pass

    def dig_pow_01(self, n, p):
        """
        intuitive
        """
        digits = [int(digit) for digit in str(n)]

        _sum_ = sum([digit ** (exp_base + p) for exp_base, digit in enumerate(digits)])

        a, b = divmod(_sum_, n)

        if b == 0:
            return a
        return -1

    def dig_pow_02(self, n, p):
        """
        intuitive
        """
        c2d_map = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        }

        digits = [c2d_map[c] for c in str(n)]

        _sum_ = sum([digit ** exp for digit, exp in zip(digits, range(p, p + len(digits)))])

        if _sum_ % n == 0:
            return _sum_ // n
        return -1


def sets_gen(dig_pow):
    import random
    test_sets = []
    for n in range(1, 10000):
        p = random.randint(1, 4)
        match = dig_pow(n, p)
        test_sets.append((
            (n, p),
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
