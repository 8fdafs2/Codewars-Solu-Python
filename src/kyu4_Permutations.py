from itertools import permutations as perms

class Solution():
    """
    https://www.codewars.com/kata/5254ca2719453dcc0b00027d

    In this kata you have to create all permutations of an input string and remove duplicates, if present.
    This means, you have to shuffle all letters from the input in all possible orders.

    Examples:

    permutations('a'); # ['a']
    permutations('ab'); # ['ab', 'ba']
    permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

    The order of the permutations doesn't matter.
    """

    def __init__(self):
        pass

    def permutations_01(self, string):
        """
        itertools.permutations
        """
        return sorted([''.join(p) for p in set(perms(string))])

    def permutations_02(self, string):
        """
        recursion, global list update
        """
        ret = []

        def recur(header, string):
            if len(string) == 1:
                ret.append(header + string)
                return

            for c in set(string):
                i = string.index(c)
                recur(header + c, string[:i] + string[i + 1:])

        recur('', string)

        return sorted(ret)

    def permutations_03(self, string):
        """
        recursion, returned list
        """
        def recur(string):
            if len(string) == 1:
                return [string, ]

            ret = []
            for c in set(string):
                i = string.index(c)
                ret += [c + p for p in recur(string[:i] + string[i + 1:])]

            return ret

        return sorted(recur(string))

    def permutations_04(self, string):
        """
        recursion, brute force, set every time
        """
        def recur(string):
            len_string = len(string)
            if len_string == 1:
                return set(string)

            c = string[-1]
            ps = recur(string[:-1])

            return set([p[:i] + c + p[i:] for p in ps for i in range(len_string)])

        return sorted(recur(string))

    def permutations_05(self, string):
        """
        recursion, brute force, set at end only
        """
        def recur(string):
            len_string = len(string)
            if len_string == 1:
                return [string, ]

            c = string[-1]
            ps = recur(string[:-1])

            return [p[:i] + c + p[i:] for p in ps for i in range(len_string)]

        return sorted(set(recur(string)))


def sets_gen(permutations):
    import random
    test_sets = []
    for i in range(1, 10):
        string = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(i)])
        match = permutations(string)
        test_sets.append((
            (string,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
