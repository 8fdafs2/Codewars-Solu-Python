class Solution():
    def __init__(self):
        self.int_to_english = self.int_to_english_01

    def int_to_english_01(self, n):
        if n == 0:
            return 'zero'
        n2d_map_x = {
            '1': 'one', '2': 'two', '3': 'three', '4': 'four',
            '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
        }
        n2d_map_1x = {
            '0': 'ten', '1': 'eleven', '2': 'twelve', '3': 'thirteen', '4': 'fourteen',
            '5': 'fifteen', '6': 'sixteen', '7': 'seventeen', '8': 'eighteen', '9': 'nineteen',
        }
        n2d_map_x0 = {
            '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
            '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety',
        }
        bn_map = {
            3: 'thousand', 4: 'thousand', 5: 'thousand',
            6: 'million', 7: 'million', 8: 'million',
            9: 'billion', 10: 'billion', 11: 'billion',
            12: 'trillion', 13: 'trillion', 14: 'trillion',
            15: 'quadrillion', 16: 'quadrillion', 17: 'quadrillion',
            18: 'quintillion', 19: 'quintillion', 20: 'quintillion',
            21: 'sextillion', 22: 'sextillion', 23: 'sextillion',
            24: 'septillion', 25: 'septillion', 26: 'septillion',
        }
        n = str(n)[::-1]
        len_n = len(n)
        ret = []
        for i in range(0, len_n, 3):
            ret_sub = []
            n_i = n[i]
            if i + 1 < len_n:
                n_i_1 = n[i + 1]
                if n_i_1 == '1':
                    ret_sub.append(n2d_map_1x[n_i])
                elif n_i != '0':
                    ret_sub.append(n2d_map_x[n_i])
                    if n_i_1 != '0':
                        ret_sub.append(n2d_map_x0[n_i_1])
                elif n_i_1 != '0':
                    ret_sub.append(n2d_map_x0[n_i_1])
                if i + 2 < len_n:
                    n_i_2 = n[i + 2]
                    if n_i_2 != '0':
                        ret_sub.append(n2d_map_x[n_i_2] + ' hundred')
            elif n_i != '0':
                ret_sub.append(n2d_map_x[n_i])
            if ret_sub:
                if i >= 3:
                    ret += [bn_map[i], ] + ret_sub
                else:
                    ret += ret_sub
        ret.reverse()
        return (' '.join(ret))

    def int_to_english_02(self, n):
        if n == 0:
            return 'zero'
        n2d_map_x = {
            '1': ' eno', '2': ' owt', '3': ' eerht', '4': ' ruof',
            '5': ' evif', '6': ' xis', '7': ' neves', '8': ' thgie', '9': ' enin',
        }
        n2d_map_1x = {
            '0': ' net', '1': ' nevele', '2': ' evlewt', '3': ' neetriht', '4': ' neetruof',
            '5': ' neetfif', '6': ' neetxis', '7': ' neetneves', '8': ' neethgie', '9': ' neetenin',
        }
        n2d_map_x0 = {
            '2': ' ytnewt', '3': ' ytriht', '4': ' ytrof', '5': ' ytfif',
            '6': ' ytxis', '7': ' ytneves', '8': ' ythgie', '9': ' ytenin',
        }
        bn_map = {
            3: ' dnasuoht', 4: ' dnasuoht', 5: ' dnasuoht',
            6: ' noillim', 7: ' noillim', 8: ' noillim',
            9: ' noillib', 10: ' noillib', 11: ' noillib',
            12: ' noillirt', 13: ' noillirt', 14: ' noillirt',
            15: ' noillirdauq', 16: ' noillirdauq', 17: ' noillirdauq',
            18: ' noillitniuq', 19: ' noillitniuq', 20: ' noillitniuq',
            21: ' noillitxes', 22: ' noillitxes', 23: ' noillitxes',
            24: ' noillitpes', 25: ' noillitpes', 26: ' noillitpes',
        }
        n = str(n)[::-1]
        len_n = len(n)
        ret = ''
        for i in range(0, len_n, 3):
            ret_sub = ''
            n_i = n[i]
            if i + 1 < len_n:
                n_i_1 = n[i + 1]
                if n_i_1 == '1':
                    ret_sub += n2d_map_1x[n_i]
                elif n_i != '0':
                    ret_sub += n2d_map_x[n_i]
                    if n_i_1 != '0':
                        ret_sub += n2d_map_x0[n_i_1]
                elif n_i_1 != '0':
                    ret_sub += n2d_map_x0[n_i_1]
                if i + 2 < len_n:
                    n_i_2 = n[i + 2]
                    if n_i_2 != '0':
                        ret_sub += ' derdnuh' + n2d_map_x[n_i_2]
            elif n_i != '0':
                ret_sub += n2d_map_x[n_i]
            if ret_sub:
                if i >= 3:
                    ret += bn_map[i] + ret_sub
                else:
                    ret += ret_sub
        return ret[:0:-1]

    def int_to_english_03(self, n):

        # words = ((10 ** 24, 'septillion'), (10 ** 21, 'sextillion'),
        #          (10 ** 18, 'quintillion'), (10 ** 15, 'quadrillion'),
        #          (10 ** 12, 'trillion'), (10 ** 9, 'billion'), (10 ** 6, 'million'),
        #          (10 ** 3, 'thousand'), (10 ** 2, 'hundred'), (90, 'ninety'),
        #          (80, 'eighty'), (70, 'seventy'), (60, 'sixty'), (50, 'fifty'),
        #          (40, 'forty'), (30, 'thirty'), (20, 'twenty'), (19, 'nineteen'),
        #          (18, 'eighteen'), (17, 'seventeen'), (16, 'sixteen'), (15, 'fifteen'),
        #          (14, 'fourteen'), (13, 'thirteen'), (12, 'twelve'), (11, 'eleven'),
        #          (10, 'ten'), (9, 'nine'), (8, 'eight'), (7, 'seven'), (6, 'six'),
        #          (5, 'five'), (4, 'four'), (3, 'three'), (2, 'two'), (1, 'one'))
        # def recur(n):
        #     result = []
        #     for word_value, word_name in words:
        #         q, n = divmod(n, word_value)
        #         if q:
        #             if word_value >= 100:
        #                 result.append(recur(q))
        #             result.append(word_name)
        #         if not n:
        #             return ' '.join(result)
        if n == 0:
            return 'zero'
        words = ((0, 1000000000000000000000000, 'septillion'),
                 (1, 1000000000000000000000, 'sextillion'),
                 (2, 1000000000000000000, 'quintillion'),
                 (3, 1000000000000000, 'quadrillion'),
                 (4, 1000000000000, 'trillion'),
                 (5, 1000000000, 'billion'),
                 (6, 1000000, 'million'),
                 (7, 1000, 'thousand'),
                 (8, 100, 'hundred'),
                 (9, 90, 'ninety'),
                 (10, 80, 'eighty'),
                 (11, 70, 'seventy'),
                 (12, 60, 'sixty'),
                 (13, 50, 'fifty'),
                 (14, 40, 'forty'),
                 (15, 30, 'thirty'),
                 (16, 20, 'twenty'),
                 (17, 19, 'nineteen'),
                 (18, 18, 'eighteen'),
                 (19, 17, 'seventeen'),
                 (20, 16, 'sixteen'),
                 (21, 15, 'fifteen'),
                 (22, 14, 'fourteen'),
                 (23, 13, 'thirteen'),
                 (24, 12, 'twelve'),
                 (25, 11, 'eleven'),
                 (26, 10, 'ten'),
                 (27, 9, 'nine'),
                 (28, 8, 'eight'),
                 (29, 7, 'seven'),
                 (29, 6, 'six'),
                 (30, 5, 'five'),
                 (31, 4, 'four'),
                 (32, 3, 'three'),
                 (33, 2, 'two'),
                 (34, 1, 'one'))
        ret = []

        def recur(n, i_s):
            for i, word_value, word_name in words[i_s:]:
                if n >= word_value:
                    q, n = divmod(n, word_value)
                    if q:
                        if word_value >= 100:
                            recur(q, i + 1)
                        ret.append(word_name)
                    if n == 0:
                        return

        recur(n, 0)
        return ' '.join(ret)

    def int_to_english_04(self, n):
        if n == 0:
            return 'zero'
        words_big = ((1000000000000000000000000, 'septillion'),
                     (1000000000000000000000, 'sextillion'),
                     (1000000000000000000, 'quintillion'),
                     (1000000000000000, 'quadrillion'),
                     (1000000000000, 'trillion'),
                     (1000000000, 'billion'),
                     (1000000, 'million'),
                     (1000, 'thousand'),
                     (1, ''),)
        words_small = ((90, 'ninety'),
                       (80, 'eighty'),
                       (70, 'seventy'),
                       (60, 'sixty'),
                       (50, 'fifty'),
                       (40, 'forty'),
                       (30, 'thirty'),
                       (20, 'twenty'),
                       (19, 'nineteen'),
                       (18, 'eighteen'),
                       (17, 'seventeen'),
                       (16, 'sixteen'),
                       (15, 'fifteen'),
                       (14, 'fourteen'),
                       (13, 'thirteen'),
                       (12, 'twelve'),
                       (11, 'eleven'),
                       (10, 'ten'),
                       (9, 'nine'),
                       (8, 'eight'),
                       (7, 'seven'),
                       (6, 'six'),
                       (5, 'five'),
                       (4, 'four'),
                       (3, 'three'),
                       (2, 'two'),
                       (1, 'one'))
        n2d_map_x00 = {
            1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred',
            5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred',
        }
        ret = []

        for val_big, nam_big in words_big:
            if n >= val_big:
                q, n = divmod(n, val_big)
                if q:
                    if q >= 100:
                        a, q = divmod(q, 100)
                        ret.append(n2d_map_x00[a])
                    if q:
                        for val_small, nam_small in words_small:
                            a, q = divmod(q, val_small)
                            if a:
                                ret.append(nam_small)
                            if q == 0:
                                break
                    ret.append(nam_big)
                if n == 0:
                    break

        if ret[-1] == '':
            return ' '.join(ret[:-1])

        return ' '.join(ret)


def sets_gen(int_to_english):
    import random
    test_sets = []
    for i in range(1000):
        n = random.randint(0, 10 ** 26)
        match = int_to_english(n)
        test_sets.append((n, match))
    return test_sets


def test(int_to_english, test_sets, msg):
    for n, match in test_sets:
        try:
            assert (int_to_english(n) == match)
        except AssertionError as ex:
            print((n, match, int_to_english(n)))
            print((msg, '--> Assertion Error <--'))


def test_spd(int_to_english, test_sets):
    for n, _ in test_sets:
        int_to_english(n)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.int_to_english)
    # test
    print('test...')
    test(sol.int_to_english_01, test_sets, '01')
    test(sol.int_to_english_02, test_sets, '02')
    test(sol.int_to_english_03, test_sets, '03')
    test(sol.int_to_english_04, test_sets, '04')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.int_to_english_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 100
    import timeit

    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(4), setup=_setup_, number=_number_))
