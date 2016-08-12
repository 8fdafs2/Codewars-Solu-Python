from functools import reduce


class Solution():
    """
    We all know about "balancing parentheses"
    (plus brackets, braces and chevrons) and even balancing characters that are identical.

    Read that last sentence again,
    I balanced different characters and identical characters twice and you didn't even notice... :)

    Kata

        Your challenge in this kata is to write a piece of code to validate that a supplied string is balanced.
        You must determine if all that is open is then closed, and nothing is closed which is not already open!
        You will be given a string to validate, and a second string,
        where each pair of characters defines an opening and closing sequence that needs balancing.
        You may assume that the second string always has an even number of characters.

    Example

        # In this case '(' opens a section, and ')' closes a section
        is_balanced("(Sensei says yes!)", "()")       # => True
        is_balanced("(Sensei says no!", "()")         # => False

        # In this case '(' and '[' open a section, while ')' and ']' close a section
        is_balanced("(Sensei [says] yes!)", "()[]")   # => True
        is_balanced("(Sensei [says) no!]", "()[]")    # => False

        # In this case a single quote (') both opens and closes a section
        is_balanced("Sensei says 'yes'!", "''")       # => True
        is_balanced("Sensei say's no!", "''")         # => False
    """

    def __init__(self):
        pass

    def is_balanced_01(self, source, caps):
        """
        intuitive
        """
        c_open = {}
        c_close = set()
        for i in range(0, len(caps), 2):
            c_open[caps[i]] = caps[i + 1]
            c_close.add(caps[i + 1])

        stack = []
        for c in source:
            if c in c_open and c in c_close:
                if stack:
                    if stack[-1] != c:
                        stack.append(c)
                    else:
                        stack.pop()
                else:
                    stack.append(c)
            elif c in c_open:
                stack.append(c_open[c])
            elif c in c_close:
                if not stack or stack.pop() != c:
                    return False

        return not stack

    def is_balanced_02(self, source, caps):
        """
        close_of
        """
        source = filter(lambda x: x in caps, source)
        # open -> close
        close_of = dict(zip(caps[::2], caps[1::2]))
        # store opens
        stack = []
        for cap in source:
            if stack and cap == close_of.get(stack[-1], ''):
                stack.pop()
            else:
                stack.append(cap)
        return not stack

    def is_balanced_03(self, source, caps):
        """
        open_of
        """
        source = filter(lambda x: x in caps, source)
        # close -> open
        open_of = dict(zip(caps[1::2], caps[::2]))
        # store closes
        stack = []
        for cap in source:
            if stack and stack[-1] == open_of.get(cap, ''):
                stack.pop()
            else:
                stack.append(cap)
        return not stack

    def is_balanced_04(self, source, caps):
        """
        open_of, reduce
        """
        # close -> open
        open_of = {c2: c1 for c1, c2 in zip(caps[0::2], caps[1::2])}

        def func_reduce(stack, e):
            if stack and stack[-1] == open_of.get(e):
                return stack[:-1]
            return stack + e

        return not reduce(func_reduce, [c for c in source if c in caps], '')


def sets_gen(is_balanced):
    args_sets = [
        ("(Sensei says yes!)", "()"),
        ("(Sensei says no!", "()"),
        ("(Sensei [says] yes!)", "()[]"),
        ("(Sensei [says) no!]", "()[]"),
        ("Sensei says 'yes'!", "''"),
        ("Sensei say's no!", "''"),

        ("Hello Mother can you hear me?", "()"),
        ("(Hello Mother can you hear me?)", "()"),
        ("(Hello Mother can you hear me?", ""),
        ("(Hello Mother can you hear me?", "()"),
        ("(Hello Mother can you hear me?))", "()"),
        (")Hello Mother can you hear me?", "()"),

        ("(Hello Mother can you hear me?)[Monkeys, in my pockets!!]", "()[]"),
        ("(Hello Mother can you hear me?)[Monkeys, in my pockets!!](Gosh!!)", "()[]"),
        ("Hello Mother can you hear me?)[Monkeys, in my pockets!!]", "()[]"),
        ("(Hello Mother can you hear me?[Monkeys, in my pockets!!]", "()[]"),
        ("(Hello Mother can you hear me?)Monkeys, in my pockets!!]", "()[]"),
        ("(Hello Mother can you hear me?)[Monkeys, in my pockets!!", "()[]"),

        ("((Hello))", "()"),
        ("(((Hello)))", "()"),
        ("((()Hello()))", "()"),
        ("((()Hello())", "()"),
        ("(()Hello()))", "()"),

        ("([{-Hello!-}])", "()[]{}"),
        ("([{([{Hello}])}])", "()[]{}"),
        ("([{-Hello!-})]", "()[]{}"),

        ("-Hello Mother can you hear me?-", "--"),
        ("-Hello Mother can you hear me?", "--"),
        ("Hello Mother can you hear me?-", "--"),

        ("-abcd-e@fghi@", "--@@"),
        ("abcd-e@fghi@", "--@@"),
        ("-abcde@fghi@", "--@@"),
        ("-abcd-efghi@", "--@@"),
        ("-abcd-e@fghi", "--@@"),

        ("-a@b@cd@e@fghi-", "--@@"),
        ("-ab@cd@e@fghi-", "--@@"),
        ("-a@bcd@e@fghi-", "--@@"),
        ("-a@b@cde@fghi-", "--@@"),
        ("-a@b@cd@efghi-", "--@@"),
        ("a@b@cd@e@fghi-", "--@@"),
        ("-a@b@cd@e@fghi", "--@@"),
    ]
    test_sets = []
    for args in args_sets:
        match = is_balanced(*args)
        test_sets.append((
            args,
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
