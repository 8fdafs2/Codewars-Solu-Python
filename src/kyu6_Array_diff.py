class Solution():
    """
    Your goal in this kata is to implement an difference function,
    which subtracts one list from another.

    It should remove all values from list a, which are present in list b.

    difference([1,2],[1]) == [2]
    If a value is present in b, all of its occurrences must
    be removed from the other:

    difference([1,2,2,2,3],[2]) == [1,3]
    """

    def __init__(self):
        pass

    @staticmethod
    def array_diff_01(a, b):
        """
        """
        for ele in b:
            while ele in a:
                a.remove(ele)
        return a

    @staticmethod
    def array_diff_02(a, b):
        """
        """
        b_set = set(b)
        return [x for x in a if x not in b_set]

    @staticmethod
    def array_diff_03(a, b):
        """
        """
        return list(filter(lambda x: x not in b, a))


def sets_gen(subsol):
    import random
    test_sets = []
    for n in range(3, 1000):
        a = [random.randint(0, 9) for _ in range(n)]
        b = [a[random.randint(0, len(a) - 1)] for _ in range(n // 2)]
        match = subsol(a, b)
        test_sets.append((
            (a, b),
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
