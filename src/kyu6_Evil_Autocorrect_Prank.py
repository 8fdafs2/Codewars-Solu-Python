import re


class Solution():
    """
    https://www.codewars.com/kata/538ae2eb7a4ba8c99b000439

    Your friend won't stop texting his girlfriend. It's all he does. All day. Seriously.
    The texts are so mushy too! The whole situation just makes you feel ill.
    Being the wonderful friend that you are, you hatch an evil plot. While he's sleeping,
    you take his phone and change the autocorrect options
    so that every time he types "you" or "u" it gets changed to "your sister."

    Write a function called autocorrect that takes a string and replaces
    all instances of "you" or "u" (not case sensitive) with "your sister" (always lower case).
    Return the resulting string.

    Here's the slightly tricky part: These are text messages, so there are different forms of "you" and "u".

    For the purposes of this kata, here's what you need to support:
        "youuuuu" with any number of u characters tacked onto the end
        "u" at the beginning, middle, or end of a string, but NOT part of a word
        "you" but NOT as part of another word like youtube or bayou
    """

    def __init__(self):
        pass

    def autocorrect_01(self, input):
        """
        regex, scan twice
        """
        pat = re.compile(r'(^|[^a-z0-9_])(you+|u)([^a-z0-9_]|$)', re.I)

        return pat.sub('\\1your sister\\3', pat.sub('\\1your sister\\3', input))

    def autocorrect_02(self, input):
        """
        regex
        """
        return re.sub(r'\b(you+|u)\b', 'your sister', input, flags=re.I)


def sets_gen(autocorrect):
    import random
    marks = '.!?'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    words = ['u', 'you', 'you' + 'u' * random.randint(2, 5)]
    test_sets = []
    for i in range(1, 50):
        input = []
        for _ in range(i):
            if random.choice([True, False]):
                input.append(random.choice(words) + ''.join([random.choice(marks) for _ in range(0, 1)]))
            else:
                input.append(''.join([random.choice(letters) for _ in range(random.randint(0, 2))]) +
                             random.choice(words) +
                             ''.join([random.choice(letters) for _ in range(random.randint(0, 2))]))
        input = ' '.join(input)
        match = autocorrect(input)
        test_sets.append((
            (input,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=True)
