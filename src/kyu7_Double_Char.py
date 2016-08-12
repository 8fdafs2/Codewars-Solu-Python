class Solution():
    def __init__(self):
        self.double_char = self.double_char_01

    def double_char_01(self, s):
        ret = ''
        for c in s:
            ret += c + c
        return ret