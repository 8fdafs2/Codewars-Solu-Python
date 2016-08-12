from functools import reduce
from itertools import chain


class Solution():
    """
    https://www.codewars.com/kata/recover-a-secret-string-from-random-triplets

    There is a secret string which is unknown to you.
    Given a collection of random triplets from the string, recover the original string.

    A triplet here is defined as a sequence of three letters such that
    each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

    As a simplification, you may assume that no letter occurs more than once in the secret string.

    You can assume nothing about the triplets given to you other than that they are valid triplets and that
    they contain sufficient information to deduce the original string.
    In particular, this means that the secret string will never contain letters that
    do not occur in one of the triplets given to you.
    """

    def __init__(self):
        pass

    def recoverSecret_01(self, triplets):
        """
        rule-out-one x length-times
        """
        set_all = set(sum(triplets, []))
        triplets = [list(triplet) for triplet in triplets]
        c = ''
        ret = []
        while set_all:
            set_front = []
            for t in triplets:
                if not t:
                    continue
                if c == t[0]:
                    del t[0]
                if not t:
                    continue
                set_front += t[1:]
            c = (set_all - set(set_front)).pop()
            set_all.discard(c)
            ret.append(c)

        return ''.join(ret)

    def recoverSecret_02(self, triplets):
        """
        rule-out-two x length//2-times
        """
        set_all = set(sum(triplets, []))
        triplets = [list(triplet) for triplet in triplets]
        c_front = c_back = ''
        l = len(set_all)
        ret = [None, ] * l
        i, j = 0, l - 1
        while True:
            set_front = []
            set_back = []
            for t in triplets:
                if not t:
                    continue
                if c_front == t[0]:
                    del t[0]
                if not t:
                    continue
                if c_back == t[-1]:
                    del t[-1]
                if not t:
                    continue
                set_front += t[:-1]
                set_back += t[1:]
            ret[i] = c_front = (set_all - set(set_back)).pop()
            set_all.discard(c_front)
            i += 1
            ret[j] = c_back = (set_all - set(set_front)).pop()
            set_all.discard(c_back)
            j -= 1
            if len(set_all) < 2:
                if set_all:
                    ret[i] = set_all.pop()
                return ''.join(ret)

    def recoverSecret_03(self, triplets):
        """
        count x len(triplets)*2-times
        """
        hashtab = {c: 1 for c in set([c for t in triplets for c in t])}
        triplets_dbl = triplets + triplets[::-1]
        for _ in range(len(hashtab) >> 1):
            for t0, t1, t2 in triplets_dbl:
                hashtab[t1] += hashtab[t0]
                hashtab[t2] += hashtab[t1]

        return ''.join([c for c, _ in sorted(hashtab.items(), key=lambda x: x[1])])

    def recoverSecret_04(self, triplets):
        """
        sort-in-place x more-than-len(triplets)-times (worst case)
        """
        set_all = list(set([c for t in triplets for c in t]))

        is_change = True
        while is_change:
            is_change = False
            for t0, t1, t2 in triplets:
                i_t0, i_t1, i_t2 = set_all.index(t0), set_all.index(t1), set_all.index(t2)
                if not i_t0 < i_t1 < i_t2:
                    # i_t0, i_t1, i_t2 = sorted([i_t0, i_t1, i_t2])

                    if i_t0 > i_t1:
                        i_t0, i_t1 = i_t1, i_t0
                    if i_t1 > i_t2:
                        i_t1, i_t2 = i_t2, i_t1
                    if i_t0 > i_t1:
                        i_t0, i_t1 = i_t1, i_t0

                    set_all[i_t0], set_all[i_t1], set_all[i_t2] = t0, t1, t2
                    is_change = True

        return ''.join(set_all)

    def recoverSecret_05(self, triplets):
        """
        sort-by-append x len(triplets)*2-times
        """
        set_all = list(set(chain(*triplets)))
        for t0, t1, t2 in triplets + triplets[::-1]:
            i_t0, i_t1, i_t2 = set_all.index(t0), set_all.index(t1), set_all.index(t2)
            # 0 2 1
            if i_t0 < i_t2 < i_t1:
                del set_all[i_t2]
                set_all.append(t2)
            # 1 0 2
            elif i_t1 < i_t0 < i_t2:
                del set_all[i_t2]
                del set_all[i_t1]
                set_all.append(t1)
                set_all.append(t2)
            # 1 2 0
            elif i_t1 < i_t2 < i_t0:
                del set_all[i_t2]
                del set_all[i_t1]
                set_all.append(t1)
                set_all.append(t2)
            # 2 0 1
            elif i_t2 < i_t0 < i_t1:
                del set_all[i_t2]
                set_all.append(t2)
            # 2 1 0
            elif i_t2 < i_t1 < i_t0:
                del set_all[i_t1]
                del set_all[i_t2]
                set_all.append(t1)
                set_all.append(t2)

        return ''.join(set_all)

    def recoverSecret_06(self, triplets):
        """
        sort-by-insert x len(triplets)*2-times
        """
        set_all = list(set(chain(*triplets)))
        for t0, t1, t2 in triplets + triplets[::-1]:
            i_t0, i_t1, i_t2 = set_all.index(t0), set_all.index(t1), set_all.index(t2)
            # 0 2 1
            if i_t0 < i_t2 < i_t1:
                del set_all[i_t1]
                set_all.insert(i_t2, t1)
            # 1 0 2
            elif i_t1 < i_t0 < i_t2:
                del set_all[i_t0]
                set_all.insert(i_t1, t0)
            # 1 2 0
            elif i_t1 < i_t2 < i_t0:
                del set_all[i_t0]
                set_all.insert(i_t1, t0)
            # 2 0 1
            elif i_t2 < i_t0 < i_t1:
                del set_all[i_t1]
                del set_all[i_t0]
                set_all.insert(i_t2, t1)
                set_all.insert(i_t2, t0)
            # 2 1 0
            elif i_t2 < i_t1 < i_t0:
                del set_all[i_t0]
                del set_all[i_t1]
                set_all.insert(i_t2, t1)
                set_all.insert(i_t2, t0)

        return ''.join(set_all)

    def recoverSecret_07(self, triplets):
        """
        rule-out-one x length-times
        """
        set_all = set(reduce(list.__add__, triplets))
        triplets = [list(t) for t in triplets]
        ret = []
        for i in range(len(set_all)):
            out = list(zip(*triplets))
            ret.append(list(set(out[0]) - set(out[1] + out[2]))[0])
            for t in triplets:
                if t[0] == ret[-1]:
                    t[:2], t[2] = t[1:], None

        return ''.join(ret)


def sets_gen(recoverSecret):
    import random
    import string
    import itertools
    test_sets = []
    for i in range(3, 30):
        secret = random.sample(string.ascii_letters, i)
        triplets_all = list(itertools.combinations(secret, 3))
        random.shuffle(triplets_all)
        triplets = []
        for a, b in zip(secret, secret[1:]):
            for t in triplets_all:
                if a in t and b in t:
                    if t not in triplets:
                        triplets.append(list(t))
                    break
        match = recoverSecret(triplets)
        test_sets.append((
            (triplets,),
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
