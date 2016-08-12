from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase, printable
from codecs import encode


class Solution():
    """
    https://www.codewars.com/kata/52223df9e8f98c7aa7000062

    How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

    I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
    According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

    Hint: For this task you're only supposed to substitue characters.
    Not spaces, punctuation, numbers etc.

    Test examples:

        Test.expect(rot13("EBG13 rknzcyr.") == "ROT13 example.");
        Test.expect(rot13("This is my first ROT13 excercise!") == "Guvf vf zl svefg EBG13 rkprepvfr!")
    """

    def __init__(self):
        pass

    def rot13_01(self, message):
        """
        intuitive
        """
        ret = []
        for c in message:
            if c in lowercase:
                ret.append(lowercase[(lowercase.index(c) + 13) % 26])
            elif c in uppercase:
                ret.append(uppercase[(uppercase.index(c) + 13) % 26])
            else:
                ret.append(c)
        return ''.join(ret)

    def rot13_02(self, message):
        """
        codecs.encode
        """
        return encode(message, 'rot13')

    def rot13_03(self, message):
        """
        maketrans
        """
        trans = str.maketrans(lowercase + uppercase, lowercase[13:] + lowercase[:13] + uppercase[13:] + uppercase[:13])

        return message.translate(trans)

    def rot13_04(self, message):
        """
        trans-dict manually made
        """
        trans = {
            a: b for a, b in zip(encode(lowercase + uppercase, 'ascii'),
                                 encode(lowercase[13:] + lowercase[:13] + uppercase[13:] + uppercase[:13], 'ascii'))
            }

        return message.translate(trans)

    def rot13_05(self, message):
        """
        ascii codec
        """
        ret = []
        for c in message:
            c_ord = ord(c)
            if 65 <= c_ord < 91:
                ret.append(chr(65 + (c_ord - 65 + 13) % 26))
            elif 97 <= c_ord < 123:
                ret.append(chr(97 + (c_ord - 97 + 13) % 26))
            else:
                ret.append(c)

        return ''.join(ret)


def sets_gen(rot13):
    import random
    test_sets = []
    for i in range(100, 2001):
        message = ''.join([random.choice(printable) for _ in range(i)])
        match = rot13(message)
        test_sets.append((
            (message,),
            match
        ))
    return test_sets


if __name__ == "__main__":
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
