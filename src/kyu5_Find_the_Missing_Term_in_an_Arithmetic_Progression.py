class Solution():
    """
    https://www.codewars.com/kata/find-the-missing-term-in-an-arithmetic-progression

    An Arithmetic Progression is defined as one in which there is a constant difference between
    the consecutive terms of a given series of numbers. You are provided with consecutive elements of
    an Arithmetic Progression.
    There is however one hitch: Exactly one term from the original series is missing from the set of numbers which
    have been given to you.
    The rest of the given series is the same as the original AP. Find the missing term.

    You have to write the function findMissing (list) , list will always be at least 3 numbers.

    Example :

    findMissing([1,3,5,9,11]) # => 7
    PS: This is a sample question of the facebook engineer challenge on interviewstreet.
    I found it quite fun to solve on paper using math, derive the algo that way. Have fun!
    """

    def __init__(self):
        pass

    @staticmethod
    def find_missing_01(sequence):
        """
        diff_old, diff
        """
        diff_old = sequence[1] - sequence[0]
        for i in range(1, len(sequence) - 1):
            diff = sequence[i + 1] - sequence[i]
            if diff == diff_old + diff_old:
                return sequence[i] + diff_old
            elif diff + diff == diff_old:
                return sequence[i] - diff
            diff_old = diff

    @staticmethod
    def find_missing_02(sequence):
        """
        diff
        """
        diff = (sequence[-1] - sequence[0]) // len(sequence)
        for i in range(0, len(sequence) - 1):
            if sequence[i + 1] - sequence[i] != diff:
                return sequence[i] + diff

    @staticmethod
    def find_missing_03(sequence):
        """
        math
        """
        return (sequence[0] + sequence[-1]) * (len(sequence) + 1) // 2 - sum(sequence)


def sets_gen(find_missing):
    import random
    diffs = list(range(-10, 0, 1)) + list(range(10, 0, -1))
    test_sets = []
    for i in range(4, 1000):
        diff = random.choice(diffs)
        start = random.randint(-10, 10)
        sequence = [start + diff * j for j in range(i)]
        sequence.pop(random.randint(0, i - 1))
        match = find_missing(sequence)
        test_sets.append((
            (sequence,),
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
