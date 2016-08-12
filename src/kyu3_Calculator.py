import operator
import decimal
import re
from functools import reduce


class Solution():
    """
    https://www.codewars.com/kata/5235c913397cbf2508000048

    Create a simple calculator that given a string of operators (+ - * and /)
    and numbers separated by spaces returns the value of that expression

    Example:

    Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7

    Remember about the order of operations!
    Multiplications and divisions have a higher priority and should be performed left-to-right.
    Additions and subtractions have a lower priority and should also be performed left-to-right.

    """

    def __init__(self):
        pass

    def evaluate_01(self, string):
        """
        two-pass, stack
        """
        mp_op = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 }

        stack = ['', '', ]
        for token in string.split():
            if token not in mp_op:
                token = decimal.Decimal(token)
                if stack[-1] in '*/' and isinstance(stack[-2], decimal.Decimal):
                    stack.append(mp_op[stack.pop()](stack.pop(), token))
                    continue
            stack.append(token)

        for i in range(2, len(stack) - 1, 2):
            stack[i + 2] = mp_op[stack[i + 1]](stack[i], stack[i + 2])

        return float(stack[-1])

    def evaluate_02(self, string):
        """
        eval, round, precision issue
        """
        return round(eval(string), 16)

    def evaluate_03(self, string):
        """
        eval, decimal
        """
        return float(eval(re.sub(r'([\d.]+)', r'decimal.Decimal("\1")', string)))

    def evaluate_04(self, string):
        """
        recursion, w/ priority
        """
        mp_op = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 }

        def recur(tokens):
            n = len(tokens)
            if n == 1:
                return decimal.Decimal(tokens[0])
            for ops in ('+-', '*/'):
                for i in reversed(range(n)):
                    token = tokens[i]
                    if token in ops:
                        return mp_op[token](recur(tokens[:i]), recur(tokens[i + 1:]))

        return float(recur(string.split()))


def sets_gen(evaluate):
    import random
    test_sets = []
    for i in range(3, 1000, 2):
        string = []
        for j in range(i):
            if j % 2 == 0:
                string.append(random.choice(('-', '')) + str(random.randint(1, 9)))
            else:
                string.append(random.choice('+-*/'))
        string = ' '.join(string)
        match = evaluate(string)
        test_sets.append((
            (string,),
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
