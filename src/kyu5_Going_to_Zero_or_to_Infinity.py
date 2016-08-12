from math import factorial, trunc


class Solution():
    """
    https://www.codewars.com/kata/going-to-zero-or-to-infinity

    Consider the following numbers (where n! is factorial(n)):

    u1 = (1 / 1!) * (1!)

    u2 = (1 / 2!) * (1! + 2!)

    u3 = (1 / 3!) * (1! + 2! + 3!)

    un = (1 / n!) * (1! + 2! + 3! + ... + n!)

    Which will win: 1 / n! or (1! + 2! + 3! + ... + n!)?

    Are these number going to 0 because of 1/n! or to infinity due to the sum of factorials?

    Task:

        Calculate (1 / n!) * (1! + 2! + 3! + ... + n!) for a given n.
        Call this function "going(n)" where n is an integer greater or equal to 1.

        To avoid discussions about rounding,
        if the result of the calculation is designed by "result",
        going(n) will return "result" truncated to 6 decimal places.

    Examples:

        1.0000989217538616 will be truncated to 1.000098
        1.2125000000000001 will be truncated to 1.2125

    Remark:

        Keep in mind that factorials grow rather rapidly,
        and you can need to handle large inputs.
    """

    def __init__(self):
        pass

    def going_01(self, n):
        """
        """
        if n == 1:
            return 1

        fn = factorial(n)

        ret = (1 + sum(factorial(x) for x in range(2, n))) / fn + 1

        return int(ret * 1000000) / 1000000

    def going_02(self, n):
        """
        """
        if n == 1:
            return 1

        ret = 1
        f = 1
        for i in range(2, n + 1):
            f *= i
            ret += f

        return round(ret / f - 0.000000499, 6)

    def going_03(self, n):
        """
        """
        if n == 1:
            return 1

        ret = 1
        f = 1
        for i in range(2, n):
            f *= i
            ret += f

        return trunc((ret / (f * n) + 1) * 1000000) / 1000000


def sets_gen(going):
    test_sets = []
    for n in range(1, 500):
        match = going(n)
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
