import textwrap


class Solution():
    """
    https://www.codewars.com/kata/537e18b6147aa838f600001b

    Your task in this Kata is to emulate text justification in monospace font.
    You will be given a single-lined text and the expected justification width.
    The longest word will never be greater than this width.

    Here are the rules:

        Use spaces to fill in the gaps between words.
        Each line should contain as many words as possible.
        Use '\n' to separate lines.
        Gap between words can't differ by more than one space.
        Lines should end with a word not a space.
        '\n' is not included in the length of a line.
        Large gaps go first, then smaller ones: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 spaces).
        Last line should not be justified, use only one space between words.
        Last line should not contain '\n'
        Strings with one word do not need gaps ('somelongword\n').

    Example with width=30:

        Lorem  ipsum  dolor  sit amet,
        consectetur  adipiscing  elit.
        Vestibulum    sagittis   dolor
        mauris,  at  elementum  ligula
        tempor  eget.  In quis rhoncus
        nunc,  at  aliquet orci. Fusce
        at   dolor   sit   amet  felis
        suscipit   tristique.   Nam  a
        imperdiet   tellus.  Nulla  eu
        vestibulum    urna.    Vivamus
        tincidunt  suscipit  enim, nec
        ultrices   nisi  volutpat  ac.
        Maecenas   sit   amet  lacinia
        arcu,  non dictum justo. Donec
        sed  quam  vel  risus faucibus
        euismod.  Suspendisse  rhoncus
        rhoncus  felis  at  fermentum.
        Donec lorem magna, ultricies a
        nunc    sit    amet,   blandit
        fringilla  nunc. In vestibulum
        velit    ac    felis   rhoncus
        pellentesque. Mauris at tellus
        enim.  Aliquam eleifend tempus
        dapibus. Pellentesque commodo,
        nisi    sit   amet   hendrerit
        fringilla,   ante  odio  porta
        lacus,   ut   elementum  justo
        nulla et dolor.

    Also you can always take a look at
    how justification works in your text editor or directly in HTML (css: text-align: justify).

    Have fun :)
    """

    def __init__(self):
        pass

    def justify_01(self, text, width):
        """
        intuitive
        """
        lines = []
        line = []
        len_line = 0
        for word in text.split():
            len_word = len(word)
            if len_line + len_word <= width:
                line.append(word)
                len_line += len_word + 1
            else:
                n_gp = len(line) - 1
                n_sp_ex = width - len_line + 1
                if n_gp > 0:
                    j = 0
                    for k in range(n_sp_ex):
                        line[j] += ' '
                        if j < n_gp - 1:
                            j += 1
                        else:
                            j = 0
                    lines.append(' '.join(line))
                else:
                    lines += line
                line = [word, ]
                len_line = len_word + 1

        if len_line == 0:
            lines.append(line)
        else:
            lines.append(' '.join(line))

        return '\n'.join(lines)

    def justify_02(self, text, width):
        """
        textwrap.wrap to preformat
        """
        lines = textwrap.wrap(text, width, break_on_hyphens=False)

        def line_justify(line):
            n_gp = line.count(' ')
            if n_gp == 0:
                return line
            n_sp = width - len(line) + n_gp
            n_sp_a, n_sp_b = divmod(n_sp, n_gp)
            _line_ = ''
            words = line.split()
            for i, word in enumerate(line.split()[:-1]):
                _line_ += word + ' ' * (n_sp_a + (i < n_sp_b))
            return _line_ + words[-1]

        return '\n'.join(list(map(line_justify, lines[:-1])) + [lines[-1], ])


def sets_gen(justify):
    import random
    import string
    test_sets = []
    for i in range(10, 100):
        text = ' '.join([''.join(
            random.sample(string.ascii_letters, random.randint(1, 8)) + random.sample(',.?!', random.randint(0, 1))) for
                         _ in range(i)])
        width = random.randint(9, 30)
        match = justify(text, width)
        test_sets.append((
            (text, width),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(100, prt_docstr=True)
