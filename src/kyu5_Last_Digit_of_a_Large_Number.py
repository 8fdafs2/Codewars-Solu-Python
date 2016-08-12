class Solution():
    """
    https://www.codewars.com/kata/5511b2f550906349a70004e1

    Define a function

    def last_digit(n1, n2):
      return

    that takes in two numbers a and b and returns the last decimal digit of a^b.
    Note that a and b may be very large!
    For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969.
    The last decimal digit of (2^200)^(2^300),
    which has over 10^92 decimal digits, is 6.
    The inputs to your function will always be non-negative integers.

    Examples

        last_digit(4, 1)                # returns 4
        last_digit(4, 2)                # returns 6
        last_digit(9, 7)                # returns 9
        last_digit(10, 10 ** 10)        # returns 0
        last_digit(2 ** 200, 2 ** 300)  # returns 6

    Remarks

        JavaScript

        Since JavaScript doesn't have native arbitrary large integers,
        your arguments are going to be strings representing non-negative integers, e.g.

        lastDigit("10", "10000000000");

        The kata is still as hard as the variants for Haskell or Python, don't worry.
    """
    def __init__(self):
        pass

    def last_digit_01(self, n1, n2):
        """
        repeat pattern
        """
        if n2 == 0:
            return 1
        hashtab = {
            0: [0, ],
            1: [1, ],
            2: [2, 4, 8, 6],
            3: [3, 9, 7, 1],
            4: [4, 6],
            5: [5, ],
            6: [6, ],
            7: [7, 9, 3, 1],
            8: [8, 4, 2, 6],
            9: [9, 1],
        }
        seq_n1 = hashtab[n1 % 10]
        a, b = divmod(n2, len(seq_n1))
        if b == 0:
            return seq_n1[-1]
        return seq_n1[b - 1]

    def last_digit_02(self, n1, n2):
        """
        direct
        """
        return pow(n1, n2, 10)

    def last_digit_03(self, n1, n2):
        """
        repeat pattern w/ padding
        """
        if n2 == 0:
            return 1
        hashtab = {
            0: [0, 0, 0, 0],
            1: [1, 1, 1, 1],
            2: [2, 4, 8, 6],
            3: [3, 9, 7, 1],
            4: [4, 6, 4, 6],
            5: [5, 5, 5, 5],
            6: [6, 6, 6, 6],
            7: [7, 9, 3, 1],
            8: [8, 4, 2, 6],
            9: [9, 1, 9, 1],
        }
        return hashtab[n1 % 10][n2 % 4 - 1]

    def last_digit_04(self, n1, n2):
        """
        pow(number, x) % 10 == pow(number % 10, x % 4 + 4) % 10
        """
        # pow(number, x) % 10 == pow(number % 10, x) % 10
        # pow(number, x) % 10 == pow(number, x % 4 + 4) % 10, with the exception of x == 0
        if n2 == 0:
            return 1
        return (n1 % 10) ** (n2 % 4 + 4) % 10


def sets_gen(last_digit):
    import random
    test_sets = []
    for i in range(1000):
        n1 = random.randint(0, 10000000000)
        n2 = random.randint(0, 10000000000)
        match = last_digit(n1, n2)
        test_sets.append((
            (n1, n2),
            match
        ))
    return test_sets

if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=True)