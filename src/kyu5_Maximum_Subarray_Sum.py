class Solution():
    """
    https://www.codewars.com/kata/maximum-subarray-sum

    The maximum sum subarray problem consists in finding
    the maximum sum of a contiguous subsequence in an array or list of integers:

    maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # should be 6: [4, -1, 2, 1]
    Easy case is when the list is made up of only positive numbers and
    the maximum sum is the sum of the whole array.
    If the list is made up of only negative numbers, return 0 instead.

    Empty list is considered to have zero greatest sum.
    Note that the empty list or array is also a valid sublist/subarray.

    """

    def __init__(self):
        pass

    @staticmethod
    def maxSequence_01(arr):
        """
        """
        if not arr:
            return 0

        # all negative number seq check
        # in this case it is supposed to be omitted
        nums_max = max(arr)
        if nums_max < 0:
            return nums_max

        sum_max_g = sum_max = 0
        for num in arr:
            if sum_max + num >= 0:
                sum_max += num
            else:
                sum_max = 0
            if sum_max > sum_max_g:
                sum_max_g = sum_max

        return sum_max_g

    @staticmethod
    def maxSequence_02(arr):
        """
        """
        lowest = ans = total = 0
        for i in arr:
            total += i
            lowest = min(lowest, total)
            ans = max(ans, total - lowest)
        return ans

    @staticmethod
    def maxSequence_03(arr):
        """
        """
        sum_max_g, sum_max = 0, 0
        for num in arr:
            sum_max += num
            if sum_max < 0:
                sum_max = 0
            if sum_max > sum_max_g:
                sum_max_g = sum_max
        return sum_max_g

    @staticmethod
    def maxSequence_04(arr):
        """
        """
        sum_max_g = sum_max = 0
        for num in arr:
            sum_max = max(0, sum_max + num)
            sum_max_g = max(sum_max_g, sum_max)
        return sum_max_g


def sets_gen(maxSequence):
    import random
    test_sets = []
    for i in range(10, 500):
        nums = [random.randint(-i, i) for _ in range(i)]
        match = maxSequence(nums)
        test_sets.append((
            (nums,),
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
