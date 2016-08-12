class Solution():
    def __init__(self):
        self.add = self.add_01

    def add_01(self, x):

        class Add(int):
            def __call__(self, x):
                return Add(self + x)

        return Add(x)

if __name__ == '__main__':
    sol = Solution()
    print((sol.add(1)))