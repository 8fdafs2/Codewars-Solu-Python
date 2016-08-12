class Solution():
    def __init__(self):
        self.longest_consec = self.longest_consec_01

    def longest_consec_01(self, strarr, k):
        lens = [len(s) for s in strarr]
        len_lens = len(lens)
        if len_lens == 0 or k > len_lens or k <= 0:
            return ''
        if k == 1:
            return strarr[lens.index(max(lens))]
        sums = [sum(lens[i:i + k]) for i in range(len_lens - k + 1)]
        i = sums.index(max(sums))
        return ''.join(strarr[i:i + k])

    def longest_consec_02(self, strarr, k):
        len_strarr = len(strarr)
        if len_strarr == 0 or k > len_strarr or k <= 0:
            return ''
        strs = [''.join(strarr[i:i + k]) for i in range(len_strarr - k + 1)]
        return max(strs, key=lambda x: len(x))


if __name__ == '__main__':
    sol = Solution()
    print((
    sol.longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)))
