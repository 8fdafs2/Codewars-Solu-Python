class Solution():
    def __init__(self):
        self.title_case = self.title_case_01

    def title_case_01(self, title, minor_words=''):
        words = title.capitalize().split()
        minor_words = minor_words.lower().split()
        ret = []
        for w in words:
            if w in minor_words:
                ret.append(w)
            else:
                ret.append(w.capitalize())

        return ' '.join(ret)

    def title_case_02(self, title, minor_words=''):
        words = title.capitalize().split()
        minor_words = minor_words.lower().split()
        return ' '.join([w if w in minor_words else w.capitalize() for w in words])


if __name__ == '__main__':
    sol = Solution()
    print((sol.title_case(title='a bc', minor_words='bc')))
