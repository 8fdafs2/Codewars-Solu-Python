class Solution():
    def __init__(self):
        self.maskify = self.maskify_01

    def maskify_01(self, cc):
        return '#' * (len(cc) - 4) + cc[-4:]

    def maskify_02(self, cc):
        return '{cc:#>{w}}'.format(cc=cc[-4:], w=len(cc))

    def maskify_03(self, cc):
        return cc[-4:].rjust(len(cc), '#')


def sets_gen(maskify):
    import random
    import string
    test_sets = []
    for i in range(1000):
        cc = ''.join([random.choice(string.printable) for _ in range(i)])
        match = maskify(cc)
        test_sets.append((cc, match))
    return test_sets


def test(maskify, test_sets, msg):
    for cc, match in test_sets:
        try:
            assert (maskify(cc) == match)
        except AssertionError:
            print((cc, match, maskify(cc)))
            print((msg, '--> Assertion Error <--'))


def test_spd(maskify, test_sets):
    for cc, _ in test_sets:
        maskify(cc)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.maskify)
    # test
    print('test...')
    test(sol.maskify_01, test_sets, '01')
    test(sol.maskify_02, test_sets, '02')
    test(sol.maskify_03, test_sets, '03')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.maskify_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 100
    import timeit

    print((timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_)))
