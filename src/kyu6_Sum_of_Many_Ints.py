class Solution():
    """
    https://www.codewars.com/kata/54c2fc0552791928c9000517
    for i from 1 to n, do i % m and return the sum
    f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)
    """

    def __init__(self):
        pass

    def f_01(self, n, m):
        '''
        intuitive approach
        '''
        ret = 0
        for i in range(1, n + 1):
            if i < m:
                ret += i
            else:
                ret += i % m

        return ret

    def f_02(self, n, m):
        '''
        specific pattern followed
        '''
        a, b = divmod(n, m)
        ret = 0
        if a != 0:
            ret += a * (m * (m - 1)) >> 1
        if b != 0:
            ret += ((b + 1) * b) >> 1
        return ret


def sets_gen(f):
    import random
    test_set = []
    for _ in range(10):
        n, m = random.randint(0, 100000), random.randint(0, 100000)
        match = f(n, m)
        test_set.append(((n, m), match))
    return test_set


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture
    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(20, prt_docstr=True)
