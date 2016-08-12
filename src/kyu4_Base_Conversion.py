Alphabet = {
    'BINARY': '01',
    'OCTAL': '01234567',
    'DECIMAL': '0123456789',
    'HEXA_DECIMAL': '0123456789abcdef',
    'ALPHA_LOWER': 'abcdefghijklmnopqrstuvwxyz',
    'ALPHA_UPPER': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'ALPHA': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'ALPHA_NUMERIC': '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
}

bin = Alphabet['BINARY']
oct = Alphabet['OCTAL']
dec = Alphabet['DECIMAL']
hex = Alphabet['HEXA_DECIMAL']
allow = Alphabet['ALPHA_LOWER']
alup = Alphabet['ALPHA_UPPER']
alpha = Alphabet['ALPHA']
alnum = Alphabet['ALPHA_NUMERIC']


class Solution():
    """
    https://www.codewars.com/kata/526a569ca578d7e6e300034e

    In this kata you have to implement a base converter,
    which converts between arbitrary bases / alphabets.
    Here are some pre-defined alphabets:

    bin='01'
    oct='01234567'
    dec='0123456789'
    hex='0123456789abcdef'
    allow='abcdefghijklmnopqrstuvwxyz'
    allup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphanum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    The function convert() should take an input (string),
    the source alphabet (string) and the target alphabet (string).
    You can assume that the input value always consists of characters from the source alphabet.
    You don't need to validate it.

    Examples:

        convert("15", dec, bin) #should return "1111"
        convert("15", dec, oct) #should return "17"
        convert("1010", bin, dec) #should return "10"
        convert("1010", bin, hex) #should return "a"

        convert("0", dec, alpha) #should return "a"
        convert("27", dec, allow) #should return "bb"
        convert("hello", allow, hex) #should return "320048"

    Additional Notes:

        The maximum input value can always be encoded in a number without loss of precision in JavaScript.
        In Haskell, intermediate results will probably be to large for Int.
        The function must work for any arbitrary alphabets, not only the pre-defined ones
        You don't have to consider negative numbers
    """

    def __init__(self):
        pass

    def convert_01(self, input, source, target):
        """
        subfunc
        """
        if source == target:
            return input

        def str_to_num(strng, source):
            ret = 0
            base = len(source)
            for i, c in enumerate(reversed(strng)):
                ret += source.index(c) * (base ** i)
            return ret

        def num_to_str(num, target):
            ret = ''
            base = len(target)
            while True:
                num, rem = divmod(num, base)
                ret += target[rem]
                if num <= 0:
                    return ret[::-1]

        return num_to_str(str_to_num(input, source), target)

    def convert_02(self, input, source, target):
        """
        iter
        """
        base_in = len(source)
        base_out = len(target)
        acc = 0
        for d in input:
            acc *= base_in
            acc += source.index(d)
        out = ''
        while True:
            out = target[acc % base_out] + out
            acc //= base_out
            if acc == 0:
                return out


def sets_gen(convert):
    import random
    formats = [bin, oct, dec, hex, allow, alup, alpha, alnum]
    test_sets = []
    for i in range(1000):
        source = random.choice(formats)
        input = ''.join([random.choice(source) for _ in range(1, 10)]).lstrip(source[0])
        target = random.choice(formats)
        match = convert(input, source, target)
        test_sets.append((
            (input, source, target),
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

