class Solution():
    def __init__(self):
        self.next_bigger = self.next_bigger_01

    def next_bigger_01(self, n):
        n = list(str(n)[::-1])
        for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                for j in range(i + 1):
                    if n[j] > n[i + 1]:
                        n[j], n[i + 1] = n[i + 1], n[j]
                        n = n[i + 1:][::-1] + sorted(n[:i + 1])
                        return int(''.join(n))
        return -1

    def next_bigger_02(self, n):
        n = list(str(n))
        for i in range(len(n) - 1, 0, -1):
            if n[i] > n[i - 1]:
                for j in range(len(n) - 1, i - 1, -1):
                    if n[j] > n[i - 1]:
                        n[j], n[i - 1] = n[i - 1], n[j]
                        n = n[:i] + sorted(n[i:])
                        return int(''.join(n))
        return -1

    def next_bigger_03(self, n):
        n = str(n)[::-1]
        for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                for j in range(i + 1):
                    if n[j] > n[i + 1]:
                        return int(n[i + 2:][::-1] + n[j] + ''.join(sorted(n[j + 1:i + 2] + n[:j])))
        return -1

    def next_bigger_04(self, n):
        i, ss = n, sorted(str(n))

        if str(n) == ''.join(ss[::-1]):
            return -1

        while True:
            i += 1
            if sorted(str(i)) == ss and i != n:
                return i


def sets_gen(next_bigger):
    import random
    test_sets = []
    for i in range(100):
        n = random.randint(1, 10 ** 10)
        match = next_bigger(n)
        test_sets.append((n, match))
    return test_sets


def test(next_bigger, test_sets, msg):
    for n, match in test_sets:
        try:
            assert (next_bigger(n) == match)
        except AssertionError:
            print((n, match, next_bigger(n)))
            print((msg, '--> Assertion Error <--'))


def test_spd(next_bigger, test_sets):
    for n, _ in test_sets:
        next_bigger(n)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.next_bigger)
    # test
    print('test...')
    test(sol.next_bigger_01, test_sets, '01')
    test(sol.next_bigger_02, test_sets, '02')
    test(sol.next_bigger_03, test_sets, '03')
    test(sol.next_bigger_04, test_sets, '04')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.next_bigger_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 1000
    import timeit

    print((timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_)))
    # print(timeit.timeit(stmt=_stmt_.format(4), setup=_setup_, number=_number_))
