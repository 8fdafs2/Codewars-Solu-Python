from collections import Counter


class Solution():
    """
    https://www.codewars.com/kata/55c04b4cc56a697bb0000048

    Write function scramble(str1,str2) that returns true if
    a portion of str1 characters can be rearranged to match str2, otherwise returns false.

    For example:
    str1 is 'rkqodlw' and str2 is 'world' the output should return true.
    str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
    str1 is 'katas' and str2 is 'steak' should return false.

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered
    """

    def __init__(self):
        pass

    def scramble_01(self, s1, s2):
        """
        counter comparison one-by-one
        """
        hashtab_s1 = Counter(s1)
        hashtab_s2 = Counter(s2)
        for c in hashtab_s2:
            if c not in hashtab_s1:
                return False
            if hashtab_s1[c] < hashtab_s2[c]:
                return False

        return True

    def scramble_02(self, s1, s2):
        """
        counter subtraction
        """
        return not bool(Counter(s2) - Counter(s1))

    def scramble_03(self, s1, s2):
        """
        count
        """
        for c in set(s2):
            if s1.count(c) < s2.count(c):
                return False
        return True


def sets_gen(scramble):
    import random
    letters = 'abcdefghijklmnopqrstuvwxyz'
    test_sets = []
    for i in range(1000):
        if random.choice((True, False)):
            s2 = [random.choice(letters) for _ in range(8, 13)]
            s1 = [random.choice(letters) for _ in range(1, 7)] + s2
            random.shuffle(s1)
        else:
            s2 = [random.choice(letters) for _ in range(8, 13)]
            s1 = [random.choice(letters) for _ in range(9, 20)]
        s1 = ''.join(s1)
        s2 = ''.join(s2)
        match = scramble(s1, s2)
        test_sets.append((
            (s1, s2),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(100, prt_docstr=True)
