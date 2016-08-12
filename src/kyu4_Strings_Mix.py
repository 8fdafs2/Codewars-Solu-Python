from collections import Counter


class Solution():
    def __init__(self):
        self.mix = self.mix_01

    def mix_01(self, s1, s2):

        hashtab_s1 = {}
        for c in s1:
            if c.islower():
                hashtab_s1[c] = hashtab_s1.get(c, 0) + 1
        hashtab_s2 = {}
        for c in s2:
            if c.islower():
                hashtab_s2[c] = hashtab_s2.get(c, 0) + 1

        ret = []
        for c in set(list(hashtab_s1.keys()) + list(hashtab_s2.keys())):
            cnt_s1 = hashtab_s1.get(c, 0)
            cnt_s2 = hashtab_s2.get(c, 0)
            cnt_mx = max(cnt_s1, cnt_s2)
            if cnt_mx > 1:
                ret.append(('1:' if cnt_mx > cnt_s2 else '2:' if cnt_mx > cnt_s1 else '=:') + c * cnt_mx)

        return '/'.join(sorted(ret, key=lambda x: (-len(x), x[0], x[2])))

    def mix_02(self, s1, s2):

        hashtab_s1 = Counter([c for c in s1 if c.islower()])
        hashtab_s2 = Counter([c for c in s2 if c.islower()])

        ret = []
        for c in set(list(hashtab_s1.keys()) + list(hashtab_s2.keys())):
            cnt_s1 = hashtab_s1.get(c, 0)
            cnt_s2 = hashtab_s2.get(c, 0)
            cnt_mx = max(cnt_s1, cnt_s2)
            if cnt_mx > 1:
                ret.append(('1:' if cnt_mx > cnt_s2 else '2:' if cnt_mx > cnt_s1 else '=:') + c * cnt_mx)

        return '/'.join(sorted(ret, key=lambda x: (-len(x), x[0], x[2])))


def sets_gen(mix):
    import random
    import string
    test_sets = []
    for i in range(1000):
        s1 = ''.join(random.choice(string.printable) for _ in range(random.randrange(10, 100)))
        s2 = ''.join(random.choice(string.printable) for _ in range(random.randrange(10, 100)))
        match = mix(s1, s2)
        test_sets.append((s1, s2, match))
    return test_sets


def test(mix, test_sets, msg):
    for s1, s2, match in test_sets:
        try:
            assert (mix(s1, s2) == match)
        except AssertionError:
            print(s1, s2, match, mix(s1, s2))
            print(msg, '--> Assertion Error <--')


def test_spd(mix, test_sets):
    for s1, s2, _ in test_sets:
        mix(s1, s2)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.mix)
    # test
    print('test...')
    test(sol.mix_01, test_sets, '01')
    test(sol.mix_02, test_sets, '02')
    # test(sol.mix_03, test_sets, '03')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.mix_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import test_spd, test_sets, sol'
    _number_ = 100
    from timeit import timeit

    print('01', timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print('02', timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
    # print('03', timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_))
