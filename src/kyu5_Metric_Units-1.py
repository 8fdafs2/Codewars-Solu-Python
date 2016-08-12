import math

class Solution():
    def __init__(self):
        self.meters = self.meters_01

    def meters_01(self, x):
        prefix_map = {
            0: (1, 'm',),  # 3 - 1
            1: (1000, 'km',),  # 6 - 1
            2: (1000000, 'Mm',),  # 9 - 1
            3: (1000000000, 'Gm',),  # 12 - 1
            4: (1000000000000, 'Tm',),  # 15 - 1
            5: (1000000000000000, 'Pm',),  # 18 - 1
            6: (1000000000000000000, 'Em',),  # 21 - 1
            7: (1000000000000000000000, 'Zm',),  # 24 - 1
            8: (1000000000000000000000000, 'Ym',),  # 27 - 1
        }
        # a, b = prefix_map[(len(str(int(x))) - 1) // 3]
        a, b = prefix_map[int(math.log10(x) / 3)]
        return '{:g}{:s}'.format(float(x) / a, b)

    def meters_02(self, x):
        prefix_seq = [
            (1000000000000000000000000, 'Ym',),
            (1000000000000000000000, 'Zm', ),
            (1000000000000000000, 'Em',),
            (1000000000000000, 'Pm',),
            (1000000000000, 'Tm',),
            (1000000000, 'Gm',),
            (1000000, 'Mm',),
            (1000, 'km',),
            (1, 'm',),
        ]
        for a, b in prefix_seq:
            if x >= a:
                return '{:g}{:s}'.format(float(x) / a, b)

    def meters_03(self, x):
        prefix_lst = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
        i = int(math.log10(x) / 3)
        return '{:g}{:s}m'.format(float(x) / 1000**i, prefix_lst[i])



def sets_gen(meters):
    import random
    test_sets = []
    for i in range(1000):
        x = random.randint(1, 10 ** 27)
        match = meters(x)
        test_sets.append((x, match))
    return test_sets


def test(meters, test_sets, msg):
    for x, match in test_sets:
        try:
            assert (meters(x) == match)
        except AssertionError as ex:
            print((x, match, meters(x)))
            print((msg, '--> Assertion Error <--'))


def test_spd(meters, test_sets):
    for x, _ in test_sets:
        meters(x)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.meters)
    # test
    print('test...')
    test(sol.meters_01, test_sets, '01')
    test(sol.meters_02, test_sets, '02')
    test(sol.meters_03, test_sets, '03')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.meters_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 100
    import timeit

    print((timeit.timeit(stmt=_stmt_.format(0o1), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(0o2), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(0o3), setup=_setup_, number=_number_)))
