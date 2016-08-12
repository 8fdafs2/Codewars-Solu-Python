import itertools

class Solution():
    def __init__(self):
        self.sum_consecutives = self.sum_consecutives_01

    def sum_consecutives_01(self, s):

        ret = []
        prev = None
        for num in s:
            if num != prev:
                ret.append(num)
                prev = num
            else:
                ret[-1] += num
        return ret

    def sum_consecutives_02(self, s):
        ret = [s[0]]
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                ret[-1] += s[i]
            else:
                ret.append(s[i + 1])
        return ret


    def sum_consecutives_03(self, s):

        return [sum(gp) for _, gp in itertools.groupby(s)]


if __name__ == '__main__':
    sol = Solution()
    print((sol.sum_consecutives([1,4,4,4,0,4,3,3,1])))