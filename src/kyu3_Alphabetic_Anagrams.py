from math import factorial
from collections import Counter
try:
    from functools import reduce
except ImportError:
    pass


class Solution():
    """
    https://www.codewars.com/kata/53e57dada0cb0400ba000688

    Consider a "word" as any sequence of capital letters A-Z (not limited to just "dictionary words").
    For any word with at least two different letters,
    there are other words composed of the same letters but in a different order
    (for instance, STATIONARILY/ANTIROYALIST, which happen to both be dictionary words;
    for our purposes "AAIILNORSTTY" is also a "word" composed of the same letters as these two).

    We can then assign a number to every word,
    based on where it falls in an alphabetically sorted list of all words made up of the same group of letters.
    One way to do this would be to generate the entire list of words and find the desired one,
    but this would be slow if the word is long.

    Given a word, return its number.
    Your function should be able to accept any word 25 letters or less in length (possibly with some letters repeated),
    and take no more than 500 milliseconds to run. To compare,
    when the solution code runs the 27 test cases in JS, it takes 101ms.

    For very large words,
    you'll run into number precision issues in JS (if the word's position is greater than 2^53).
    For the JS tests with large positions, there's some leeway (.000000001%).
    If you feel like you're getting it right for the smaller ranks,
    and only failing by rounding on the larger, submit a couple more times and see if it takes.

    Python, Java and Haskell have arbitrary integer precision,
    so you must be precise in those languages (unless someone corrects me).

    C# is using a long, which may not have the best precision, but the tests are locked so we can't change it.

    Sample words, with their rank:
    ABAB = 2
    AAAB = 1
    BAAA = 4
    QUESTION = 24572
    BOOKKEEPER = 10743
    """
    def __init__(self):
        pass

    def listPosition_01(self, word):
        """
        recursion, left to right, w/ explicit skip
        """
        def recur(word):
            # skip uncounted portion
            n = len(word)
            word_sorted = sorted(word)
            for i in range(n):
                if word[i] != word_sorted[i]:
                    break
            if i == n - 1:
                return 1  # return since no portion left to count

            # count
            n -= i
            word = word[i:]
            word_set = sorted(set(word))
            hashtab = {}
            for c in word:  # record frequencies
                hashtab[c] = hashtab.get(c, 0) + 1

            # formula: ret = fac(n-1) * sum(freq(c) for all c that is not the greatest) / product(freq(c) for all c)
            ret = factorial(n - 1) * sum([hashtab[c] for c in word_set[: word_set.index(word[0])]])
            div = 1
            for c_cnt in hashtab.values():
                div *= factorial(c_cnt)
            ret //= div
            return ret + recur(word[1:])

        return recur(word)

    def listPosition_02(self, word):
        """
        recursion, left to right, optimize
        """
        def recur(word):
            if not word:
                return 1
            # formula: ret = fac(n-1) * sum(freq(c) for all c that is not the greatest) / product(freq(c) for all c)
            ret = factorial(len(word) - 1) * sum(c < word[0] for c in word[1:])
            ret //= reduce(lambda a, n: a * factorial(n), Counter(word).values(), 1)
            return ret + recur(word[1:])

        return recur(word)

    def listPosition_03(self, word):
        """
        for-loop, right to left
        """
        n, ret, fac_div_prod = len(word), 1, 1
        cnts = Counter()

        for i in range(n):
            c = word[(n - 1) - i]
            cnts[c] += 1
            _sum_ = sum([cnts[_c_] for _c_ in cnts if _c_ < c])
            ret += fac_div_prod * _sum_ // cnts[c]
            fac_div_prod = fac_div_prod * (i + 1) // cnts[c]
        return ret


    def listPosition_04(self, word):
        """
        for-loop, right to left, boosted
        """
        n, ret, fac, div = len(word), 1, 1, 1
        cnts = {}
        for i in range(1, n + 1):
            c = word[-i]
            cnts[c] = cnts.get(c, 0) + 1
            _sum_ = 0
            for _c_ in cnts:
                if _c_ < c:
                    _sum_ += cnts[_c_]
            div *= cnts[c]
            ret += fac * _sum_ // div
            fac *= i
        return ret


def sets_gen(listPosition):
    import random
    import string
    test_sets = []
    for i in range(1, 51):
        word = ''.join([random.choice(string.ascii_uppercase) for _ in range(i)])
        match = listPosition(word)
        test_sets.append((
            (word,),
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
