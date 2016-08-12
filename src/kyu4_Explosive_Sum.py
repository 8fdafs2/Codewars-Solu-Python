class Solution():
    """
    https://www.codewars.com/kata/explosive-sum

    How many ways can you make the sum of a number?

    From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

        In number theory and combinatorics, a partition of a positive integer n,
        also called an integer partition, is a way of writing n as a sum of positive integers.
        Two sums that differ only in the order of their summands are considered the same partition.
        If order matters, the sum becomes a composition.
        For example, 4 can be partitioned in five distinct ways:

        4
        3 + 1
        2 + 2
        2 + 1 + 1
        1 + 1 + 1 + 1

    Examples

        Trivial

            sum(-1) # 0
            sum(1) # 1

        Basic

            sum(2) # 2  -> 1+1 , 2
            sum(3) # 3 -> 1+1+1, 1+2, 3
            sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
            sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

            sum(10) # 42

        Explosive

            sum(50) # 204226
            sum(80) # 15796476
            sum(100) # 190569292

    See here (http://www.numericana.com/data/partition.htm) for more examples.
    """

    def __init__(self):
        pass

    def exp_sum_01(self, n):
        """
        p(n, m) = sum(p(n-k, k)), k={1...m}
        recursion
        """
        def recur(n, m):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if m > n:
                m = n
            ret = 0
            for k in range(1, m + 1):
                ret += recur(n - k, k)
            return ret

        return recur(n, n)

    def exp_sum_02(self, n):
        """
        p(n, m) = sum(p(n-k, k)), k={1...m}
        recursion, hashtab
        """
        hashtab = {(0, 0): 1}

        def recur(n, m):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if m > n:
                m = n
            if (n, m) in hashtab:
                return hashtab[(n, m)]
            ret = 0
            for k in range(1, m + 1):
                ret += recur(n - k, k)
            hashtab[(n, m)] = ret
            return ret

        return recur(n, n)

    def exp_sum_03(self, n):
        """
        pk(n) = pk-1(n) + pk(n-k)
        recursion
        """

        def recur(n, k):
            if n == 0:
                return 1
            if n < 0 or k == 0:
                return 0
            if k > n:
                k = n
            return recur(n, k - 1) + recur(n - k, k)

        return recur(n, n)

    def exp_sum_04(self, n):
        """
        pk(n) = pk-1(n) + pk(n-k)
        recursion, hashtab
        """
        hashtab = {(0, 0): 1}

        def recur(n, k):
            if n == 0:
                return 1
            if n < 0 or k == 0:
                return 0
            if k > n:
                k = n
            if (n, k) in hashtab:
                return hashtab[(n, k)]

            hashtab[(n, k)] = ret = recur(n - k, k) + recur(n, k - 1)
            return ret

        return recur(n, n)

    def exp_sum_05(self, n):
        """
        pk(n) = pk-1(n) + pk(n-k)
        recursion by for-loop via list
        """
        if n < 0:
            return 0
        dp = [1] + [0] * n
        for num in range(1, n + 1):
            for i in range(num, n + 1):
                # pk(n) = pk-1(n) + pk(n-k)
                # pk(n) is the number of partitions of n in which the largest part has at most size k
                dp[i] += dp[i - num]
        return dp[-1]

    def exp_sum_06(self, n):
        """
        formula, hashtab
        """
        hashtab = {0: 1,}

        def recur(n):
            if n < 0:
                return 0
            if n in hashtab:
                return hashtab[n]
            ret = 0
            sign = 1
            for k in range(1, n + 1):
                tmp = 3 * k * k
                ret += sign * (recur(n - ((tmp - k) >> 1)) + recur(n - ((tmp + k) >> 1)))
                sign = -sign
            hashtab[n] = ret
            return hashtab[n]

        return recur(n)


def sets_gen(exp_sum):
    test_sets = []
    for n in range(0, 31):
        match = exp_sum(n)
        test_sets.append((
            (n,),
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
