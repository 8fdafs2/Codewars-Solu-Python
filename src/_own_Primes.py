from math import sqrt, ceil

import numpy as np


class Solution():
    """
    """

    def __init__(self):
        pass

    def primes_01(self, n):
        """
        Trial division
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        primes = []
        for m in range(3, n + 1, 2):
            mroot = int(sqrt(m))
            for p in primes:
                if p > mroot:
                    primes.append(m)
                    break
                if m % p == 0:  # not-a-prime-number
                    break
            else:
                primes.append(m)

        return [2, ] + primes

    def primes_02(self, n):
        """
        sieves, skip 2, True/False
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        top = n + 1
        sieve = [True, ] * top
        for i in range(3, int(sqrt(top)) + 1, 2):
            if sieve[i]:
                bot = i * i
                sieve[bot::i + i] = [False, ] * ((top - bot - 1) // (i + i) + 1)

        return [2, ] + [i for i in range(3, top, 2) if sieve[i]]

    def primes_03(self, n):
        """
        sieves, skip 2, True/False, half length
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        top = (n + 1) // 2
        sieve = [True, ] * top
        for i in range(3, int(sqrt(n + 1)) + 1, 2):
            if sieve[i // 2]:
                bot = i * i // 2
                sieve[bot::i] = [False, ] * ((top - bot - 1) // i + 1)

        return [2, ] + [i + i + 1 for i in range(1, top) if sieve[i]]

    def primes_04(self, n):
        """
        sieves, skip 2, True/False, half length, numpy
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        sieve = np.ones((n + 1) // 2, dtype=np.bool)
        for i in range(3, int(sqrt(n + 1)) + 1, 2):
            if sieve[i // 2]:
                sieve[i * i // 2::i] = False

        return [2, ] + list(np.r_[2 * np.nonzero(sieve)[0][1::] + 1])
        # return list(np.r_[2, 2 * np.nonzero(sieve)[0][1::] + 1])

    def primes_05(self, n):
        """
        sieves, skip 2, range
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        top = n + 1
        sieve = list(range(top))
        for i in range(3, int(sqrt(n)) + 1, 2):
            if sieve[i] != 0:
                bot = i * i
                sieve[bot::i + i] = [0, ] * ((top - bot - 1) // (i + i) + 1)

        return [2, ] + list(filter(None, sieve[3::2]))

    def primes_06(self, n):
        """
        sieves, skip 2, range, half length
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        sieve = list(range(3, n + 1, 2))
        top = len(sieve)
        m = 3
        for i in range(int(sqrt(n)) // 2):
            if sieve[i] != 0:
                bot = (m * m - 3) // 2
                sieve[bot::m] = [0, ] * ((top - bot - 1) // m + 1)
            m += 2

        return [2, ] + list(filter(None, sieve))

    def primes_07(self, n):
        """
        sieves, skip 2, range, half length
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        sieve = list(range(3, n + 1, 2))
        top = len(sieve)
        for m in range(3, int(sqrt(n + 1)) + 1, 2):
            if sieve[(m - 3) // 2] != 0:
                bot = (m * m - 3) // 2
                sieve[bot::m] = [0, ] * ((top - bot - 1) // m + 1)

        return [2, ] + list(filter(None, sieve))

    def primes_08(self, n):
        """
        sieves, skip 2, range, half length, no sqrt
        """
        # Code from: <dickinsm@gmail.com>, Nov 30 2006
        # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        sieve = list(range(3, n + 1, 2))
        top = len(sieve)
        for m in sieve:
            if m != 0:
                bot = (m * m - 3) // 2
                if bot >= top:
                    return [2, ] + list(filter(None, sieve))
                sieve[bot::m] = [0, ] * ((top - bot - 1) // m + 1)

    def primes_09(self, n):
        """
        sieves, skip 2, range, half length, no sqrt, numpy
        """
        # Code from: <dickinsm@gmail.com>, Nov 30 2006
        # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        sieve = np.arange(3, n + 1, 2)
        top = len(sieve)
        for m in sieve:
            if m != 0:
                bot = (m * m - 3) // 2
                if bot >= top:
                    # return list(np.r_[2, sieve[sieve > 0]])
                    # return [2, ] + list(np.r_[sieve[sieve > 0]])
                    return [2, ] + list(filter(None, sieve))
                sieve[bot::m] = 0

    def primes_10(self, n):
        """
        sieves, sundaram
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        sieve = list(range(3, n + 1, 2))
        top = len(sieve)
        bot = 3
        for step in range(3, n + 1, 2):
            sieve[bot::step] = [0, ] * ((top - bot - 1) // step + 1)
            bot += 2 * (step + 1)
            if bot >= top:
                return [2, ] + list(filter(None, sieve))

    def primes_11(self, n):
        """
        sieves, sundaram, numpy
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        sieve = np.arange(3, n + 1, 2)
        top = len(sieve)
        bot = 3
        for step in range(3, n + 1, 2):
            sieve[bot::step] = 0
            bot += 2 * (step + 1)
            if bot >= top:
                # return list(np.r_[2, sieve[sieve > 0]])
                # return [2, ] + list(np.r_[sieve[sieve > 0]])
                return [2, ] + list(filter(None, sieve))

    def primes_12(self, n):
        """
        sieve, a third of
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        n += 1

        correction = (n % 6 > 1)
        n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
        sieve = [True, ] * (n // 3)
        sieve[0] = False
        for i in range(int(sqrt(n)) // 3 + 1):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[k * k // 3::k + k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
                sieve[k * (k - 2 * (i & 1) + 4) // 3::k + k] = \
                    [False] * ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)

        return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]

    def primes_13(self, n):
        """
        sieve, a third of, numpy
        """
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        sieve = np.ones((n + 1) // 3 + ((n + 1) % 6 == 2), dtype=np.bool)
        sieve[0] = False
        for i in range(int(sqrt(n + 1)) // 3 + 1):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[k * k // 3::k + k] = False
                sieve[k * (k - 2 * (i & 1) + 4) // 3::k + k] = False

        return [2, 3] + list(np.r_[((3 * np.nonzero(sieve)[0] + 1) | 1)])
        # return list(np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)])

    def primes_14(self, n):
        """
        sieve, wheel criterion 2*3*5 = 30
        """
        # http://zerovolt.com/?p=88
        # Copyright 2009 by zerovolt.com
        # This code is free for non-commercial purposes,
        # in which case you can just leave this comment as a credit for my work.
        # If you need this code for commercial purposes,
        # please contact me by sending an email to: info [at] zerovolt [dot] com.
        if n < 2:
            return []
        if n == 2:
            return [2, ]

        __smallp = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                    61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
                    149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
                    229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
                    313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
                    409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
                    499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
                    691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
                    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997)

        const = 30
        if n <= const:
            pos = 0
            while __smallp[pos] <= n:
                pos += 1
            return list(__smallp[:pos])
        # make the offsets list
        offsets = (7, 11, 13, 17, 19, 23, 29, 1)
        # prepare the list
        p = [2, 3, 5]
        dim = 2 + n // const
        tk1 = [True] * dim
        tk7 = [True] * dim
        tk11 = [True] * dim
        tk13 = [True] * dim
        tk17 = [True] * dim
        tk19 = [True] * dim
        tk23 = [True] * dim
        tk29 = [True] * dim
        tk1[0] = False
        # help dictionary d
        # d[a , b] = c  ==> if I want to find the smallest useful multiple of (30*pos)+a
        # on tkc, then I need the index given by the product of [(30*pos)+a][(30*pos)+b]
        # in general. If b < a, I need [(30*pos)+a][(30*(pos+1))+b]
        d = {}
        for x in offsets:
            for y in offsets:
                res = (x * y) % const
                if res in offsets:
                    d[(x, res)] = y
        # another help dictionary: gives tkx calling tmptk[x]
        tmptk = {1: tk1, 7: tk7, 11: tk11, 13: tk13, 17: tk17, 19: tk19, 23: tk23, 29: tk29}
        pos, prime, lastadded, stop = 0, 0, 0, int(ceil(sqrt(n)))

        # inner functions definition
        def del_mult(tk, start, step):
            for k in range(start, len(tk), step):
                tk[k] = False

        # end of inner functions definition
        cpos = const * pos
        while prime < stop:
            # 30k + 7
            if tk7[pos]:
                prime = cpos + 7
                p.append(prime)
                lastadded = 7
                for off in offsets:
                    tmp = d[(7, off)]
                    start = (pos + prime) if off == 7 else (
                        prime * (
                            const * (pos + 1 if tmp < 7 else 0) + tmp)) // const
                    del_mult(tmptk[off], start, prime)
            # 30k + 11
            if tk11[pos]:
                prime = cpos + 11
                p.append(prime)
                lastadded = 11
                for off in offsets:
                    tmp = d[(11, off)]
                    start = (pos + prime) if off == 11 else (prime * (
                        const * (pos + 1 if tmp < 11 else 0) + tmp)) // const
                    del_mult(tmptk[off], start, prime)
            # 30k + 13
            if tk13[pos]:
                prime = cpos + 13
                p.append(prime)
                lastadded = 13
                for off in offsets:
                    tmp = d[(13, off)]
                    start = (pos + prime) if off == 13 else (prime * (
                        const * (pos + 1 if tmp < 13 else 0) + tmp)) // const
                    del_mult(tmptk[off], start, prime)
            # 30k + 17
            if tk17[pos]:
                prime = cpos + 17
                p.append(prime)
                lastadded = 17
                for off in offsets:
                    tmp = d[(17, off)]
                    start = (pos + prime) if off == 17 else (prime * (
                        const * (pos + 1 if tmp < 17 else 0) + tmp)) // const
                    del_mult(tmptk[off], start, prime)
            # 30k + 19
            if tk19[pos]:
                prime = cpos + 19
                p.append(prime)
                lastadded = 19
                for off in offsets:
                    tmp = d[(19, off)]
                    start = (pos + prime) if off == 19 else (prime * (
                        const * (pos + 1 if tmp < 19 else 0) + tmp)) // const
                    del_mult(tmptk[off], start, prime)
            # 30k + 23
            if tk23[pos]:
                prime = cpos + 23
                p.append(prime)
                lastadded = 23
                for off in offsets:
                    tmp = d[(23, off)]
                    start = (pos + prime) if off == 23 else (prime * (
                        const * (pos + 1 if tmp < 23 else 0) + tmp)) // const
                    del_mult(tmptk[off], start, prime)
            # 30k + 29
            if tk29[pos]:
                prime = cpos + 29
                p.append(prime)
                lastadded = 29
                for off in offsets:
                    tmp = d[(29, off)]
                    start = (pos + prime) if off == 29 else (prime * (
                        const * (pos + 1 if tmp < 29 else 0) + tmp)) // const
                    del_mult(tmptk[off], start, prime)
            # now we go back to top tk1, so we need to increase pos by 1
            pos += 1
            cpos = const * pos
            # 30k + 1
            if tk1[pos]:
                prime = cpos + 1
                p.append(prime)
                lastadded = 1
                for off in offsets:
                    tmp = d[(1, off)]
                    start = (pos + prime) if off == 1 else (prime * (const * pos + tmp)) // const
                    del_mult(tmptk[off], start, prime)
        # time to add remaining primes
        # if lastadded == 1, remove last element and start adding them from tk1
        # this way we don't need an "if" within the last while
        if lastadded == 1:
            p.pop()
        # now complete for every other possible prime
        while pos < len(tk1):
            cpos = const * pos
            if tk1[pos]:
                p.append(cpos + 1)
            if tk7[pos]:
                p.append(cpos + 7)
            if tk11[pos]:
                p.append(cpos + 11)
            if tk13[pos]:
                p.append(cpos + 13)
            if tk17[pos]:
                p.append(cpos + 17)
            if tk19[pos]:
                p.append(cpos + 19)
            if tk23[pos]:
                p.append(cpos + 23)
            if tk29[pos]:
                p.append(cpos + 29)
            pos += 1
        # remove exceeding if present
        pos = len(p) - 1
        while p[pos] > n:
            pos -= 1
        if pos < len(p) - 1:
            del p[pos + 1:]
        # return p list
        return p

    def primes_15(self, end):
        """
        sieve of Atkin(end)
        """
        # Code by Steve Krenzel, <Sgk284@gmail.com>, improved
        # Code: https://web.archive.org/web/20080324064651/http://krenzel.info/?p=83
        # Info: http://en.wikipedia.org/wiki/Sieve_of_Atkin
        if end < 2:
            return []
        if end == 2:
            return [2, ]

        lng = end // 2
        sieve = [False] * (lng + 1)

        x_max, x2, xd = int(sqrt(end / 4)), 0, 4
        for xd in range(4, 8 * x_max + 2, 8):
            x2 += xd
            y_max = int(sqrt(end + 1 - x2))
            n, n_diff = x2 + y_max * y_max, (y_max * 2) - 1
            if not (n & 1):
                n -= n_diff
                n_diff -= 2
            for d in range((n_diff - 1) * 2, -1, -8):
                m = n % 12
                if m == 1 or m == 5:
                    m = n // 2
                    sieve[m] = not sieve[m]
                n -= d

        x_max, x2, xd = int(sqrt(end / 3)), 0, 3
        for xd in range(3, 6 * x_max + 2, 6):
            x2 += xd
            y_max = int(sqrt(end + 1 - x2))
            n, n_diff = x2 + y_max * y_max, (y_max << 1) - 1
            if not (n & 1):
                n -= n_diff
                n_diff -= 2
            for d in range((n_diff - 1) * 2, -1, -8):
                if n % 12 == 7:
                    m = n // 2
                    sieve[m] = not sieve[m]
                n -= d

        x_max, y_min, x2, xd = int((2 + sqrt(4 + 8 * end)) / 4), -1, 0, 3
        for x in range(1, x_max + 1):
            x2 += xd
            xd += 6
            if x2 >= end + 1:
                y_min = (((int(ceil(sqrt(x2 - end - 1))) - 1) * 2) - 2) * 2
            n, n_diff = ((x * x + x) * 2) - 1, (((x - 1) * 2) - 2) * 2
            for d in range(n_diff, y_min, -8):
                if n % 12 == 11:
                    m = n // 2
                    sieve[m] = not sieve[m]
                n += d

        primes = [2, 3]
        if end <= 2:
            return primes[:max(0, end - 1)]

        for n in range(5 // 2, (int(sqrt(end + 1)) + 1) // 2):
            if sieve[n]:
                primes.append((n * 2) + 1)
                aux = (n * 2) + 1
                aux *= aux
                for k in range(aux, end + 1, 2 * aux):
                    sieve[k // 2] = False

        s = int(sqrt(end + 1)) + 1
        if s % 2 == 0:
            s += 1
        primes.extend([i for i in range(s, end + 1, 2) if sieve[i // 2]])

        return primes


def sets_gen(primes):
    test_sets = []
    for n in range(1, 1000):
        match = primes(n)
        test_sets.append((
            (n,),
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
