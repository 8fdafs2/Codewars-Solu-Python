class Solution():
    """
    https://www.codewars.com/kata/longest-palindrome

    Longest Palindrome

        Find the length of the longest substring in the given string s that is the same in reverse.

        As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

        If the length of the input string is 0, return value must be 0.

    Example:

        "a" -> 1
        "aab" -> 2
        "abcde" -> 1
        "zzbaabcd" -> 4
        "" -> 0
    """

    def __init__(self):
        pass

    def longest_palindrome_01(self, s):
        """
        brute force
        """
        if not s:
            return 0
        len_s = len(s)
        for l in range(len_s, 1, -1):
            for i in range(len_s - l + 1):
                if s[i: l + i] == s[i: l + i][::-1]:
                    return l
        return 1

    def longest_palindrome_02(self, s):
        """
        brute force
        """
        if not s:
            return 0
        ret = 0
        len_s = len(s)
        for l in range(len_s):
            for r in range(len_s, l, -1):
                if s[l:r] == s[l:r][::-1]:
                    ret = max(ret, r - l)
        return ret

    def longest_palindrome_03(self, s):
        """
        Manacher algorithm - Complexity O(n)
        """
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return maxLen


def sets_gen(longest_palindrome):
    import random
    import string
    test_sets = []
    for i in range(100):
        s = ''.join([random.choice(string.ascii_lowercase) for _ in range(i)])
        match = longest_palindrome(s)
        test_sets.append((
            (s,),
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
