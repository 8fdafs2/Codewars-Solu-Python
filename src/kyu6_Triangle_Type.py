import math


class Solution():
    """
    https://www.codewars.com/kata/53907ac3cd51b69f790006c5

    In this kata, you should calculate type of triangle with three given sides a, b and c (given in any order).

    If all angles are less than 90°, this triangle is acute and function should return 1.
    If one angle is strictly 90°, this triangle is right and function should return 2.
    If one angle more than 90°, this triangle is obtuse and function should return 3.
    If three sides cannot form triangle, or one angle is 180° (which turns triangle into segment) - function should return 0.

    Input parameters are sides of given triangle. All input values are non-negative floating point or integer numbers (or both).
    """

    def __init__(self):
        pass

    def triangle_type_01(self, a, b, c):
        """
        the Pythagorean theorem
        """
        a, b, c = sorted([a, b, c])
        if (a + b) <= c:
            return 0
        flag = a * a + b * b - c * c
        if flag == 0:
            return 2
        if flag < 0:
            return 3
        return 1

    def triangle_type_02(self, a, b, c):
        """
        included angle calculation
        """
        a, b, c = sorted([a, b, c])
        if (a + b) <= c:
            return 0
        # c^2 = a^2 + b^2 - 2*a*b*cos(theta)
        # theta = arccos((a^2 + b^2 - c^2) / 2*a*b)
        angle = math.acos((a * a + b * b - c * c) / (2.0 * a * b))
        flag = angle + angle - math.pi
        if flag == 0:
            return 2
        if flag > 0:
            return 3
        return 1


def sets_gen(triangle_type):
    import random
    test_sets = []
    for i in range(1000):
        a = random.randint(0, 15)
        b = random.randint(0, 15)
        c = random.randint(0, 15)
        match = triangle_type(a, b, c)
        test_sets.append((
            (a, b, c),
            match))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=True)
