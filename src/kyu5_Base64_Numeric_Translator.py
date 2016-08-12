from functools import reduce


class Solution():
    """
    Our standard numbering system is (Base 10). That includes 0 through 9.
    Binary is (Base 2), only 1’s and 0’s.
    And Hexadecimal is (Base 16) (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F).
    A hexadecimal “F” has a (Base 10) value of 15.
    (Base 64) has 64 individual characters which translate in value in (Base 10) from between 0 to 63.
    Write a method that will convert a string from (Base 64) to it's (Base 10) integer value.

    The (Base 64) characters from least to greatest will be

    ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/

    Where 'A' is equal to 0 and '/' is equal to 63.

    Just as in standard (Base 10) when you get to the highest individual integer 9
    the next number adds an additional place and starts at the beginning 10;
    so also (Base 64) when you get to the 63rd digit '/' and
    the next number adds an additional place and starts at the beginning "BA".

    Example:

    base64_to_base10("/") # => 63
    base64_to_base10("BA") # => 64
    base64_to_base10("BB") # => 65
    base64_to_base10("BC") # => 66

    Write a method base64_to_base10 that will take a string (Base 64) number and
    output it's (Base 10) value as an integer.
    """

    def __init__(self):
        pass

    def base64_to_base10_01(self, str):
        """
        intuitive, for-loop, MSB to LSB
        """
        base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

        ret = 0
        for c in str:
            ret *= 64
            ret += base64.index(c)

        return ret

    def base64_to_base10_02(self, str):
        """
        intuitive, reduce, MSB to LSB
        """
        base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

        return reduce(lambda ret, c: ret * 64 + base64.index(c), str, 0)

    def base64_to_base10_03(self, str):
        """
        intuitive, LSB to MSB
        """
        base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

        return sum(base64.index(c) * 64 ** i for i, c in enumerate(str[::-1]))


def sets_gen(base64_to_base10):
    import random
    base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    test_sets = []
    for i in range(1, 500):
        str = ''.join([random.choice(base64) for _ in range(i)])
        match = base64_to_base10(str)
        test_sets.append((
            (str,),
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
