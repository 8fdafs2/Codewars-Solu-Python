import re


class Solution():
    """
    """

    def __init__(self):
        pass

    @staticmethod
    def to_underscore_01(string):
        """
        intuitive
        """
        if isinstance(string, int):
            return str(string)

        ret = string[0].lower()
        for c in string[1:]:
            if c.isupper():
                ret += '_' + c.lower()
                continue
            ret += c
        return ret

    @staticmethod
    def to_underscore_02(string):
        """
        regex
        """
        if isinstance(string, int):
            return str(string)

        def func(m):
            if m.group(1):
                return m.group(1).lower()
            return '_' + m.group(2).lower()

        return re.sub(r'(^[A-Z])|([A-Z])', func, string)

    @staticmethod
    def to_underscore_03(string):
        """
        regex
        """
        if isinstance(string, int):
            return str(string)

        return re.sub(r'([A-Z])', r'_\1', string)[1:].lower()

    @staticmethod
    def to_underscore_04(string):
        """
        regex
        """
        if isinstance(string, int):
            return str(string)

        return re.sub("(?<=.)(?=[A-Z])", "_", string).lower()


def sets_gen(to_underscore):
    import random
    letters_lc = 'abcdefghijklmnopqrstuvwxyz0123456789'
    letters_uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = letters_lc + letters_uc
    test_sets = []
    for i in range(6, 1000):
        if random.choice((True, False)):
            string = random.choice(letters_uc) + ''.join([random.choice(letters) for _ in range(i - 1)])
        else:
            string = random.randint(0, 9)
        match = to_underscore(string)
        test_sets.append((
            (string,),
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
