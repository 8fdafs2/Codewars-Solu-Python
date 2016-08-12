class Solution():
    """
    https://www.codewars.com/kata/54b679eaac3d54e6ca0008c9

    The purpose of this kata is to write a higher-order function
    which is capable of creating a function
    that iterates on a specified function a given number of times.
    This new functions takes in an argument as a seed to start the computation from.

    For instance, consider the function getDouble.
    When run twice on value 3, yields 12 as shown below.

    getDouble(3) => 6
    getDouble(6) => 12
    """

    def __init__(self):
        pass

    def create_iterator_01(self, func, n):
        """
        for-loop, no recursion
        """
        def f(x):
            for _ in range(n):
                x = func(x)

            return x

        if n <= 1:
            return func
        return f

    def create_iterator_02(self, func, n):
        """
        recursion
        """
        def f(n):
            if n <= 1:
                return func
            return lambda x: func(f(n - 1)(x))

        return f(n)


def sets_gen(create_iterator):
    import random
    test_sets = []
    for n in range(1, 101):
        func = random.choice((
            lambda x: x * 1,
            lambda x: x * 2,
            lambda x: x * 3,
            lambda x: x * 4,
        ))
        arg = random.randint(0, 10)
        match = create_iterator(func, n)(arg)
        test_sets.append((
            (func, n),
            (arg, ),
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
