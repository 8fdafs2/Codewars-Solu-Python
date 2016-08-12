class Solution():
    """
    https://www.codewars.com/kata/55c45be3b2079eccff00010f

    Your task is to sort a given string.
    Each word in the String will contain a single number.
    This number is the position the word should have in the result.

    Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

    If the input String is empty, return an empty String.
    The words in the input String will only contain valid consecutive numbers.

    For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

    """
    def __init__(self):
        pass

    def order_01(self, sentence):
        """
        intuitive
        """
        if not sentence:
            return ''
        hashtab = {}
        for word in sentence.split():
            for letter in word:
                if letter in '123456789':
                    hashtab[letter] = word
                    break
        ret = []
        for letter in '123456789':
            if letter in hashtab:
                ret.append(hashtab[letter])

        return ' '.join(ret)

    def order_02(self, sentence):
        """
        sort word to place the digit first
        """
        if not sentence:
            return ''
        hashtab = {}
        for word in sentence.split():
            hashtab[sorted(word)[0]] = word
        ret = []
        for letter in '123456789':
            try:
                ret.append(hashtab[letter])
            except KeyError:
                break

        return ' '.join(ret)

    def order_03(self, sentence):
        """
        sort word to place the digit first
        """
        if not sentence:
            return ''
        words = sentence.split()
        ret = [''] * len(words)
        for word in words:
            ret[int(sorted(word)[0])-1] = word
        return ' '.join(ret)


    def order_04(self, sentence):
        """
        sort word to place the digit first
        """
        if not sentence:
            return ''
        return ' '.join(sorted(sentence.split(), key=lambda word: sorted(word)))


def sets_gen(order):
    import random
    test_sets = []
    for i in range(2, 11):
        senctence = []
        for j in range(1, i):
            letters = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(4, 8))]
            letters[random.randint(0, len(letters) - 1)] = str(j)
            senctence.append(''.join(letters))
        random.shuffle(senctence)
        senctence = ' '.join(senctence)
        match = order(senctence)
        test_sets.append((
            (senctence,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10000, prt_docstr=True)
