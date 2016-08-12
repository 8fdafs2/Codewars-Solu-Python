import itertools


class Solution():
    """
    https://www.codewars.com/kata/54d81488b981293527000c8f

    Sum of Pairs

    Given a list of integers and a single sum value,
    return the first two values (parse from the left please) in order of appearance that add up to form the sum.

    sum_pairs([11, 3, 7, 5],         10)
    #              ^--^      3 + 7 = 10
    == [3, 7]

    sum_pairs([4, 3, 2, 3, 4],         6)
    #          ^-----^         4 + 2 = 6, indices: 0, 2 *
    #             ^-----^      3 + 3 = 6, indices: 1, 3
    #                ^-----^   2 + 4 = 6, indices: 2, 4
    #  * entire pair is earlier, and therefore is the correct answer
    == [4, 2]

    sum_pairs([0, 0, -2, 3], 2)
    #  there are no pairs of values that can be added to produce 2.
    == None/nil/undefined (Based on the language)

    sum_pairs([10, 5, 2, 3, 7, 5],         10)
    #              ^-----------^   5 + 5 = 10, indices: 1, 5
    #                    ^--^      3 + 7 = 10, indices: 3, 4 *
    #  * entire pair is earlier, and therefore is the correct answer
    == [3, 7]

    Negative numbers and duplicate numbers can and will appear.

    NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements.
    Be sure your code doesn't time out.
    """
    def __init__(self):
        pass

    def sum_pairs_01(self, ints, s):
        """
        left to right, intuitive
        """
        rng = list(range(len(ints)))
        for i in rng[1:]:
            int2expect = s - ints[i]
            for j in rng[:i]:
                if ints[j] == int2expect:
                    return [int2expect, ints[i]]

    def sum_pairs_02(self, ints, s):
        """
        right to left, intuitive
        """
        ret = []
        rng = list(range(len(ints)))
        for i in rng[::-1]:
            int2expect = s - ints[i]
            for j in rng[:i]:
                if ints[j] == int2expect:
                    ret = [int2expect, ints[i]]
        if ret:
            return ret

    def sum_pairs_03(self, ints, s):
        """
        searched cache by dict(hashed)
        """
        ints_dict = {}
        for i in range(len(ints)):
            int2expect = s - ints[i]
            if int2expect in ints_dict:
                return [int2expect, ints[i]]
            ints_dict[ints[i]] = None

    def sum_pairs_04(self, ints, s):
        """
        searched cache by set(hashed)
        """
        ints_set = set()
        for i in range(len(ints)):
            int2expect = s - ints[i]
            if int2expect in ints_set:
                return [int2expect, ints[i]]
            ints_set.add(ints[i])

    def sum_pairs_05(self, ints, s):
        """
        searched cache by list
        """
        ints_set = []
        for i in range(len(ints)):
            int2expect = s - ints[i]
            if int2expect in ints_set:
                return [int2expect, ints[i]]
            ints_set.append(ints[i])

    def sum_pairs_06(self, ints, s):
        """
        itertools.combinations
        """
        for int_02, int_01 in list(itertools.combinations(ints[::-1], 2))[::-1]:
            if int_02 + int_01 == s:
                return [int_01, int_02]


def sets_gen(sum_pairs):
    import random
    test_sets = []
    rng = list(range(-800, 801))
    for i in range(3, 201):
        ints = random.sample(rng, i)
        s = sum(random.sample(ints, 2))
        match = sum_pairs(ints, s)
        test_sets.append((
            (ints, s),
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
