def divisors_01(integer):
    return [i for i in range(2, integer // 2 + 1) if not integer % i] or '{:d} is prime'.format(integer)


def divisors_02(integer):
    if integer % 2 == 0:
        div_last = integer // 2
        if div_last > 1:
            return [2, ] + [i for i in range(3, div_last) if integer % i == 0] + [div_last, ]
        return [2, ]
    return [i for i in range(3, integer // 2) if integer % i == 0] or '{:d} is prime'.format(integer)


# --------------------------------

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def prime_gen_01(integer):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    ret = []

    D = {}

    # The running integer that's checked for primeness
    q = 2

    for q in range(2, integer + 1):
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            ret.append(q)
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

    return ret

# --------------------------------

import functools
import itertools
import operator


def prime_gen_02(integer):
    """
    Sieve of Eratosthenes
    Create a candidate list within which non-primes will be
    marked as None.
    """
    cand = [i for i in range(3, integer + 1, 2)]
    end = int(integer ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * (
                (integer // cand[i]) - (integer // (2 * cand[i])) - 1)

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]


def factorize(integer):
    prime_multiples = []
    for item in primes_list:
        if item > integer: break
        while integer > 1:
            if integer % item != 0: break
            integer //= item
            prime_multiples.append(item)
    return prime_multiples


def divisors_03(integer):
    prime_multiples_list = factorize(integer)
    """
    construct unique combinations
    A, B, B, C --> A, B, C, AB, AC, BB, BC, ABC, ABB, BBC
    """
    unique_combinations = set()
    for i in range(1, len(prime_multiples_list)):
        unique_combinations.update(
            set(itertools.combinations(prime_multiples_list, i)))

    # multiply elements of each unique combination
    return sorted(functools.reduce(operator.mul, i)
                  for i in unique_combinations) or '{:d} is prime'.format(integer)


# --------------------------------

divisors = divisors_01


def sets_get(divisors=None):
    import random
    test_sets = []
    for i in range(100):
        integer = random.randint(1, 1000)
        match = divisors(integer)
        test_sets.append((integer, match))
    return test_sets


def test(divisors=None, test_sets=[]):
    for integer, match in test_sets:
        try:
            assert (divisors(integer) == match)
        except AssertionError as ex:
            print(ex)
            print((integer, match, divisors(integer)))


def test_spd(divisors=None, test_sets=[]):
    for integer, match in test_sets:
        divisors(integer)


if __name__ == '__main__':

    # prep
    print('prep...')
    test_sets = sets_get(divisors)

    # test
    print('test...')
    test(divisors_01, test_sets)
    test(divisors_02, test_sets)

    prime_gen = prime_gen_01
    primes_list = prime_gen(1000)
    test(divisors_03, test_sets)

    prime_gen = prime_gen_02
    primes_list = prime_gen(1000)
    test(divisors_03, test_sets)

    # test_spd
    print('test_spd...')
    stmt = 'test_spd(divisors_{:02d}, test_sets)'
    setup = 'from __main__ import test_spd, test_sets, divisors_01, divisors_02'
    setup_ = 'from __main__ import test_spd, test_sets, divisors_03, factorize, primes_list'
    number = 2000

    stmt_pre = 'prime_gen_{:02d}(1000)'
    setup_pre = 'from __main__ import prime_gen_01, prime_gen_02'
    number_pre = 2000

    import timeit
    print((timeit.timeit(stmt=stmt.format(1), setup=setup, number=number)))
    print((timeit.timeit(stmt=stmt.format(2), setup=setup, number=number)))

    prime_gen = prime_gen_01
    primes_list = prime_gen(1000)

    t_main = timeit.timeit(stmt=stmt.format(3), setup=setup_, number=number)
    t_pre = timeit.timeit(stmt=stmt_pre.format(1), setup=setup_pre, number=number_pre) / number_pre
    print(('{} + {}'.format(t_main, t_pre)))

    prime_gen = prime_gen_02
    primes_list = prime_gen(1000)

    t_main = timeit.timeit(stmt=stmt.format(3), setup=setup_, number=number)
    t_pre = timeit.timeit(stmt=stmt_pre.format(2), setup=setup_pre, number=number_pre) / number_pre
    print(('{} + {}'.format(t_main, t_pre)))


