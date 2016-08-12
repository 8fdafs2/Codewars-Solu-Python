import re


class Solution():
    """
    https://www.codewars.com/kata/520446778469526ec0000001

    Complete the method (or function in Python) to return true
    when its argument is an array that has the same nesting structure as the first array.

    For example:

    # should return True
    same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
    same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

    # should return False
    same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
    same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

    # should return True
    same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

    # should return False
    same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

    For your convenience, there is already a function 'isArray(o)' declared in the JS version
    that returns true if its argument is an array, false otherwise.
    """

    def __init__(self):
        pass

    def same_structure_as_01(self, original, other):
        """
        recursion, ele-by-ele
        """
        if isinstance(original, list):
            if not isinstance(other, list):
                return False

        def same_stru_as(original, other):
            length = len(original)
            if length != len(other):
                return False
            for i in range(length):
                if isinstance(original[i], list):
                    if not isinstance(other[i], list):
                        return False
                    return same_stru_as(original[i], other[i])
            return True

        return same_stru_as(original, other)

    def same_structure_as_02(self, original, other):
        """
        stru by regex replace
        """
        pat = re.compile(r'\d+|\'.*?\'|\".*?\"')

        if pat.sub(r'', str(original)) != pat.sub(r'', str(other)):
            return False
        return True

    def same_structure_as_03(self, original, other):
        """
        stru by recursion reconstruction
        """

        def stru(x):
            if isinstance(x, list):
                return list(map(stru, x))
            return

        return stru(original) == stru(other)

    def same_structure_as_04(self, original, other):
        """
        stru by recursion ele-by-ele replace
        """

        def hashed(x):
            if isinstance(x, list):
                ret = '['
                for x_sub in x:
                    ret += hashed(x_sub)
                ret += ']'
                return ret
            return ' '

        return hashed(original) == hashed(other)


def sets_gen(same_structure_as):
    import random
    import copy
    test_sets = []

    eles = (1, 2, '[', ']')

    def randlst(length, depth):
        lst = [random.choice(eles) for _ in range(random.randint(0, length))]
        if depth:
            if len(lst) == 0:
                lst.append(randlst(length - 1, depth - 1))
            if len(lst) == 1:
                lst[0] = randlst(length - 1, depth - 1)
            else:
                for i in random.sample(list(range(len(lst))), random.randint(1, len(lst) - 1)):
                    lst[i] = randlst(length - 1, depth - 1)
        return lst

    def modilst(lst):
        for i in range(len(lst)):
            if isinstance(lst[i], list):
                modilst(lst[i])
            else:
                lst[i] = random.choice(eles)

    def struas(lst):
        lst = copy.deepcopy(lst)
        modilst(lst)
        return lst

    for i in range(2, 10):
        orig = randlst(i, i - 1)
        if random.choice((True, False)):
            othe = struas(orig)
        else:
            othe = randlst(i, i - 1)
        match = same_structure_as(orig, othe)

    test_sets.append((
        (orig, othe),
        match
    ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10000, prt_docstr=True)
