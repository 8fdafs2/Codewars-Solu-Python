class Solution():
    def __init__(self):
        self.spin_words = self.spin_words_01

    def spin_words_01(self, sentence):
        word_lst = []
        for word in sentence.split(' '):
            if len(word) >= 5:
                word_lst.append(word[::-1])
            else:
                word_lst.append(word)
        return ' '.join(word_lst)

    def spin_words_02(self, sentence):
        word_lst = sentence.split(' ')
        for i in range(len(word_lst)):
            if len(word_lst[i]) >= 5:
                word_lst[i] = word_lst[i][::-1]
        return ' '.join(word_lst)

    def spin_words_03(self, sentence):
        return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])

    def spin_words_04(self, sentence):
        sentence = list(sentence)
        i_w_s = 0
        for i, c in enumerate(sentence + [' ']):
            if c == ' ':
                if i - i_w_s >= 5:
                    sentence[i_w_s:i] = sentence[i_w_s:i][::-1]
                i_w_s = i + 1
        return ''.join(sentence)


def sentence_gen(num_word):
    import random
    import string
    sentence = []
    for i in range(num_word):
        sentence.append(''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(2, 10))]))
    return ' '.join(sentence)


def sets_gen(spin_words):
    import random
    test_sets = []
    for _ in range(1000):
        sentence = sentence_gen(random.randint(10, 15))
        match = spin_words(sentence)
        test_sets.append((sentence, match))
    return test_sets


def test(spin_words, test_sets, msg):
    for sentence, match in test_sets:
        try:
            assert (spin_words(sentence) == match)
        except AssertionError as ex:
            print((sentence, match, spin_words(sentence)))
            print((msg, '--> Assertion Error <--'))


def test_spd(spin_words, test_sets):
    for sentence, _ in test_sets:
        spin_words(sentence)


if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.spin_words)
    # test
    print('test...')
    test(sol.spin_words_01, test_sets, '01')
    test(sol.spin_words_02, test_sets, '02')
    test(sol.spin_words_03, test_sets, '03')
    test(sol.spin_words_04, test_sets, '04')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.spin_words_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 500
    import timeit

    print((timeit.timeit(stmt=_stmt_.format(0o1), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(0o2), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(0o3), setup=_setup_, number=_number_)))
    print((timeit.timeit(stmt=_stmt_.format(0o4), setup=_setup_, number=_number_)))
