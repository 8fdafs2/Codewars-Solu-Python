class Solution():
    """
    https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

    Given an n x n array,
    return the array elements arranged from outermost elements to the middle element,
    traveling clockwise.

    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    snail(array) #=> [1,2,3,6,9,8,7,4,5]
    """

    def __init__(self):
        pass

    def snail_01(self, array):
        """
        intuitive solution
        """
        # array[0][0:n]
        # array[1][n-1] + ... + array[n-1][n-1]
        # array[n-1][0:n-1][::-1]
        # array[n-2][0] + ... + array[1][0]
        #
        # array[1][1:n-1]
        # array[2][n-2] + ... + array[n-2][n-2]
        # array[n-2][1:n-2][::-1]
        # array[n-3][1] + ... + array[2][1]
        n = len(array)
        ret = []
        k = 0
        while True:
            n_k = n - k
            ret += array[k][k:n_k]
            if 1 + k >= n_k:
                return ret
            ret += [array[i][n_k - 1] for i in range(1 + k, n_k)]
            ret += array[n_k - 1][k:n_k - 1][::-1]
            if n_k - 2 <= k:
                return ret
            ret += [array[i][k] for i in range(n_k - 2, k, -1)]
            k += 1

    def snail_02(self, array):
        """
        pop, zip and reverse
        """
        array = list(array)
        a = []
        while array:
            a += array.pop(0)
            array = list(zip(*array))
            array.reverse()
        return a

    def snail_03(self, array):
        """
        pop, zip and reverse in recursion form
        """
        ret = []

        def recur(array):
            if array:
                ret.extend(array[0])
                recur(list(zip(*array[1:]))[::-1])

        recur(array)
        return ret


def sets_gen(snail):
    def mat_gen(n):
        return [list(range(n * i, n * (i + 1))) for i in range(n)]

    test_set = []
    for i in range(2, 50):
        array = mat_gen(i)
        match = snail(array)
        test_set.append((
            (array,),
            match
        ))
    return test_set

if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture
    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(100, prt_docstr=True)
