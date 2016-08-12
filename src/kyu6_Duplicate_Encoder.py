class Solution():
    def __init__(self):
        self.duplicate_encode = self.duplicate_encode_01

    def duplicate_encode_01(self, word):
        word = word.lower()
        hashtab = {}
        for c in word:
            hashtab[c] = hashtab.get(c, 0) + 1
        ret = ''
        for c in word:
            if hashtab[c] == 1:
                ret += '('
            else:
                ret += ')'

        return ret

    def duplicate_encode_02(self, word):
        import string
        word = word.lower()
        notuse = set(string.printable) - set(word)
        word = word.replace('(', notuse.pop()).replace(')', notuse.pop())
        hashtab = {}
        for c in word:
            hashtab[c] = hashtab.get(c, 0) + 1
        for c, i in list(hashtab.items()):
            if i == 1:
                word = word.replace(c, '(')
            else:
                word = word.replace(c, ')')

        return word

    def duplicate_encode_03(self, word):
        word = word.lower()
        ret = ''
        for c in word:
            if word.count(c) == 1:
                ret += '('
            else:
                ret += ')'

        return ret


if __name__ == '__main__':
    sol = Solution()
    print((sol.duplicate_encode_02(' ( ( )')))