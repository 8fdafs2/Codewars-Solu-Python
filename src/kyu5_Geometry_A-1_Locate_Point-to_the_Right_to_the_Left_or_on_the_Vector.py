class Solution():
    """
    https://www.codewars.com/kata/554c8a93e466e794fe000001/train/python

    Task
        Your task is to determine the relationship between the given point and the vector.
        Direction of the vector is important! To determine if the point is to the left or to the right,
        you should imagine yourself standing at the beginning of the vector and looking at the end of the vector.

    Arguments
        You are given coordinates of a point and coordinates of a vector on 2D plane:
        point = [x, y]
        vector = [[x, y], [x, y]] (two points, direction is from first to second)
        Vectors always have non-zero length, so you don't have to check for that at this point.

    Return
        Your function must return:
        -1 if the point is to the left of the vector,
        0 if the point is on the same line as vector,
        1 if the point is to the right of the vector.
    """

    def __init__(self):
        pass

    def point_vs_vector_01(self, point, vector):
        """
        cross product of two vectors
        ignore grid background
        """

        def cross_prod(v1, v2):
            a1 = v1[1][0] - v1[0][0]
            b1 = v1[1][1] - v1[0][1]
            a2 = v2[1][0] - v2[0][0]
            b2 = v2[1][1] - v2[0][1]

            return a1 * b2 - a2 * b1

        vector_01 = vector
        vector_02 = [vector[0], point]

        ret = cross_prod(vector_02, vector_01)

        if ret > 0:
            return 1
        if ret < 0:
            return -1
        return 0

    def point_vs_vector_02(self, point, vector):
        """
        line equation
        mx - y + b = 0 <> Ax + By + C = 0
        check the y intercept
        """

        def ln_equ_by_vec(vector):
            [[x1, y1], [x2, y2]] = vector
            return y2 - y1, x1 - x2, x2 * y1 - x1 * y2

        cA, cB, cC = ln_equ_by_vec(vector)

        ret = cA * point[0] + cB * point[1] + cC

        if ret > 0:
            return 1
        if ret < 0:
            return -1
        return 0


def sets_gen(point_vs_vector):
    import random
    test_sets = []
    for _ in range(1000):
        point = [random.randint(-5, 5), random.randint(-5, 5)]
        vector = [[random.randint(-5, 5), random.randint(-5, 5)], [random.randint(-5, 5), random.randint(-5, 5)]]
        match = point_vs_vector(point, vector)
        test_sets.append((
            (point, vector),
            match
        ))
    return test_sets


if __name__ == "__main__":
    sol = Solution()
    from test_fixture import Test_Fixture
    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=True)
