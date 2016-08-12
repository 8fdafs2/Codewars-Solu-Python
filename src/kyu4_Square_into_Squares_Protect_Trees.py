from math import sqrt


class Solution():
    """
    https://www.codewars.com/kata/54eb33e5bc1a25440d000891

    My little sister came back home from school with the following task:
    given a squared sheet of paper she has to cut it in pieces which,
    when assembled, give squares the sides of which form an increasing sequence of numbers.
    At the beginning it was lot of fun but little by little we were tired of seeing the pile of torn paper.
    So we decided to write a program that could help us and protects trees.

    Task

    Given a positive integral number n,
    return a strictly increasing sequence (list/array/string depending on the language) of numbers,
    so that the sum of the squares is equal to n².

    If there are multiple solutions (and there will be),
    return the result with the largest possible values:

    Examples

    decompose(11) must return [1,2,4,10].
    Note that there are actually two ways to decompose 11²,
    11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

    For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49]
    since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

    Note

    Neither [n] nor [1,1,1,…,1] are valid solutions.
    If no valid solution exists, return nil, null, Nothing, None or "" (Java, C#) or {} (C++).

    The function "decompose" will take a positive integer n and return the decomposition of N = n² as:

    [x1 ... xk]

    Hint

    Very often xk will be n-1.
    """

    def __init__(self):
        pass

    def decompose_01(self, n):
        """
        calc pow 2 whenever needed
        """
        def recur(a, i):
            if a == 0:
                return []
            if a < 0:
                return
            for x in range(i - 1, 0, -1):
                ret = recur(a - x * x, x)
                if ret is not None:
                    return ret + [x, ]

        return recur(n * n, n)

    def decompose_02(self, n):
        """
        calc and cache pow 2 whenever needed
        """
        a_dct = {}

        def recur(a, i):
            if a == 0:
                return []
            if a < 0:
                return
            for x in range(i - 1, 0, -1):
                if x not in a_dct:
                    a_dct[x] = x * x
                ret = recur(a - a_dct[x], x)
                if ret is not None:
                    return ret + [x, ]

        return recur(n * n, n)

    def decompose_03(self, n):
        """
        pre-calc all pow 2 in hashtab
        """
        n_a_lst = n - 1
        a_dct = {x: x * x for x in range(n_a_lst, 0, -1)}

        def recur(a, i):
            if a == 0:
                return []
            if a < 0:
                return
            for x in range(i - 1, 0, -1):
                ret = recur(a - a_dct[x], x)
                if ret is not None:
                    return ret + [x, ]

        return recur(n * n, n)

    def decompose_04(self, n):
        """
        pre-calc all pow 2 then calc sqrt at end
        """
        n_a_lst = n - 1
        a_lst = [x * x for x in range(n_a_lst, 0, -1)]

        def recur(a, i):
            if a == 0:
                return []
            if a < 0:
                return
            for j in range(i, n_a_lst):
                a_ = a_lst[j]
                ret_ = recur(a - a_, j + 1)
                if ret_ is not None:
                    return ret_ + [a_, ]

        ret = recur(n * n, 0)
        if ret:
            return [sqrt(a) for a in ret]

    # def decompose_02(self, n):
    #     """
    #     """
    #     a_lst = [x * x for x in range(n - 1, 0, -1)]
    #
    #     a_start = n * n
    #
    #     n_a = n - 1
    #
    #     for i in range(n_a - 1):
    #         ret = [a_lst[i], ]
    #         a = a_start - ret[-1]
    #         for j in range(i + 1, n_a):
    #             a_ = a_lst[j]
    #             if a == a_:
    #                 return [sqrt(a_), ] + [sqrt(a) for a in ret][::-1]
    #             if a > a_:
    #                 a -= a_
    #                 ret.append(a_)



def sets_gen(decompose):
    test_sets = []
    for n in range(1, 200):
        match = decompose(n)
        test_sets.append((
            (n,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    #
    # print(sol.decompose_02(50))
    #
    # exit()

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
