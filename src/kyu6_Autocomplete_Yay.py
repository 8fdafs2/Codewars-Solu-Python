import re


class Solution():
    """
    https://www.codewars.com/kata/5389864ec72ce03383000484

    It's time to create an autocomplete function! Yay!

    The autocomplete function will take in an input string and a dictionary array and
    return the values from the dictionary that start with the input string.
    If there are more than 5 matches, restrict your output to the first 5 results.
    If there are no matches, return an empty array.

    Example:

        autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']

    For this kata, the dictionary will always be a valid array of strings.
    Please return all results in the order given in the dictionary, even if they're not always alphabetical.
    The search should NOT be case sensitive, but the case of the word should be preserved when it's returned.

    For example, "Apple" and "airport" would both return for an input of 'a'. However,
    they should return as "Apple" and "airport" in their original cases.

    Important note:

        Any input that is NOT a letter should be treated as if it is not there. For example,
        an input of "$%^" should be treated as "" and an input of "ab*&1cd" should be treated as "abcd".

        (Thanks to wthit56 for the suggestion!)
    """

    def __init__(self):
        pass

    def autocomplete_01(self, input_, dictionary):
        """
        str.startswith
        """
        input_ = ''.join([c for c in input_.lower() if c.isalpha()])
        ret = []
        i = 0
        for key in dictionary:
            if key.lower().startswith(input_):
                ret.append(key)
                i += 1
                if i == 5:
                    return ret
        return ret

    def autocomplete_02(self, input_, dictionary):
        """
        str.find
        """
        input_ = ''.join([c for c in input_.lower() if c.isalpha()])
        ret = []
        i = 0
        for key in dictionary:
            if key.lower().find(input_) == 0:
                ret.append(key)
                i += 1
                if i == 5:
                    return ret
        return ret

    def autocomplete_03(self, input_, dictionary):
        """
        re.match
        """
        ret = []
        pat = re.compile(r'^' + re.escape(''.join([c for c in input_.lower() if c.isalpha()])), re.I)
        i = 0
        for key in dictionary:
            if pat.match(key):
                ret.append(key)
                i += 1
                if i == 5:
                    return ret
        return ret


def sets_gen(autocomplete):
    import random
    letters = 'abcdefghijklmnopqrstuvwxyz'
    others = '0123456789!@#$%^&*()_+'
    test_sets = []
    for i in range(5, 200):
        input_ = ''.join([random.choice(letters) for _ in range(1, 3)])
        dictionary = []
        for _ in range(i):
            if random.choice([True, False]):
                dictionary.append(input_ + ''.join([random.choice(letters) for _ in range(1, 3)]))
            else:
                dictionary.append(''.join([random.choice(letters) for _ in range(1, 6)]))
        input_ = list(input_) + [random.choice(others) for _ in range(0, 10)]
        random.shuffle(input_)
        input_ = ''.join(input_)
        match = autocomplete(input_, dictionary)
        test_sets.append((
            (input_, dictionary),
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