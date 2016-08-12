class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-length-and-count

    Linked Lists - Length & Count

    Implement Length() to count the number of nodes in a linked list.

    length(null) === 0
    length(1 -> 2 -> 3 -> null) === 3
    Implement Count() to count the occurrences of an integer in a linked list.

    count(null, 1) === 0
    count(1 -> 2 -> 3 -> null, 1) === 1
    count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) === 4
    I've decided to bundle these two functions within the same Kata since they are both very similar.

    The push() and buildOneTwoThree() functions do not need to be redefined.

    Related Kata in order of expected completion (increasing difficulty):
    Linked Lists - Push & BuildOneTwoThree
    Linked Lists - Length & Count
    Linked Lists - Get Nth Node
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
    """

    def __init__(self):
        pass

    def length_01(self, node):
        i = 0
        while node:
            i += 1
            node = node.__next__
        return i

    def count_01(self, node, data):
        i = 0
        while node:
            if node.data == data:
                i += 1
            node = node.__next__
        return i

    def _cnt_02(self, node, func):
        i = 0
        while node:
            if func(node):
                i += 1
            node = node.__next__
        return i

    def length_02(self, node):
        return self._cnt_02(node, lambda node: True)

    def count_02(self, node, data):
        return self._cnt_02(node, lambda node: node.data == data)
