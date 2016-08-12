from math import sqrt, hypot


class Solution():
    """
    https://www.codewars.com/kata/parabolic-arc-length

    We want to approximate the length of a curve representing a function y = f(x) with a<= x <= b.
    First, we split the interval [a, b] into n sub-intervals with
    widths h1, h2, ... , hn by defining points x1, x2 , ... , xn-1 between a and b.
    This defines points P0, P1, P2, ... , Pn on the curve whose x-coordinates are
    a, x1, x2 , ... , xn-1, b and y-coordinates f(a), f(x1), ..., f(xn-1), f(b) .
    By connecting these points, we obtain a polygonal path approximating the curve.

    Our task is to approximate the length of a parabolic arc representing
    the curve y = x * x with x in the interval [0, 1].
    We will take a common step h between the points xi: h1, h2, ... , hn = h = 1/n and
    we will consider the points P0, P1, P2, ... , Pn on the curve.
    The coordinates of each Pi are (xi, yi = xi * xi).

    The function len_curve (or similar in other languages) takes n as parameter (number of sub-intervals) and
    returns the length of the curve truncated to 9 decimal places.
    """

    def __init__(self):
        pass

    def len_curve_01(self, n):
        """
        intuitive
        """
        x = 0
        y = 0
        ret = 0
        for i in range(1, n + 1):
            x_ = i / n
            y_ = x_ * x_
            ret += sqrt((y_ - y) * (y_ - y) + (x_ - x) * (x_ - x))
            x = x_
            y = y_

        return int(ret * 1000000000) / 1000000000

    def len_curve_02(self, n):
        """
        intuitive, opt
        """
        x = 0
        ret = 0
        dx = 1 / n
        for _ in range(n):
            x_ = x + dx
            ret += sqrt((x_ + x) * (x_ + x) + 1)
            x = x_

        return int(ret * dx * 1000000000) / 1000000000

    def len_curve_03(self, n):
        """
        k, k + 1
        """
        ret = sum(hypot(k + k + 1, n) for k in range(n)) / (n * n)
        return int(ret * 1000000000) / 1000000000

    def len_curve_04(self, n):
        """
        k, k + 1
        """
        ret = sum(abs((k + k + 1) / n + 1j) for k in range(n)) / n
        return int(ret * 1000000000) / 1000000000


def sets_gen(len_curve):
    test_sets = []
    for n in range(1, 1000):
        match = len_curve(n)
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
