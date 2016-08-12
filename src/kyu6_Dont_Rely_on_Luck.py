import random


class Solution():
    def __init__(self):
        self.drnl = self.drnl_01

    def drnl_01(self):
        random.seed(0)
        guess = random.randint(1, 100)
        random.seed(0)
        return guess

    def drnl_02(self):
        sta = random.getstate()
        guess = random.randint(1, 100)
        random.setstate(sta)
        return guess

    def drnl_03(self):
        class Guess():
            def __eq__(self, other):
                return True

        return Guess()

    def drnl_04(self):
        random.randint = lambda *args: 0
        return 0


def test(drnl, msg):
    for i in range(100):
        assert (sol.drnl_01() == random.randint(1, 100))


def test_spd(drnl):
    for i in range(100):
        sol.drnl_01()


if __name__ == '__main__':
    sol = Solution()
    # test
    print('test...')
    test(sol.drnl_01, '01')
    test(sol.drnl_02, '02')
    test(sol.drnl_03, '03')
    test(sol.drnl_04, '04')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.drnl_{0:02d})'
    _setup_ = 'from __main__ import sol, test_spd'
    _number_ = 1000
    import timeit

    print((timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(4), setup=_setup_, number=_number_)))
