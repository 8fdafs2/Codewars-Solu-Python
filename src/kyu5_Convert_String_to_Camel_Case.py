import re

class Solution():
    """
    Complete the method/function so that it converts dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized only if the original word was capitalized.

    Examples:

    # returns "theStealthWarrior"
    to_camel_case("the-stealth-warrior")

    # returns "TheStealthWarrior"
    to_camel_case("The_Stealth_Warrior")
    """
    def __init__(self):
        pass

    def to_camel_case_01(self, text):
        """
        intuitive
        """
        if '_' in text:
            text = text.replace('_', '-')

        words = text.split('-')

        ret = [words[0], ]

        for w in words[1:]:
            ret.append(w.capitalize())

        return ''.join(ret)

    def to_camel_case_02(self, text):
        """
        regex
        """
        return re.sub('[-_]([a-z]*)', lambda m: m.group(1).capitalize(), text, flags=re.I)


def sets_gen(to_camel_case):
    import random
    letters = 'abcdefgABCDEFG'
    seps = '-_'
    test_sets = []
    for i in range(10, 100):
        text = []
        for j in range(i):
            word = [random.choice(letters) for _ in range(random.randint(2, 6))]
            if j < i - 1:
                word.append(random.choice(seps))
            text.append(''.join(word))
        text = ''.join(text)
        match = to_camel_case(text)
        test_sets.append((
            (text,),
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
