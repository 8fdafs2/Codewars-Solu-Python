from collections import deque
from collections import defaultdict
from bisect import insort
from heapq import merge
from itertools import product, tee, islice
from queue import PriorityQueue


class Solution():
    """
    https://www.codewars.com/kata/hamming-numbers

    A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

    Write a function that computes the nth smallest Hamming number.

    Specifically:

        The first smallest Hamming number is 1 = 2^0*3^0*5^0
        The second smallest Hamming number is 2 = 2^1*3^0*5^0
        The third smallest Hamming number is 3 = 2^0*3^1*5^0
        The fourth smallest Hamming number is 4 = 2^2*3^0*5^0
        The fifth smallest Hamming number is 5 = 2^0*3^0*5^1

    The 20 smallest Hamming numbers are given in example test fixture.

    Your code should be able to compute all of the smallest 5,000 (Clojure: 2000) Hamming numbers without timing out.

    """

    def __init__(self):
        pass

    def hamming_01(self, n):
        """
        Dijkstra’s paper, reliable
        """
        hs = [1, ]
        i2 = i3 = i5 = 0
        for _ in range(1, n):
            h_i2_2, h_i3_3, h_i5_5 = 2 * hs[i2], 3 * hs[i3], 5 * hs[i5]
            h = min(h_i2_2, h_i3_3, h_i5_5)
            hs.append(h)
            if h_i2_2 == h:
                i2 += 1
            if h_i3_3 == h:
                i3 += 1
            if h_i5_5 == h:
                i5 += 1
        return hs[-1]

    def hamming_02(self, n):
        """
        long list computed only once, non-reliable
        """
        if not hasattr(self, 'hs'):
            self.hs = sorted([2 ** i * 3 ** j * 5 ** k
                              for i, j, k in product(range(50), repeat=3)
                              ])

        return self.hs[n - 1]

    def hamming_03(self, n):
        """
        Dijkstra’s paper, reliable
        """
        bases = [2, 3, 5]
        expos = [0, 0, 0]
        hs = [1, ]
        rng3 = list(range(3))
        for _ in range(n - 1):
            next_hs = [bases[i] * hs[expos[i]] for i in rng3]
            next_h = min(next_hs)
            hs.append(next_h)
            for i in rng3:
                if next_hs[i] == next_h:
                    expos[i] += 1
        return hs[-1]

    def hamming_04(self, n):
        """
        lazy, reliable
        """
        def recur():
            last = 1
            yield last
            a, b, c = tee(recur(), 3)
            for n in merge((2 * i for i in a), (3 * i for i in b), (5 * i for i in c)):
                if n != last:
                    yield n
                    last = n

        return list(islice(recur(), n))[-1]

    # def hamming_05(self, n):
    #     """
    #     sequence merge, possibly reliable
    #     """
    #     que = PriorityQueue()
    #     h = 1
    #     for i in range(1, n):
    #         h2 = h + h
    #         h3 = h2 + h
    #         h5 = h3 + h2
    #         que.put_nowait(h2)
    #         que.put_nowait(h3)
    #         que.put_nowait(h5)
    #         while True:
    #             h_ = que.get_nowait()
    #             if h_ != h:
    #                 h = h_
    #                 break
    #
    #     return h

    # def hamming_xx(self, n):
    #     """
    #     brute-force % /
    #     """
    #     if n == 1:
    #         return 1
    #     n_h = 1
    #     h = 1
    #     while n_h < n:
    #         h += 1
    #         h_ = h
    #         while True:
    #             if h_ % 2 == 0:
    #                 h_ /= 2
    #                 if h_ % 3 == 0:
    #                     h_ /= 3
    #                     if h_ % 5 == 0:
    #                         h_ /= 5
    #             elif h_ % 3 == 0:
    #                 h_ /= 3
    #                 if h_ % 5 == 0:
    #                     h_ /= 5
    #             elif h_ % 5 == 0:
    #                 h_ /= 5
    #             else:
    #                 break
    #
    #         if h_ == 1:
    #             n_h += 1
    #
    #     return h


def sets_gen(hamming):
    test_sets = []
    for n in range(1, 1001):
        match = hamming(n)
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
    tf.test_spd(1, prt_docstr=True)
