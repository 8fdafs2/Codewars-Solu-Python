from functools import reduce
class Solution():
    def __init__(self):
        self.chained = self.chained_01

    def chained_01(self, functions):
        def ret(x):
            for func in functions:
                x = func(x)
            return x

        return ret

    def chained_02(self, functions):
        return lambda x: reduce(lambda v, f: f(v), functions, x)
