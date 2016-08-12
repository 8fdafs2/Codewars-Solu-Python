class Solution():
    """
    https://www.codewars.com/kata/human-readable-time

    Write a function,
    which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59
    The maximum time never exceeds 359999 (99:59:59)

    You can find some examples in the test fixtures.
    """
    def __init__(self):
        pass

    def make_readable_01(self, seconds):
        """
        """
        mm, ss = divmod(seconds, 60)
        hh, mm = divmod(mm, 60)

        return '{:02d}:{:02d}:{:02d}'.format(hh, mm, ss)

    def make_readable_02(self, seconds):
        """
        """
        return '{:02d}:{:02d}:{:02d}'.format(seconds // 3600,
                                             seconds // 60 % 60,
                                             seconds % 60)


if __name__ == '__main__':

    sol = Solution()

    print(sol.make_readable_01(359999))
    print(sol.make_readable_02(359999))