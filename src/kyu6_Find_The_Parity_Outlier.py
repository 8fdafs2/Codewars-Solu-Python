class Solution():
    """
    https://www.codewars.com/kata/5526fc09a1bbd946250002dc

    You are given an array (which will have a length of at least 3,
    but could be very large) containing integers.
    The integers in the array are either entirely odd or entirely even except for a single integer N.
    Write a method that takes the array as an argument and returns N.

    For example:
    [2, 4, 0, 100, 4, 11, 2602, 36]
    Should return: 11
    [160, 3, 1719, 19, 11, 13, -21]
    Should return: 160
    """
    def __init__(self):
        pass

    def find_outlier_01(self, integers):
        """
        flag calculated by using first 3 integers then for-if
        """
        mod = sum([i % 2 for i in integers[: 3]])
        # mod=0 or 1: odd to search
        # mod=2 or 3: even to search
        mod = mod < 2
        for i in integers:
            if i % 2 == mod:
                return i

    def find_outlier_02(self, integers):
        """
        obtain the result of mod_2 for all integers
        """
        parity = [i % 2 for i in integers]

        return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

    def find_outlier_03(self, integers):
        """
        filter the even ones out of integers then use set boolean
        """
        even = [x for x in integers if x % 2 == 0]
        return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]

    def find_outlier_04(self, integers):
        """
        filter the even ones out of integers then use filter
        """
        even = [x for x in integers if x % 2 == 0]
        return even[0] if len(even) == 1 else filter(lambda x: x % 2 != 0, integers)[0]

    def find_outlier_05(self, integers):
        """
        bitwise, flag constructed by first 3 integers
        """
        bit = ((integers[0] & 1) + (integers[1] & 1) + (integers[2] & 1)) >> 1
        # bit=1 : even_to_search
        # bit=0 : odd_to_search
        for i in integers:
            if (i & 1) ^ bit:
                return i

    def find_outlier_06(self, integers):
        """
        bitwise, flag constructed by first integer
        """
        bit = integers[0] & 1
        if integers[1] & 1 != bit:
            return integers[integers[2] & 1 == bit]
        # bit=1 : even_to_search
        # bit=0 : odd_to_search
        for i in integers:
            if i & 1 != bit:
                return i

    def find_outlier_07(self, integers):
        """
        flag calculated by using first 3 integers then next
        """
        mod = sorted([i % 2 for i in integers[:3]])[1]
        # mod=1 : even_to_search
        # mod=0 : odd_to_search
        return next(i for i in integers if i % 2 != mod)

    def find_outlier_08(self, integers):
        """
        flag calculated by using first 3 integers then next, one-liner
        """
        return integers[0] \
            if integers[1] % 2 != integers[0] % 2 != integers[2] % 2 \
            else next(i for i in integers if i % 2 != integers[0] % 2)


def sets_gen(find_outlier):
    import random
    test_sets = []
    for i in range(3, 500):
        if random.choice((True, False)):
            integers = [random.randrange(0, 100, 2) for _ in range(i)]
            integers[random.randint(0, i - 1)] = random.randrange(1, 100, 2)
        else:
            integers = [random.randrange(1, 100, 2) for _ in range(i)]
            integers[random.randint(0, i - 1)] = random.randrange(0, 100, 2)
        match = find_outlier(integers)
        test_sets.append((integers, match))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture
    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(100, prt_docstr=True)