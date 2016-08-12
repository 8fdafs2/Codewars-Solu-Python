from math import factorial, log


class Solution():
    """
    https://www.codewars.com/kata/factorial-tail

    The problem

        How many zeroes are at the end of the factorial of 10? 10! = 3628800, i.e. there are two zeroes.
        16! in hexadecimal would be 0x130777758000, which results in three zeroes.

        Unfortunately machine integer numbers has not enough precision for larger values.
        Floats drops the tail we need.
        We can fall back to arbitrary-precision ones - built-ins or from a library,
        but calculating the full product isn't an efficient way to find the tail of the factorial.
        Calculating 100'000! takes around 10 seconds on my machine, let alone 1'000'000!.

    Your task

        is to write a function,
        which will find number of zeroes at the end of (number) factorial in arbitrary radix = base for larger numbers.

        base is an integer from 2 to 256
        number is an integer from 1 to 1'000'000
    """

    def __init__(self):
        pass

    # @staticmethod
    # def zeroes_01(base, number):
    #     """
    #     ugly brute force
    #     """
    #     ret = 0
    #     f = factorial(number)
    #     while f % base == 0:
    #         ret += 1
    #         f //= base
    #     return ret
    #
    # @staticmethod
    # def zeroes_02(base, number):
    #     """
    #     brute force, opt
    #     """
    #     f = 1
    #     ret = 0
    #     for i in range(2, number + 1):
    #         while i % base == 0:
    #             ret += 1
    #             i //= base
    #         f *= i
    #     while f % base == 0:
    #         ret += 1
    #         f //= base
    #     return ret

    @staticmethod
    def zeroes_03(base, number):
        """
        prime factor
        """
        hashtab_base = {}
        i = 2
        _base_ = base
        while i <= _base_:
            if _base_ % i == 0:
                _base_ //= i
                e = 1
                while _base_ % i == 0:
                    _base_ //= i
                    e += 1
                hashtab_base[i] = e
            if i == 2:
                i = 3
            else:
                i += 2

        ret = []
        hashtab_fac = {}
        for p in hashtab_base:
            hashtab_fac[p] = 0
            _number_ = number
            while _number_ > 0:
                _number_ //= p
                hashtab_fac[p] += _number_
            ret.append(hashtab_fac[p] // hashtab_base[p])

        return min(ret)

    @staticmethod
    def zeroes_04(base, number):
        """
        prime factor, opt
        """
        ret = []
        p = 2
        _base_ = base
        while p <= _base_:
            if _base_ % p == 0:
                _base_ //= p
                e_base = 1
                while _base_ % p == 0:
                    _base_ //= p
                    e_base += 1
                e_fac = 0
                _number_ = number
                while _number_ > 0:
                    _number_ //= p
                    e_fac += _number_
                ret.append(e_fac // e_base)
            if p == 2:
                p = 3
            else:
                p += 2

        return min(ret)

    @staticmethod
    def zeroes_05(base, number):
        """
        brute force, opt, cap f
        """
        ret = 0
        f = 1
        b = base ** int(log(1000000, base))
        # b = base ** 5
        for i in range(2, number + 1):
            f *= i
            while f % base == 0:
                f //= base
                ret += 1
            f %= b
        return ret


def sets_gen(zeros):
    test_sets = []
    for base in range(2, 65):
        for number in range(10000, 10101):
            match = zeros(base, number)
            test_sets.append((
                (base, number),
                match
            ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1, prt_docstr=True)
