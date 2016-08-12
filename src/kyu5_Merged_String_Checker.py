class Solution():
    def __init__(self):
        self.is_merge = self.is_merge_01

    def is_merge_01(self, s, part1, part2):

        def recur(s, part1, part2):
            for i in range(len(s)):
                c = s[i]
                if part1 and c == part1[0]:
                    if part2 and c == part2[0]:
                        if recur(s[i + 1:], part1, part2[1:]):
                            return True
                    part1 = part1[1:]
                elif part2 and c == part2[0]:
                    part2 = part2[1:]
                else:
                    return False
            if part1 or part2:
                return False
            return True

        return recur(s, part1, part2)

    def is_merge_02(self, s, part1, part2):

        def recur(s, part1, part2):
            if not part1:
                return s == part2
            if not part2:
                return s == part1
            if not s:
                return part1 + part2 == ''
            if s[0] == part1[0] and recur(s[1:], part1[1:], part2):
                return True
            if s[0] == part2[0] and recur(s[1:], part1, part2[1:]):
                return True
            return False

        return recur(s, part1, part2)

    def is_merge_03(self, s, part1, part2):

        def recur(s, part1, part2):
            return not (s + part1 + part2) or \
                   s and part1 and s[0] == part1[0] and recur(s[1:], part1[1:], part2) or \
                   s and part2 and s[0] == part2[0] and recur(s[1:], part2[1:], part1)

        return recur(s, part1, part2)




if __name__ == '__main__':
    sol = Solution()
    print((sol.is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am')))