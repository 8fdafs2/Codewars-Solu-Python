from collections import deque
from queue import PriorityQueue


class Solution():
    """
    https://www.codewars.com/kata/5672682212c8ecf83e000050

    Consider a sequence u where u is defined as follows:

        The number u(0) = 1 is the first one in u.
        For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
        There are no other numbers in u.

    Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

    1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

    Task:

        Given parameter n the function dbl_linear (or dblLinear...)
        returns the element u(n) of the ordered (with <) sequence u.

    Example:

        dbl_linear(10) should return 22

    Note:

        Focus attention on efficiency
    """
    def __init__(self):
        pass

    def dbl_linear_01(self, n):
        """
        same as hamming num Dijkstra’s paper, reliable
        """
        nums = [1, ]
        i2 = i3 = 0

        for _ in range(n):
            num_i2 = nums[i2] * 2 + 1
            num_i3 = nums[i3] * 3 + 1
            num = num_i2 if num_i2 < num_i3 else num_i3
            nums.append(num)
            if num == num_i2:
                i2 += 1
            if num == num_i3:
                i3 += 1

        return nums[-1]

    def dbl_linear_02(self, n):
        """
        deque, reliable
        """
        ret = 1
        q2, q3 = deque(), deque()
        while True:
            if 0 >= n:
                return ret
            q2.append(2 * ret + 1)
            q3.append(3 * ret + 1)
            ret = min(q2[0], q3[0])
            if ret == q2[0]:
                q2.popleft()
            if ret == q3[0]:
                q3.popleft()
            n -= 1

    def dbl_linear_03(self, n):
        """
        brute-force, non-reliable
        """
        seq = {1, }
        seq_last = [1, ]
        f1 = lambda x: 2 * x + 1
        f2 = lambda x: 3 * x + 1
        while n >= len(seq):
            seq_last = [f(x) for f in (f1, f2) for x in seq_last]
            seq.update(seq_last)
        seq_last = [f(x) for f in (f1, f2) for x in seq_last]
        seq.update(seq_last)
        seq_last = [f(x) for f in (f1, f2) for x in seq_last]
        seq.update(seq_last)
        seq_last = [f(x) for f in (f1, f2) for x in seq_last]
        seq.update(seq_last)
        return sorted(seq)[n]

    def dbl_linear_04(self, n):
        """
        brute-force, non-reliable
        """
        n_max = n * 9
        seq = [1, ]
        for i in seq:
            seq.append((i * 2) + 1)
            seq.append((i * 3) + 1)
            if len(seq) > n_max:
                break
        return sorted(set(seq))[n]

    def dbl_linear_05(self, n):
        """
        brute-force, queue.PriorityQueue, reliable
        """
        q = PriorityQueue()
        num = 1
        for _ in range(n):
            q.put_nowait(num * 2 + 1)
            q.put_nowait(num * 3 + 1)
            num_ = q.get_nowait()
            while num == num_:
                num_ = q.get_nowait()
            num = num_

        return num


def sets_gen(dbl_linear):
    import random
    test_sets = []
    for _ in range(10):
        n = random.randint(0, 10001)
        match = dbl_linear(n)
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
    tf.test_spd(10, prt_docstr=True)
