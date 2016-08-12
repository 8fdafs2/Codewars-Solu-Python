class Solution():
    """
    https://www.codewars.com/kata/multiples-of-3-and-5

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

    Courtesy of ProjectEuler.net
    """
    def __init__(self):
        pass

    def solution_01(self, number):
        """
        regular pattern
        """
        number -= 1
        n_3 = number // 3
        n_5 = number // 5
        n_15 = number // 15
        return (n_3 * (1 + n_3) * 3 +
                n_5 * (1 + n_5) * 5 -
                n_15 * (1 + n_15) * 15) >> 1

    def solution_02(self, number):
        """
        brute force
        """
        number -= 1
        ret = 0
        while number > 2:
            if number % 3 == 0 or number % 5 == 0:
                ret += number
            number -= 1
        return ret

    def solution_03(self, number):
        """
        brute force
        """
        return sum([i if i % 3 == 0 or i % 5 == 0 else 0 for i in range(3, number)])

    def solution_04(self, number):
        """
        brute force
        """
        return sum([i for i in range(3, number) if i % 3 == 0 or i % 5 == 0])


def sets_gen(solution):
    import random
    test_sets = []
    for i in range(1000):
        number = random.randint(0, 100)
        match = solution(number)
        test_sets.append((
            (number,),
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