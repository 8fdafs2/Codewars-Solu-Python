# 1 <= n <= 1000000000

# 5x2^(n-1)
# ---------------------------------------------
# n=1 :: 5x2^(1-1)=5
# ABCDE
# n=2 :: 5x2^(2-1)=10
# AABBCCDDEE
# n=3 :: 5x2^(3-1)=20
# AAAABBBBCCCCDDDDEEEE
# n=4 :: 5x2^(4-1)=40
# AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEE
# n=5 :: 5x2^(5-1)=80
# AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEE
# ......

# sum = 5xSn = 5x(1 + 2 + 4 + 8 + 16 + ... + n) = 5x(2**n - 1)
# ---------------------------------------------
# sum = 5xS1 = 5x1
# sum = 5xS2 = 5x3
# sum = 5xS3 = 5x7
# sum = 5xS4 = 5x15
# sum = 5xS5 = 5x31
# ......

import math


class Solution():
    """
    https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0

    Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine;
    there are no other people in the queue.
    The first one in the queue (Sheldon) buys a can, drinks it and doubles!
    The resulting two Sheldons go to the end of the queue.
    Then the next in the queue (Leonard) buys a can,
    drinks it and gets to the end of the queue as two Leonards, and so on.

    For example, Penny drinks the third can of cola and the queue will look like this:

    Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny

    Write a program that will return the name of a man who will drink the n-th cola.

    Note that in the very beginning the queue looks like that:

    Sheldon, Leonard, Penny, Rajesh, Howard

    Input

    The input data consist of an array which contains five names, and single integer n.

    (1 ≤ n ≤ 1000000000).

    Output / Examples

    Return the single line — the name of the person who drinks the n-th can of cola.
    The cans are numbered starting from 1.
    Please note that you should spell the names like this:
    "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" (without the quotes).
    In that order precisely the friends are in the queue initially.

    whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1)=="Sheldon"
    whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52)=="Penny"
    whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951)=="Leonard"
    """
    def __init__(self):
        pass

    def whoIsNext_01(self, names, r):
        """
        math
        """
        n = len(names)
        k = 2 ** int(math.log(r // n + 1, 2))
        s = r - n * (k - 1) - 1
        return names[s // k]

    def whoIsNext_02(self, names, r):
        """
        step-by-step
        """
        queue = [[name, 1] for name in names]
        while queue[0][1] < r:
            r -= queue[0][1]
            queue[0][1] <<= 1
            queue.append(queue.pop(0))
        return queue[0][0]

    def whoIsNext_03(self, names, r):
        """
        math
        """
        n = len(names)
        while r > n:
            r = (r - n + 1) >> 1
        return names[r - 1]


def sets_gen(whoIsNext):
    test_sets = []
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    for r in range(1, 10001):
        match = whoIsNext(names, r)
        test_sets.append((
            (names, r),
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
