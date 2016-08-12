import numpy as np


class Solution():
    """
    https://www.codewars.com/kata/52a382ee44408cea2500074c

    Write a function that accepts a square matrix (n x n 2D array) and returns the determinant of the matrix.
    How to take the determinant of a matrix --
    it is simplest to start with the smallest cases:
    A 1x1 matrix |a| has determinant a. A 2x2 matrix [[a, b], [c, d]] or

    |a b|
    |c d|

    has determinant ad - bc.

    The determinant of an n x n sized matrix is calculated by
    reducing the problem to the calculation of the determinants of
    n n-1 x n-1 matrices. For the 3x3 case, [[a, b, c], [d, e, f], [g, h, i]] or

    |a b c|
    |d e f|
    |g h i|

    the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor)
    where det(a_minor) refers to taking the determinant of the 2x2 matrix
    created by crossing out the row and column in which the element a occurs, or

    |e f|
    |h i|

    Note the alternation of signs.

    The determinant of larger matrices are calculated analogously,
    e.g. if M is a 4x4 matrix with first row [a, b, c, d],
    det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)

    """
    def __init__(self):
        pass

    def determinant_01(self, matrix):
        """
        intuitive recursion
        """
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        def det(matrix, n):
            if n == 1:
                return matrix[0][0]
            if n == 2:
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            ret = 0
            for i in range(n):
                if i % 2 == 0:
                    ret += matrix[0][i] * det([row[:i] + row[i + 1:] for row in matrix[1:]], n - 1)
                else:
                    ret -= matrix[0][i] * det([row[:i] + row[i + 1:] for row in matrix[1:]], n - 1)
            return ret

        return det(matrix, n)

    def determinant_02(self, matrix):
        """
        numpy.linalg.det
        """
        return round(np.linalg.det(matrix))


def sets_gen(determinant):
    import random
    test_sets = []

    for i in range(2, 10):
        matrix = [[random.randint(-10, 10) for _ in range(i)] for _ in range(i)]
        match = determinant(matrix)
        test_sets.append(((matrix, ), match))

    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture
    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
