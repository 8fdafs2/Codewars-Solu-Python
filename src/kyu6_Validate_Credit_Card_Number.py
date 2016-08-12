class Solution():
    def __init__(self):
        self.validate = self.validate_01

    def validate_01(self, n):
        n = [int(d) for d in str(n)]
        len_n = len(n)
        for i in range(len_n % 2 != 0, len_n, 2):
            n[i] <<= 1
            if n[i] > 9:
                n[i] -= 9
        return sum(n) % 10 == 0

    def validate_02(self, n):
        n = [int(d) for d in str(n)]
        for i in range(len(n) - 2, -1, -2):
            n[i] <<= 1
            if n[i] > 9:
                n[i] -= 9
        return sum(n) % 10 == 0
