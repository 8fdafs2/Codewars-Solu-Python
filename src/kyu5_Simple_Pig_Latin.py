import re


class Solution():
    """
    https://www.codewars.com/kata/520b9d2ad5c005041100000f

    Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    """

    def __init__(self):
        pass

    def pig_it_01(self, text):
        """
        intuitive
        """
        ret = []
        for word in text.split():
            if word not in '!?.':
                ret.append(word[1:] + word[0] + 'ay')
            else:
                ret.append(word)

        return ' '.join(ret)

    def pig_it_02(self, text):
        """
        regex
        """
        return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.IGNORECASE)

    def pig_it_03(self, text):
        """
        regex
        """
        return re.sub(r'(\w)(\w*)', r'\g<2>\g<1>ay', text)

    def pig_it_04(self, text):
        """
        isalpha
        """
        return ' '.join([
            w[1:] + w[0] + 'ay' if w.isalpha() else w for w in text.split()
        ])

def sets_gen(pig_it):
    import random

    def word_gen():
        return random.choice([
            ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(1, 8))]),
            random.choice('!?.')
        ])

    test_sets = []
    for i in range(1, 200):
        text = ' '.join([word_gen() for _ in range(i)])
        match = pig_it(text)
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
