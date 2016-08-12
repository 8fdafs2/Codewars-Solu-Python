import re


class Solution():
    def __init__(self):
        self.to_weird_case = self.to_weird_case_01

    def to_weird_case_01(self, string):
        string = string.upper()
        words = string.split()
        ret = []
        for word in words:
            is_upper = True
            _word_ = ''
            for c in word:
                if is_upper:
                    _word_ += c
                else:
                    _word_ += c.lower()
                is_upper = not is_upper
            ret.append(_word_)

        return ' '.join(ret)

    def to_weird_case_02(self, string):
        string = string.upper()
        ret = ''
        is_upper = True
        for c in string:
            if c != ' ':
                if is_upper:
                    ret += c
                else:
                    ret += c.lower()
                is_upper = not is_upper
            else:
                ret += ' '
                is_upper = True

        return ret

    def to_weird_case_03(self, string):
        string = string.upper()
        ret = []
        for word in string.split():
            ret.append(''.join([c.lower() if i % 2 == 1 else c for i, c in enumerate(word)]))

        return ' '.join(ret)

    def to_weird_case_04(self, string):
        return re.sub(r'\w{2}|\w\s|\w$', lambda m: m.group().lower().capitalize(), string)




if __name__ == '__main__':
    pass
