import re
import collections


class Solution():
    """
    https://www.codewars.com/kata/52f831fa9d332c6591000511

    For a given chemical formula represented by a string,
    count the number of atoms of each element contained in the molecule and return an object.

    For example:

    water = 'H2O'
    parse_molecule(water)                 # return {H: 2, O: 1}

    magnesium_hydroxide = 'Mg(OH)2'
    parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

    var fremy_salt = 'K4[ON(SO3)2]2'
    parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}

    As you can see, some formulas have brackets in them.
    The index outside the brackets tells you
    that you have to multiply count of each atom inside the bracket on this index.
    For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

    Note that brackets may be round, square or curly and can also be nested.
    Index after the braces is optional.
    """

    def __init__(self):
        pass

    def parse_molecule_01(self, formula):
        """
        intuitive, left-to-right
        """
        tokens = [None, None]
        for token in formula:
            if token.isupper():
                tokens.append(token)
            elif token.islower():
                tokens[-1] += token
            elif token.isdigit():
                if tokens[-1].isdigit():
                    tokens[-1] += token
                else:
                    tokens.append(token)
            elif token in '{[(':
                tokens.append(token)
            elif token in ')]}':
                tokens.append(token)

        len_tokens = len(tokens)

        stack = [{}]

        def stack_push():
            stack.append({})

        def stack_pop():
            _hashtab_ = stack.pop()
            hashtab = stack[-1]
            for token in _hashtab_:
                hashtab[token] = hashtab.get(token, 0) + _hashtab_[token]

        def stack_pop_if(i):
            if tokens[i - 1] and tokens[i - 1].isdigit():
                hashtab = stack[-1]
                if tokens[i - 2] and tokens[i - 2].isalpha():
                    hashtab[tokens[i - 2]] += int(tokens[i - 1]) - 1
                else:
                    for _token_ in hashtab:
                        hashtab[_token_] *= int(tokens[i - 1])
                    stack_pop()

        for i in range(2, len_tokens):
            token = tokens[i]
            if token.isalpha():
                stack_pop_if(i)
                hashtab = stack[-1]
                hashtab[token] = hashtab.get(token, 0) + 1
            elif token in '{[(':
                stack_pop_if(i)
                stack_push()
            elif token in ')]}':
                stack_pop_if(i)

        stack_pop_if(len_tokens)
        while len(stack) > 1:
            stack_pop()

        return stack[0]

    def parse_molecule_02(self, formula):
        """
        regex, right-to-left
        """
        tokens = re.findall(r'[A-Z][a-z]?|[()\[\]{}]|\d+', formula)
        hashtab = {}

        def parse_sub(tokens, scale=1):
            _scale_ = scale
            for token in tokens:
                if token in ')]}':
                    parse_sub(tokens, _scale_)
                elif token in '{[(':
                    break
                elif token.isdigit():
                    _scale_ = scale * int(token)
                    continue
                elif token.isalpha():
                    hashtab[token] = hashtab.get(token, 0) + _scale_
                _scale_ = scale

        parse_sub(iter(reversed(tokens)))
        return hashtab

    def parse_molecule_03(self, formula):
        """
        regex, expansion
        """
        while True:
            m = re.search(r'[\[({](\w+)[\])}](\d*)', formula)
            if not m:
                break
            if m.group(2):
                formula = re.sub(re.escape(m.group(0)), m.group(1) * int(m.group(2)), formula)
            else:
                formula = re.sub(re.escape(m.group(0)), m.group(1), formula)

        while True:
            m = re.search(r'([A-Z][a-z]?)(\d+)', formula)
            if not m:
                break
            formula = re.sub(m.group(0), m.group(1) * int(m.group(2)), formula)

        return collections.Counter(re.findall(r'[A-Z][a-z]?', formula))


def sets_gen(parse_molecule):
    test_sets = [
        [['H2O', ], ],
        [['B2H6', ], ],
        [['C6H12O6', ], ],
        [['Mo(CO)6', ], ],
        [['Mg(OH)2', ], ],
        [['Fe(C5H5)2', ], ],
        [['(C5H5)Fe(CO)2CH3', ], ],
        [['Pd[P(C6H5)3]4', ], ],
        [['K4[ON(SO3)2]2', ], ],
        [['As2{Be4C5[BCo3(CO2)3]2}4Cu5', ], ],
        [['{[Co(NH3)4(OH)2]3Co}(SO4)3', ], ]
    ]
    for m in test_sets:
        m.append(parse_molecule(*m[0]))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10000, prt_docstr=True)
