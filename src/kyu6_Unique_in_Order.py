from itertools import groupby


class Solution():
    def __init__(self):
        self.unique_in_order = self.unique_in_order_01

    def unique_in_order_01(self, iterable):
        if not iterable:
            return []
        if len(iterable) == 1:
            return list(iterable)
        ret = []
        for ele, ele_next in zip(iterable, iterable[1:]):
            if ele != ele_next:
                ret.append(ele)

        if not ret:
            return [iterable[-1]]

        if ret and ret[-1] != iterable[-1]:
            return ret + [iterable[-1]]

        return ret

    def unique_in_order_02(self, iterable):
        ret = []
        ele_prev = None
        for ele in iterable:
            if ele != ele_prev:
                ret.append(ele)
                ele_prev = ele
        return ret

    def unique_in_order_03(self, iterable):
        return [ele for ele, _ in groupby(iterable)]

    def unique_in_order_04(self, iterable):
        ret = []
        for ele in iterable:
            if len(ret) == 0 or ele != ret[-1]:
                ret.append(ele)

        return ret

    def unique_in_order_05(self, iterable):
        ret = []
        for i, ele in enumerate(iterable):
            if i == 0 or iterable[i - 1] != ele:
                ret.append(ele)
        return ret


def sets_gen(unique_in_order):
    import random
    import string
    test_sets = []
    for i in range(1000):
        iterable = [random.choice(string.printable) for _ in range(i)]
        match = unique_in_order(iterable)
        test_sets.append((iterable, match))
    return test_sets


def test(unique_in_order, test_sets, msg):
    for iterable, match in test_sets:
        try:
            assert (unique_in_order(iterable) == match)
        except AssertionError:
            print((iterable, match, unique_in_order(iterable)))
            print((msg, '--> Assertion Error <--'))


def test_spd(unique_in_order, test_sets):
    for iterable, _ in test_sets:
        unique_in_order(iterable)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.unique_in_order)
    # test
    print('test...')
    test(sol.unique_in_order_01, test_sets, '01')
    test(sol.unique_in_order_02, test_sets, '02')
    test(sol.unique_in_order_03, test_sets, '03')
    test(sol.unique_in_order_04, test_sets, '04')
    test(sol.unique_in_order_05, test_sets, '05')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.unique_in_order_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 100
    import timeit

    print((timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(4), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(5), setup=_setup_, number=_number_)))
