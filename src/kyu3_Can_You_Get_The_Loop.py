from itertools import count


class Node():

    def __init__(self):
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/52a89c2ea8ddc5547a000863

    You are given a node that is the beginning of a linked list.
    This list always contains a tail and a loop.
    Your objective is to determine the length of the loop.
    For example in the following picture the tail's size is 3 and
    the loop size is 11.
    ......
    You are given a node that is the beginning of a linked list.
    This list always contains a tail and a loop.
    Your objective is to determine the length of the loop.
    For example in the following picture the tail's size is 3 and
    the loop size is 11.

    # Use the `next' attribute to get the following node

    node.next
    """

    def __init__(self):
        pass

    def loop_size_01(self, node):
        """
        hashtab
        """
        hashtab = {}
        i = 0
        while True:
            if node not in hashtab:
                hashtab[node] = i
                node = node.next
                i += 1
            else:
                return i - hashtab[node]

    def loop_size_02(self, node):
        """
        turtle and rabbit
        """
        slower = faster = node
        while True:
            slower = slower.next
            faster = faster.next.next
            if slower is faster:
                break
            faster = faster.next
            if slower is faster:
                break
        ret = 0
        while True:
            faster = faster.next
            ret += 1
            if faster is slower:
                return ret

    def loop_size_03(self, node):
        """
        property addition
        """
        for i in count():
            node.i = i
            try:
                return node.i - node.next.i + 1
            except AttributeError:
                node = node.next


def sets_gen(loop_size):
    import random
    test_sets = []
    for i in range(10, 100):
        nodes = [Node() for _ in range(i)]
        for node, next_node in zip(nodes, nodes[1:]):
            node.next = next_node
        nodes[-1].next = nodes[random.randint(0, i - 2)]
        node = nodes[0]
        match = loop_size(node)
        test_sets.append((
            (node,),
            match
        ))
    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(1000, prt_docstr=True)
