class Solution():
    """
    https://www.codewars.com/kata/weight-for-weight

    My friend John and I are members of the "Fat to Fit Club (FFC)".
    John is worried because each month a list with the weights of members is published and
    each month he is the last on the list which means he is the heaviest.

    I am the one who establishes the list so I told him: "Don't worry any more,
    I will modify the order of the list". It was decided to attribute a "weight" to numbers.
    The weight of a number will be from now on the sum of its digits.

    For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
    Given a string with the weights of FFC members in normal order can you give
    this string ordered by "weights" of these numbers?

    Example:

    a = "56 65 74 100 99 68 86 180 90"ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

    When two numbers have the same "weight", let us class them as if they were strings and not numbers:
    100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since,
    having the same "weight" (9) it comes before as a string.

    All numbers in the list are positive numbers and the list can be empty.
    """

    def __init__(self):
        pass

    def order_weight_01(self, strng):
        """
        sort by (sum, string)
        """
        weights = strng.split()

        def weight_get(number):
            number = str(number)
            return sum([int(d) for d in number]), number

        weights.sort(key=weight_get)

        return ' '.join(weights)

    def order_weight_02(self, strng):
        """
        sort by string, sort by sum
        """
        weights = strng.split()

        def weight_get(number):
            return sum([int(d) for d in str(number)])

        weights.sort()
        weights.sort(key=weight_get)

        return ' '.join(weights)


def sets_gen(order_weight):
    import random
    test_sets = []
    for i in range(3, 501):
        strng = ' '.join(str(random.randint(1, 100000)) for _ in range(i))
        match = order_weight(strng)
        test_sets.append((
            (strng,),
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
