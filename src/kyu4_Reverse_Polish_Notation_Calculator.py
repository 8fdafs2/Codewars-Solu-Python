import operator


class Solution():
    """
    https://www.codewars.com/kata/52f78966747862fc9a0009ae

    Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

    For example expression:
        5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation)
    should evaluate to 14.

    Note that for simplicity you may assume that there are always spaces between numbers and operations,
    e.g. 1 3 + expression is valid, but 1 3+ isn't.

    Empty expression should evaluate to 0.

    Valid operations are +, -, *, /.

    You may assume that there won't be exceptional situations (like stack underflow or division by zero).
    """
    def __init__(self):
        pass

    def calc_01(self, expr):
        """
        eval
        """
        if not expr:
            return 0
        stack = []
        for token in expr.split():
            if token not in '+-*/':
                stack.append(token)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append('(' + b + token + a + ')')
        return eval(stack[-1])

    def calc_02(self, expr):
        """
        op_map
        """
        if not expr:
            return 0
        op_map = {
            '+': operator.add,  # lambda x, y: x + y
            '-': operator.sub,  # lambda x, y: x - y
            '*': operator.mul,  # lambda x, y: x * y
            '/': operator.truediv,  # lambda x, y: x / y
        }
        stack = []
        for token in expr.split():
            if token not in op_map:
                stack.append(float(token))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(op_map[token](b, a))
        return stack[-1]


def sets_gen(calc):
    import random
    ops = '+-*/'
    test_sets = []
    for i in range(1, 500, 2):

        while True:
            expr = []
            n_op = -1
            for j in range(i):
                if i - j == n_op:
                    expr.append(random.choice(ops))
                    n_op -= 1
                elif n_op > 0 and random.choice((True, False)):
                    expr.append(random.choice(ops))
                    n_op -= 1
                else:
                    expr.append(str(random.randint(1, 9)))
                    n_op += 1
            expr = ' '.join(expr)
            try:
                match = calc(expr)
            except ZeroDivisionError:
                pass
            else:
                break

        test_sets.append((
            (expr,),
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
