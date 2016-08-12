from functools import reduce, partial


class Solution():
    """
    https://www.codewars.com/kata/52e864d1ffb6ac25db00017f

    Construct a function that,
    when given a string containing an expression in infix notation,
    will return an identical expression in postfix notation.

    The operators used will be +, -, *, /, and ^ with standard precedence rules
    and left-associativity of all operators but ^.

    The operands will be single-digit integers between 0 and 9, inclusive.

    Parentheses may be included in the input, and are guaranteed to be in correct pairs.

    to_postfix("2+7*5") # Should return "275*+"
    to_postfix("3*3/(7+1)") # Should return "33*71+/"
    to_postfix("5+(6-2)*9+3^(7-1)") # Should return "562-9*+371-^+"

    You may read more about postfix notation, also called Reverse Polish notation,
    here: http://en.wikipedia.org/wiki/Reverse_Polish_notation
    """

    def __init__(self):
        pass

    def to_postfix_01(self, infix):
        """
        recursion, w/ priority, left to right
        """

        def recur(infix):

            if len(infix) == 3:
                return infix[0] + infix[2] + infix[1]

            stack = [[], ]
            for token in infix:
                if token == '(':
                    stack.append([])
                    continue
                elif token == ')':
                    token = recur(stack.pop())
                stack[-1].append(token)
            infix = stack[-1]

            for ops in ('^', '*/', '+-'):
                stack = [[], ]
                for token in infix:
                    if token in ops:
                        stack.append([stack[-1].pop(), token])
                        continue
                    elif stack[-1] and stack[-1][-1] in ops:
                        token = recur(stack.pop() + [token, ])
                    stack[-1].append(token)
                infix = stack[-1]

            return stack[-1][-1]

        return recur(infix)

    def to_postfix_02(self, infix):
        """
        ...
        """
        tokens = list(reversed(infix))

        def accept(sym):
            if tokens and tokens[-1] in sym:
                return tokens.pop()

        def accept_while(sym):
            while tokens and tokens[-1] in sym:
                yield tokens.pop()

        def parse(lvl, next_handler):
            return reduce(lambda e, op: (lambda b: lambda: e() + b() + op)(next_handler()),
                          accept_while(lvl), next_handler())

        def paren():
            if accept('('):
                return (expression(), accept(')'))[0]
            return (lambda n: lambda: n)(accept('0123456789'))

        factor = partial(parse, '^', paren)
        term = partial(parse, '*/', factor)
        expression = partial(parse, '+-', term)

        return expression()()

    def to_postfix_03(self, infix):
        """
        for-loop, left to right
        """
        priority_op = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack_op = []
        postfix = []
        for token in infix:
            if token in '0123456789':
                postfix.append(token)
            elif token == '(':
                stack_op.append(token)
            # extract operators from last parentheses in reversed order
            elif token == ')':
                while stack_op[-1] != '(':
                    postfix.append(stack_op.pop())
                stack_op.pop()
            else:
                # extract operators from last parentheses in reversed order
                # if the to-be-extract operator has priority over or equal to current operator
                while stack_op and priority_op[stack_op[-1]] >= priority_op[token]:
                    postfix.append(stack_op.pop())
                stack_op.append(token)

        # extract remained operators in reversed order
        while stack_op:
            postfix.append(stack_op.pop())
        return ''.join(postfix)


def infix_gen(i, nested_parentheses=True, nums='123456789', ops='+-*/^'):
    import random
    cs = '() '
    stack = []
    infix = []

    i = ((i - 3) // 2) * 2 + 3

    for j in range(i):
        if j % 2 == 0:
            num = random.choice(nums)
            c = random.choice(cs)
            if c == ')' and stack:
                infix.append(num)
                infix.append(')')
                stack.pop()
            elif c == '(' and (not stack or nested_parentheses):
                infix.append('(')
                infix.append(num)
                stack.append(1)
            else:
                infix.append(num)
        else:
            infix.append(random.choice(ops))
    for _ in stack:
        infix.append(')')

    return ''.join(infix)


def sets_gen(to_postfix):
    test_sets = []
    for i in range(3, 500):
        infix = infix_gen(i)
        match = to_postfix(infix)
        test_sets.append((
            (infix,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(10, prt_docstr=True)
