class Solution():
    def __init__(self):
        self.solution = self.solution_01

    def solution_01(self, digits):

        seq = digits[: 5]
        for i in range(1, len(digits) - 4):
            if digits[i: i + 5] > seq:
                seq = digits[i: i + 5]

        return int(seq)

    def solution_02(self, digits):

        return max([int(digits[i:i + 5]) for i in range(len(digits) - 4)])

    def solution_03(self, digits):

        return int(max([digits[i:i + 5] for i in range(len(digits) - 4)]))

    def solution_04(self, digits):

        dseq = '9876543210'
        for a in dseq:
            for b in dseq:
                for c in dseq:
                    for d in dseq:
                        for e in dseq:
                            if digits.find(a + b + c + d + e) != -1:
                                return int(a + b + c + d + e)

    def solution_05(self, digits):

        ret = 99999
        while str(ret) not in digits:
            ret -= 1

        return ret


def sets_gen(solution):
    import random
    test_sets = []
    dseq = '9876543210'
    for i in range(5, 1001, 3):
        digits = ''.join([random.choice(dseq) for _ in range(i)])
        match = solution(digits)
        test_sets.append((digits, match))
    return test_sets


def test(solution, test_sets, msg):
    for digits, match in test_sets:
        try:
            assert (solution(digits) == match)
        except AssertionError:
            print(digits, match, solution(digits))
            print(msg, '--> Assertion Error <--')


def test_spd(solution, test_sets):
    for digits, _ in test_sets:
        solution(digits)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.solution)
    # test
    print('test...')
    test(sol.solution_01, test_sets, '01')
    test(sol.solution_02, test_sets, '02')
    test(sol.solution_03, test_sets, '03')
    test(sol.solution_04, test_sets, '04')
    test(sol.solution_05, test_sets, '05')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.solution_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 100
    import timeit

    print('01', timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print('02', timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
    print('03', timeit.timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_))
    print('04', timeit.timeit(stmt=_stmt_.format(4), setup=_setup_, number=_number_))
    print('05', timeit.timeit(stmt=_stmt_.format(5), setup=_setup_, number=_number_))
