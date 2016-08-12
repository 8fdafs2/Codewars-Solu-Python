from functools import reduce


class Solution():
    """
    https://www.codewars.com/kata/perimeter-of-squares-in-a-rectangle

    The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8.
    It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

    Say that S(n) is the nth term of the above sum. So

    S(0) = 1, S(1) = 1, S(2) = 2, ... , S(5) = 8

    Could you give the sum S of the perimeters of all the squares in a rectangle when
    there are n + 1 squares disposed in the same manner as in the drawing:

    S = S(0) + S(1) + ... + S(n) ?

    alternative text

    Hint:

    See Fibonacci sequence and beware of rather big n:-)

    Ref:

    http://oeis.org/A000045

    The function perimeter has for parameter n where n + 1 is the number of squares
    (they are numbered from 0 to n) and returns the total perimeter of all the squares.

    perimeter(5)  should return 80
    perimeter(7)  should return 216
    """

    def __init__(self):
        pass

    def perimeter_01(self, n):
        """
        for-loop, intuitive
        """

        def fibonacci(n):
            if n == 0:
                return 0
            fib1, fib2 = 0, 1
            for i in range(2, n + 1):
                fib1, fib2 = fib2, fib1 + fib2
            return fib2

        return (fibonacci(n + 3) - 1) * 4

    def perimeter_02(self, n):
        """
        lucas numbers
        """
        def lucas(n):
            if n == 1:
                return 1, 1
            l, f = lucas(n >> 1)
            l, f = (l * l + 5 * f * f) >> 1, l * f

            if n & 1:
                return (l + 5 * f) >> 1, (l + f) >> 1
            return l, f

        def fib(n):
            if n & 1:
                return lucas(n)[1]
            return reduce(lambda l, f: l * f, lucas(n >> 1))

        return (fib(n + 3) - 1) * 4

    def perimeter_03(self, n):
        """
        for-loop, intuitive, altered
        """
        a, b = 1, 1
        for i in range(n + 1):
            a, b = b, a + b
        return 4 * (b - 1)


def sets_gen(perimeter):
    test_sets = []
    for n in range(1, 2000):
        match = perimeter(n)
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
