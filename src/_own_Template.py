class Solution():
    """
    """

    def __init__(self):
        pass

    @staticmethod
    def subsol_01(n):
        """
        """
        return


def sets_gen(subsol):
    import random
    test_sets = []
    for n in range(1000):
        match = subsol(random.randint(0, 100))
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
