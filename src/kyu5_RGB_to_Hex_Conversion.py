class Solution():
    """
    https://www.codewars.com/kata/513e08acc600c94f01000001

    The rgb() method is incomplete.
    Complete the method so that passing in RGB decimal values
    will result in a hexadecimal representation being returned.
    The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values
    that fall out of that range should be rounded to the closest valid value.

    The following are examples of expected output values:

        rgb(255, 255, 255) # returns FFFFFF
        rgb(255, 255, 300) # returns FFFFFF
        rgb(0,0,0) # returns 000000
        rgb(148, 0, 211) # returns 9400D3
    """

    def rgb_01(self, r, g, b):
        """
        intuitive
        """
        if r > 255:
            r = 255
        elif r < 0:
            r = 0

        if g > 255:
            g = 255
        elif g < 0:
            g = 0

        if b > 255:
            b = 255
        elif b < 0:
            b = 0

        return '{:02X}{:02X}{:02X}'.format(r, g, b)

    def rgb_02(self, r, g, b):
        """
        one-liner, min(max( , ), )
        """
        return ('{:02X}'*3).format(
            min(255, max(0, r)),
            min(255, max(0, g)),
            min(255, max(0, b)))

    def rgb_03(self, r, g, b):
        """
        one-liner, sorted([ , , ])
        """
        return ('{:02X}'*3).format(
            sorted([0, r, 255])[1],
            sorted([0, g, 255])[1],
            sorted([0, b, 255])[1])

def sets_gen(rgb):
    import random
    test_sets = []
    for i in range(1000):
        r = random.randint(-10, 265)
        g = random.randint(-10, 265)
        b = random.randint(-10, 265)
        match = rgb(r, g, b)
        test_sets.append((
            (r, g, b),
            match
        ))
    return test_sets


if __name__ == "__main__":
    sol = Solution()
    from test_fixture import Test_Fixture
    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=True)