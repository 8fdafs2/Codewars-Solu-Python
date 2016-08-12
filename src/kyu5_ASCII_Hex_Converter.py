from codecs import encode, decode
from binascii import hexlify, unhexlify, a2b_hex, b2a_hex
from base64 import b16encode, b16decode

import sys


class Converter_01():
    # python 2
    @staticmethod
    def to_ascii(h):
        return a2b_hex(h)

    @staticmethod
    def to_hex(s):
        return b2a_hex(s)


class Converter_01_py3():
    # python 3
    @staticmethod
    def to_ascii(h):
        return a2b_hex(bytes(h, encoding='ascii')).decode(encoding='ascii')

    @staticmethod
    def to_hex(s):
        return b2a_hex(bytes(s, encoding='ascii')).decode(encoding='ascii')


class Converter_02():
    # python 2
    @staticmethod
    def to_ascii(h):
        return unhexlify(h)

    @staticmethod
    def to_hex(s):
        return hexlify(s)


class Converter_02_py3():
    # python 3
    @staticmethod
    def to_ascii(h):
        return unhexlify(bytes(h, encoding='ascii')).decode(encoding='ascii')

    @staticmethod
    def to_hex(s):
        return hexlify(bytes(s, encoding='ascii')).decode(encoding='ascii')


class Converter_03():
    # python 2
    @staticmethod
    def to_ascii(h):
        return h.decode('hex')

    @staticmethod
    def to_hex(s):
        return s.encode('hex')


class Converter_03_py3():
    # python 3
    @staticmethod
    def to_ascii(h):
        return decode(bytes(h, encoding='ascii'), 'hex').decode(encoding='ascii')

    @staticmethod
    def to_hex(s):
        return encode(bytes(s, encoding='ascii'), 'hex').decode(encoding='ascii')


class Converter_04():
    # python 2
    @staticmethod
    def to_ascii(h):
        return b16decode(h.upper())

    @staticmethod
    def to_hex(s):
        return b16encode(s).lower()


class Converter_04_py3():
    # python 3
    @staticmethod
    def to_ascii(h):
        return b16decode(bytes(h.upper(), encoding='ascii')).decode('ascii')

    @staticmethod
    def to_hex(s):
        return b16encode(bytes(s, encoding='ascii')).lower().decode('ascii')


class Converter_05():
    # python 2/3
    @staticmethod
    def to_ascii(h):
        return ''.join([chr(int(h[i:i + 2], base=16)) for i in range(0, len(h), 2)])

    @staticmethod
    def to_hex(s):
        return ''.join(['{:02x}'.format(ord(c)) for c in s])
        # return ''.join([hex(ord(c))[2:] for c in s])


if sys.version_info.major == 3:
    Converter_01 = Converter_01_py3
    Converter_02 = Converter_02_py3
    Converter_03 = Converter_03_py3
    Converter_04 = Converter_04_py3


class Solution():
    """
    https://www.codewars.com/kata/52fea6fd158f0576b8000089

    Write a module Converter that can take ASCII text and convert it to hexadecimal.
    The class should also be able to take hexadecimal and convert it to ASCII text.

    Example

    Converter.to_hex("Look mom, no hands")
    => "4c6f6f6b206d6f6d2c206e6f2068616e6473"

    Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473")
    => "Look mom, no hands"
    """

    def __init__(self):
        pass

    def subsol_01(self, s, h):
        """
        binascii.a2b_hex, binascii.b2a_hex
        """
        c = Converter_01
        return c.to_hex(s), c.to_ascii(h)

    def subsol_02(self, s, h):
        """
        binascii.hexlify, binascii.unhexlify
        """
        c = Converter_02
        return c.to_hex(s), c.to_ascii(h)

    def subsol_03(self, s, h):
        """
        codecs.encode, codecs.decode
        """
        c = Converter_03
        return c.to_hex(s), c.to_ascii(h)

    def subsol_04(self, s, h):
        """
        base64.b16encode, base64.b16decode
        """
        c = Converter_04
        return c.to_hex(s), c.to_ascii(h)

    def subsol_05(self, s, h):
        """
        chr, int, ord, hex
        """
        c = Converter_05
        return c.to_hex(s), c.to_ascii(h)


def sets_gen(subsol):
    import random
    import string
    chars_ascii = string.ascii_lowercase
    test_sets = []
    for i in range(3, 1000):
        s = ''.join([random.choice(chars_ascii) for _ in range(i)])
        h = ''.join(['{:02x}'.format(ord(c)) for c in s])
        match = subsol(s, h)
        test_sets.append((
            (s, h),
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
