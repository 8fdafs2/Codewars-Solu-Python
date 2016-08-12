class Solution():
    def __init__(self):
        self.tribonacci = self.tribonacci_01

    def tribonacci_01(self, signature, n):

        tribs = list(signature[:n])

        for i in range(3, n):
            tribs.append(sum(tribs[-3:]))

        return tribs

    def tribonacci_02(self, signature, n):

        tribs = list(signature[:n])

        while len(tribs) < n:
            tribs.append(sum(tribs[-3:]))

        return tribs
