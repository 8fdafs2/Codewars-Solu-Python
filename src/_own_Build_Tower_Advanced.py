class Solution():
    """
    https://www.codewars.com/kata/57675f3dedc6f728ee000256

    Build Tower by given number of floors (integers and always greater than 0)
    and the block size (width, height)

    Tower block unit is represented as '*'

    Have fun!

    # for example, a tower of 3 floors with block size = (2, 3)
    looks like below
    [
      ['  **  '],
      ['  **  '],
      ['  **  '],
      [' **** '],
      [' **** '],
      [' **** '],
      ['******'],
      ['******'],
      ['******']
    ]
    """

    def __init__(self):
        pass

    def tower_builder_01(self, n_floors, block_size):
        """
        """
        w, h = block_size
        floors = []
        n = n_floors
        for i in range(n_floors):
            n -= 1
            for j in range(h):
                floors.append(' ' * n * w + '*' *
                              (i * 2 + 1) * w + ' ' * n * w)

        return floors

    def tower_builder_02(self, n_floors, block_size):
        """
        """
        w, h = block_size
        r = []
        l = ""
        s = "*" * (n_floors * w * 2 - w)
        for i in range(n_floors):
            for j in range(h):
                r.append(l + s + l)
            l += " " * w
            s = s[w * 2:]
        return r[::-1]


if __name__ == '__main__':
    sol = Solution()

    for floor in sol.tower_builder_02(6, (1, 2)):
        print(floor)

    print(repr(sol.tower_builder_02(6, (2, 1))))
