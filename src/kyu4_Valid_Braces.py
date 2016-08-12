class Solution():
    def __init__(self):
        self.validBraces = self.validBraces_01

    def validBraces_01(self, string):
        brace_map_01 = {'(': True, ')': False}
        brace_map_02 = {'[': True, ']': False}
        brace_map_03 = {'{': True, '}': False}
        counterpartof = {'(': ')', '[': ']', '{': '}'}
        brace_cnts = [0, 0, 0]
        stack = []
        for brace in string:
            if brace in brace_map_01:
                if brace_map_01[brace]:
                    stack.append(counterpartof[brace])
                    brace_cnts[0] += 1
                else:
                    brace_cnts[0] -= 1
                    if brace_cnts[0] < 0:
                        return False
                    if stack.pop() != brace:
                        return False
            elif brace in brace_map_02:
                if brace_map_02[brace]:
                    stack.append(counterpartof[brace])
                    brace_cnts[1] += 1
                else:
                    brace_cnts[1] -= 1
                    if brace_cnts[1] < 0:
                        return False
                    if stack.pop() != brace:
                        return False
            elif brace in brace_map_03:
                if brace_map_03[brace]:
                    stack.append(counterpartof[brace])
                    brace_cnts[2] += 1
                else:
                    brace_cnts[2] -= 1
                    if brace_cnts[2] < 0:
                        return False
                    if stack.pop() != brace:
                        return False
        if any(brace_cnts):
            return False
        return True

    def validBraces_02(self, string):
        brace_map = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for brace in string:
            if brace in list(brace_map.keys()):
                stack.append(brace_map[brace])
            elif len(stack) == 0 or stack.pop() != brace:
                return False
        if len(stack) != 0:
            return False
        return True


def validBraces_gen(length):
    import random
    counterpartof = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    braces_open_set = '([{'
    braces = []
    braces_close = []
    while len(braces) + len(braces_close) < length:
        if braces_close:
            if random.choice((True, False)):
                braces.append(random.choice(braces_open_set))
                braces_close.append(counterpartof[braces[-1]])
            else:
                braces.append(braces_close.pop())
        else:
            braces.append(random.choice(braces_open_set))
            braces_close.append(counterpartof[braces[-1]])
    while braces_close:
        braces.append(braces_close.pop())
    return ''.join(braces)


def sets_gen(validBraces):
    import random
    test_sets = []
    for i in range(0, 200):
        if i % 2 == 0 and random.choice((True, False)):
            string = validBraces_gen(i)
        else:
            string = ''.join([random.choice('()[]{}') for _ in range(i)])
        match = validBraces(string)
        test_sets.append((string, match))
    return test_sets


def test(validBraces, test_sets, msg):
    for string, match in test_sets:
        try:
            assert (validBraces(string) == match)
        except AssertionError as ex:
            print((string, match, validBraces(string)))
            print((msg, '--> Assertion Error <--'))


def test_spd(validBraces, test_sets):
    for string, _ in test_sets:
        validBraces(string)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.validBraces)
    # test
    print('test...')
    test(sol.validBraces_01, test_sets, '01')
    test(sol.validBraces_02, test_sets, '02')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.validBraces_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 1000
    import timeit

    print((timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_)))
