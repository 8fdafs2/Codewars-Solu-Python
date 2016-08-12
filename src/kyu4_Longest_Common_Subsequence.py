import pprint


class Solution():
    """
    https://www.codewars.com/kata/52756e5ad454534f220001ef

    Write a function called LCS that accepts two sequences,
    and returns the longest subsequence common to the passed in sequences.

    Subsequence

        A subsequence is different from a substring.
        The terms of a subsequence need not be consecutive terms of the original sequence.

    Example subsequence

        Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc"

    LCS examples

        lcs( "abcdef" , "abc" ) => returns "abc"
        lcs( "abcdef" , "acf" ) => returns "acf"
        lcs( "132535365" , "123456789" ) => returns "12356"

    Notes

        Both arguments will be strings
        Return value must be a string
        Return an empty string if there exists no common subsequence
        Both arguments will have one or more characters (in JavaScript)
        All tests will only have a single longest common subsequence.
        Don't worry about cases such as LCS( "1234", "3412" ),
        which would have two possible longest common subsequences: "12" and "34".

    Note that the Haskell variant will use randomized testing,
    but any longest common subsequence will be valid.

    Tips

        Wikipedia has an explanation of the two properties that can be used to solve the problem:

            First property
            Second property
    """

    def __init__(self):
        pass

    def lcs_01(self, x, y):
        """
        table memorization, all-in-one
        """
        n_x = len(x)
        n_y = len(y)
        tab = [[''] * (n_y + 1) for _ in range(n_x + 1)]
        for i in range(n_x):
            for j in range(n_y):
                if x[i] == y[j]:
                    tab[i][j] = tab[i - 1][j - 1] + x[i]
                else:
                    if len(tab[i][j - 1]) > len(tab[i - 1][j]):
                        tab[i][j] = tab[i][j - 1]
                    else:
                        tab[i][j] = tab[i - 1][j]
        return tab[-2][-2]

    def lcs_02(self, x, y):
        """
        table memorization, tab-fill then back-track
        """
        n_x = len(x)
        n_y = len(y)
        tab = [[0] * (n_y + 1) for _ in range(n_x + 1)]

        def tab_fill():
            for i in range(n_x):
                for j in range(n_y):
                    if x[i] == y[j]:
                        tab[i][j] = tab[i - 1][j - 1] + 1
                    else:
                        tab[i][j] = max(tab[i][j - 1], tab[i - 1][j])

        tab_fill()

        def back_track(i, j):
            if i < 0 or j < 0:
                return ''
            elif x[i] == y[j]:
                return back_track(i - 1, j - 1) + x[i]
            if tab[i][j - 1] > tab[i - 1][j]:
                return back_track(i, j - 1)
            return back_track(i - 1, j)

        return back_track(n_x - 1, n_y - 1)

    # def lcs_03(self, x, y):
    #     """
    #     recursion, no memorization, pass string <- just way too slow
    #     """
    #     def recur(x, y):
    #         if (not x) or (not y):
    #             return ''
    #         if x[-1] == y[-1]:
    #             return recur(x[:-1], y[:-1]) + x[-1]
    #         # return max(recur(x, y[:-1]), recur(x[:-1], y))
    #         ret_x = recur(x, y[:-1])
    #         ret_y = recur(x[:-1], y)
    #         if len(ret_x) > len(ret_y):
    #             return ret_x
    #         return ret_y

    #     return recur(x, y)

    def lcs_04(self, x, y):
        """
        recursion, table memorization, pass index, tab
        """
        n_x = len(x)
        n_y = len(y)
        tab = [[None] * (n_y + 1) for _ in range(n_x + 1)]

        def recur(i, j):
            if tab[i][j] is not None:
                return tab[i][j]
            if (i < 0) or (j < 0):
                tab[i][j] = t = ''
                return t
            if x[i] == y[j]:
                tab[i][j] = t = recur(i - 1, j - 1) + x[i]
                return t
            # return max(recur(i, j - 1), recur(i - 1, j))
            ret_x = recur(i, j - 1)
            ret_y = recur(i - 1, j)
            if len(ret_x) > len(ret_y):
                tab[i][j] = t = ret_x
                return t
            tab[i][j] = t = ret_y
            return t

        return recur(len(x) - 1, len(y) - 1)

    def lcs_05(self, x, y):
        """
        itertools.combinations, set.intersection <- just way too slow
        """
        from itertools import combinations
        range_x = list(range(len(x) + 1))
        range_y = list(range(len(y) + 1))
        subsequences_x = set(''.join(c) for i in range_x for c in combinations(x, i))
        subsequences_y = set(''.join(c) for i in range_y for c in combinations(y, i))
        return max(subsequences_x.intersection(subsequences_y), key=len)


def sets_gen(lcs):
    import random
    letters = 'abcdefghijkl'
    test_sets = []
    for i in range(8, 16 + 1):
        x = ''.join([random.choice(letters) for _ in range(random.randint(i - 2, i + 2))])
        y = ''.join([random.choice(letters) for _ in range(random.randint(i - 2, i + 2))])
        match = lcs(x, y)
        test_sets.append((
            (x, y),
            match
        ))
    return test_sets


def cmpr(to_match, test_set):
    args, match = test_set
    if match == to_match:
        return True
    if len(to_match) != len(match):
        return False
    x, y = args
    i_x = -1
    i_y = -1
    try:
        for i in range(len(match)):
            e = match[i]
            i_x = x[i_x + 1:].index(e)
            i_y = y[i_y + 1:].index(e)
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen, cmpr)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1, prt_docstr=True)
