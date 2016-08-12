class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-iterative-reverse

    Linked Lists - Iterative Reverse

    Write an iterative Reverse() function that reverses a linked list.
    Ideally, Reverse() should only need to make one pass of the list.

    var list = 2 -> 1 -> 3 -> 6 -> 5 -> null
    reverse(list)
    list === 5 -> 6 -> 3 -> 1 -> 2 -> null
    The push() and buildOneTwoThree() functions need not be redefined.

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

    Inspired by Stanford Professor Nick Parlante's
    excellent Linked List teachings.
    """

    def __init__(self):
        pass

    def reverse_01(self, head):
        """
        """
        if not head:
            return None

        node = head
        node_new = None
        while node:
            if node_new:
                node_ = node_new
                node_new = Node(node.data)
                node_new.next = node_
            else:
                node_new = Node(node.data)
            node = node.next

        head.data = node_new.data
        head.next = node_new.next
