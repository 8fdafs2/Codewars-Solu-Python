from STree import STree


class Solution():
    """
    Find longest Common Substrings
    """

    def __init__(self):
        pass

    def lcsuff_01(self, x, y):
        """
        dynamic programming
        """
        n_x = len(x)
        n_y = len(y)

        l = [[0, ] * n_y for _ in range(n_x)]
        z = 0
        ret = ''

        for i in range(n_x):
            for j in range(n_y):
                if x[i] == y[j]:
                    if i == 0 or j == 0:
                        l[i][j] = 1
                    else:
                        l[i][j] = l[i - 1][j - 1] + 1
                    if l[i][j] > z:
                        z = l[i][j]
                        ret = x[i - z + 1:i + 1]
        return ret

    def lcsuff_02(self, x, y):
        """
        generalized suffix tree
        """
        gst = STree([x, y])
        return gst.lcs()


def sets_gen(lcsuff):
    import random
    letters = 'abcdefg'
    test_sets = []
    for i in range(10, 100):
        x = ''.join([random.choice(letters) for _ in range(i)])
        y = ''.join([random.choice(letters) for _ in range(i)])
        match = lcsuff(x, y)
        test_sets.append((
            (x, y),
            match
        ))
    return test_sets


def cmpr(to_match, test_set):
    args, match = test_set
    x, y = args
    for x_or_y in (x, y):
        if to_match not in x_or_y:
            return False
    return len(to_match) == len(match)


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen, cmpr)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
