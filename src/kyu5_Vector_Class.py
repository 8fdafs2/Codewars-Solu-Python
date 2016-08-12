import numpy as np
import math


class Vector_01:
    """
    """
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        return iter(self.__data)

    def __getitem__(self, i):
        return self.__data[i]

    def __str__(self):
        return '(' + ','.join(map(str, self.__data)) + ')'

    def equals(self, other):
        if self.__data != other.__data:
            return False
        return True

    def add(self, other):
        if len(self) != len(other):
            raise ValueError
        return Vector_01([a + b for a, b in zip(self.__data, other.__data)])

    def subtract(self, other):
        if len(self) != len(other):
            raise ValueError
        return Vector_01([a - b for a, b in zip(self.__data, other.__data)])

    def dot(self, other):
        if len(self) != len(other):
            raise ValueError
        return sum([a * b for a, b in zip(self.__data, other.__data)])

    def norm(self):
        return sum([a ** 2 for a in self.__data]) ** 0.5


class Vector_02(list):
    """
    """
    add = lambda self, v: Vector_02([a + b for a, b in zip(self, v)])
    subtract = lambda self, v: Vector_02([a - b for a, b in zip(self, v)])
    dot = lambda self, v: sum([a * b for a, b in zip(self, v)])
    norm = lambda self: math.sqrt(self.dot(self))
    equals = lambda self, v: all(a == b for a, b in zip(self, v))
    __str__ = lambda self: '(' + ','.join(str(i) for i in self) + ')'


class Vector_03(np.ndarray):
    """
    """
    def __new__(cls, input_array, info=None):
        return np.asarray(input_array).view(cls)

    def add(self, vector):
        return self + vector

    def subtract(self, vector):
        return self - vector

    def norm(self):
        return np.linalg.norm(self)

    def equals(self, vector):
        return np.all(self == vector)

    def __str__(self):
        return "({})".format(",".join([str(i) for i in self]))


def validate(v0, v1, v2):
    return [
        # norm, dot
        abs(v0.norm() - math.sqrt(v0.dot(v0))) < 1e-6,
        abs(v1.norm() - math.sqrt(v1.dot(v1))) < 1e-6,
        abs(v2.norm() - math.sqrt(v2.dot(v2))) < 1e-6,
        # equals, add, sub
        v0.add(v1).equals(v0.add(v1).add(v2).subtract(v2)),
        v1.add(v2).equals(v1.add(v2).add(v0).subtract(v0)),
        v2.add(v0).equals(v2.add(v0).add(v1).subtract(v1)),
        # str
        str(v0),
        str(v1),
        str(v2),
    ]


class Solution():
    """
    https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4

    Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

    a = Vector([1,2,3])
    b = Vector([3,4,5])
    c = Vector([5,6,7,8])
    a.add(b) # should return Vector([4,6,8])
    a.subtract(b) # should return Vector([-2,-2,-2])
    a.dot(b) # should return 1*3+2*4+3*5 = 26
    a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
    a.add(c) # raises an exception

    If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

    Also provide:

        a toString function, so that using the vectors from above, a.toString() === '(1,2,3)'
        (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
        an equals function, so that two vectors who have the same components are equal

    The test cases will utilize the user-provided equals method.
    """
    def __init__(self):
        pass

    def calc_01(self, v0, v1, v2):
        """
        intuitive
        """
        return validate(Vector_01(v0), Vector_01(v1), Vector_01(v2))

    def calc_02(self, v0, v1, v2):
        """
        derived list, lambda
        """
        return validate(Vector_02(v0), Vector_02(v1), Vector_02(v2))

    def calc_03(self, v0, v1, v2):
        """
        derived numpy.ndarray
        """
        return validate(Vector_03(v0), Vector_03(v1), Vector_03(v2))


def sets_gen(calc):
    import random
    test_sets = []
    for i in range(1, 101):
        n = random.randint(2, 101)

        v0 = [random.randint(-9, 9) for _ in range(n)]
        v1 = [random.randint(-9, 9) for _ in range(n)]
        v2 = [random.randint(-9, 9) for _ in range(n)]

        match = calc(v0, v1, v2)
        test_sets.append((
            (v0, v1, v2),
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
