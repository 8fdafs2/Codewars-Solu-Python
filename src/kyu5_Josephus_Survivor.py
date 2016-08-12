from functools import reduce


class Solution():
    """
    https://www.codewars.com/kata/555624b601231dc7a400017a

    In this kata you have to correctly return who is the "survivor",
    ie: the last element of a Josephus permutation.

    Basically you have to assume that n people are put into a circle and
    that they are eliminated in steps of k elements, like this:

    josephus_survivor(7,3) => means 7 people in a circle;
    one every 3 is eliminated until one remains
    [1,2,3,4,5,6,7] - initial sequence
    [1,2,4,5,6,7] => 3 is counted out
    [1,2,4,5,7] => 6 is counted out
    [1,4,5,7] => 2 is counted out
    [1,4,5] => 7 is counted out
    [1,4] => 5 is counted out
    [4] => 1 counted out, 4 is the last element - the survivor!
    The above link about the "base" kata description will give you a more thorough insight about
    the origin of this kind of permutation, but basically that's all that there is to know to solve this kata.

    Notes and tips: using the solution to the other kata to check your function may be helpful,
    but as much larger numbers will be used, using an array/list to compute the number of the survivor may be too slow;
    you may assume that both n and k will always be >=1.
    """

    def __init__(self):
        pass

    def josephus_survivor_01(self, n, k):
        """
        pop, loop
        """
        items = list(range(1, n + 1))

        i = 0
        while len(items) > 1:
            i = (i + k - 1) % len(items)
            items.pop(i)

        return items[0]

    def josephus_survivor_02(self, n, k):
        """
        1-base, loop
        """
        ret = 1
        for i in range(1, n + 1):
            ret = (ret + k - 1) % i + 1

        return ret

    def josephus_survivor_03(self, n, k):
        """
        0-base, loop
        """
        ret = 0
        for i in range(1, n + 1):
            ret = (ret + k) % i

        return ret + 1

    def josephus_survivor_04(self, n, k):
        """
        0-base, reduce
        """
        return reduce(lambda x, y: (x + k) % y, range(0, n + 1)) + 1

    def josephus_survivor_05(self, n, k):
        """
        1-base, recursion
        """

        def recur(n):
            if n == 1:
                return 1
            return (recur(n - 1) + k - 1) % n + 1

        return recur(n)

    def josephus_survivor_06(self, n, k):
        """
        0-base, recursion
        """

        def recur(n):
            if n == 0:
                return 0
            return (recur(n - 1) + k) % n

        return recur(n) + 1


def sets_gen(josephus_survivor):
    import random
    test_sets = []
    for n in range(3, 100):
        k = random.randint(1, n * 3)
        match = josephus_survivor(n, k)
        test_sets.append((
            (n, k),
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
