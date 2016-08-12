import re


class Solution():
    def __init__(self):
        self.compare = self.compare_01

    def compare_01(self, a, b):
        def weight(x):
            spec_x = [0, 0, 0]
            x_s = x.split(' ')
            for piece in x_s:
                spec_x[0] += piece.count('#')
                spec_x[1] += piece.count('.')
                spec_x[2] += 1 if piece[0] not in '#.*' else 0
            return spec_x

        return a if weight(a) > weight(b) else b

    def compare_02(self, a, b):
        def weight(x):
            return [
                len(re.findall(r'#\w+', x)),
                len(re.findall(r'\.\w+', x)),
                len(re.findall(r'(^| )\w+', x))
            ]

        return a if weight(a) > weight(b) else b

    def compare_03(self, a, b):
        def weight(x):
            weight_one = lambda y: (y.count('#'), y.count('.'), 1 if y[0] not in '#.*' else 0)
            return list(map(sum, list(zip(*list(map(weight_one, x.split()))))))

        return a if weight(a) > weight(b) else b


if __name__ == '__main__':
    sol = Solution()
    print((sol.compare_03('.x .y', '.foo.bar')))
