class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-get-nth-node

    Linked Lists - Get Nth

    Implement a GetNth() function that takes a linked list and an integer index and
    returns the node stored at the Nth index position. GetNth() uses the C numbering convention that
    the first node is index 0, the second is index 1, ... and so on.
    So for the list 42 -> 13 -> 666, GetNth() with index 1 should return Node(13);

    getNth(1 -> 2 -> 3 -> null, 0).data === 1
    getNth(1 -> 2 -> 3 -> null, 1).data === 2
    The index should be in the range [0..length-1].
    If it is not, GetNth() should throw/raise an exception.
    You should also raise an exception if the list is empty/null/None.

    Prerequisite Kata (may be in beta):

    Linked Lists - Push & BuildOneTwoThree
    Linked Lists - Length & Count
    The push() and buildOneTwoThree() functions do not need to be redefined.
    Related Kata in order of expected completion (increasing difficulty):

    Linked Lists - Push & BuildOneTwoThree
    Linked Lists - Length & Count
    Linked Lists Get Nth Node
    Linked Lists - Insert Nth Node
    Linked Lists - Sorted Insert
    Linked Lists - Insert Sort
    Linked Lists - Append
    Linked Lists - Remove Duplicates
    Linked Lists - Move Node
    Linked Lists - Move Node In-place
    Linked Lists - Alternating Split
    Linked Lists - Front Back Split
    Linked Lists - Shuffle Merge
    Linked Lists - Sorted Merge
    Linked Lists - Merge Sort
    Linked Lists - Sorted Intersect
    Linked Lists - Iterative Reverse
    Linked Lists - Recursive Reverse
    Inspired by Stanford Professor Nick Parlante's excellent Linked List teachings.

    http://cslibrary.stanford.edu/103/LinkedListBasics.pdf
    http://cslibrary.stanford.edu/105/LinkedListProblems.pdf
    """

    def __init__(self):
        pass

    def get_nth_01(self, node, index):
        """
        intuitive
        """
        if not node or index < 0:
            raise IndexError
        for i in range(index):
            node = node.next
            if not node:
                raise IndexError
        return node

    def get_nth_02(self, node, index):
        """
        """
        def recur(node, index):
            if not node or index < 0:
                raise IndexError
            if index == 0:
                return node
            return recur(node.next, index - 1)

        return recur(node, index)
