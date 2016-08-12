class Solution():
    """
    Make your own 'built-in' product function.

    The product function multiplies all the elements in iterable given
    as the first argument and returns the product.
    There will be a second argument (optional, default: 1) to specify
    the start element to multiply. When the iterable is empty, returns the start element.

    For example:

    product()  # 1
    product([1, 2, 3])  # 1 * 2 * 3
    product([1, 2, 3], -1)  # -1 * 1 * 2 * 3
    Remember you have to make it as a bulit-in function. Enjoy!
    """

    def __init__(self):
        pass

    @staticmethod
    def product_01(iterable=None, start=1):
        """built-in product function"""
        if not iterable:
            return start
        ret = start
        for x in iterable:
            ret *= x
        return ret


globals()['__builtins__'].product = Solution().product_01


class Multipliable(str):
    def __mul__(self, other):
        return Multipliable(int(self) * int(other))


product([Multipliable('1'),
         Multipliable('2'),
         Multipliable('3')])
