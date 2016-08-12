import re


class Solution():
    """
    https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
    Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
    Any whitespace at the end of the line should also be stripped out.
    """

    def __init__(self):
        pass

    # regex solution
    def solution_01(self, string, markers):
        """
        regex solution, process the whole string
        """
        if markers:
            return re.sub(r'([\t ]*(' + '|'.join(['(' + re.escape(m) + ')' for m in markers]) + r')[^\n]*)', r'',
                          string)
        return string

    # string solution
    def solution_02(self, string, markers):
        """
        string solution, take line's portion right before the found markers
        """
        if not markers:
            return string
        lines = []
        for line in string.split('\n'):
            pos_lst = [pos for pos in [line.find(m) for m in markers] if pos > -1]
            if pos_lst:
                lines.append(line[:min(pos_lst)].rstrip())
            else:
                lines.append(line)
        return '\n'.join(lines)

    # string solution
    def solution_03(self, string, markers):
        """
        string solution, take line's portion right before the found markers
        """
        if not markers:
            return string
        lines = []
        for line in string.split('\n'):
            for m in markers:
                pos = line.find(m)
                if pos > -1:
                    line = line[:pos].rstrip()
            lines.append(line)
        return '\n'.join(lines)

    # regex solution
    def solution_04(self, string, markers):
        """
        regex solution, process each line by explicit specify the MULTILINE flag
        """
        if markers:
            return re.sub(r'([\t ]*(' + '|'.join(['(' + re.escape(m) + ')' for m in markers]) + r').*$)', r'',
                          string, flags=re.MULTILINE)
        return string

    # string solution
    def solution_05(self, string, markers):
        """
        string solution, take first segment of line-splitting line by line
        """
        if markers:
            def lineproc(line, seps):
                for sep in seps:
                    line_segs = line.split(sep)
                    if len(line_segs) > 1:
                        line = line_segs[0].rstrip()
                    else:
                        line = line
                return line

            return '\n'.join([lineproc(line, markers) for line in string.split('\n')])

        return string


def sets_gen(solution):
    import random

    symbols = ['!#', '@', '\'', '"', '?', '=', '-', '.', ',', '|', '*', '//', 'COM']
    test_sets = []
    for i in range(1000):
        markers = random.sample(symbols, random.randint(0, 3))
        string = '\n'.join([''.join([random.choice('abcdefg' + ''.join(markers) + ' \t') for _ in
                                     range(random.randrange(0, 20))]) for _ in range(random.randrange(0, 5))])
        match = solution(string, markers)
        test_sets.append((string, markers, match))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(100, prt_docstr=True)
