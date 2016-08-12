class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-recursive-reverse

    Linked Lists - Recursive Reverse

    Write a Recursive Reverse() function that recursively reverses a linked list.
    You may want to use a nested function for the recursive calls.

    var list = 2 -> 1 -> 3 -> 6 -> 5 -> null
    reverse(list) === 5 -> 6 -> 3 -> 1 -> 2 -> null
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

    def reverse_01(self, head):
        """
        """
        def recur(head):
            if not head:
                return None
            if not head.next:
                return Node(head.data)

            node_new = node = recur(head.next)
            while node.next:
                node = node.next
            node.next = Node(head.data)

            return node_new

        return recur(head)

    def reverse_02(self, head):
        """
        """
        def recur(head, next=None):
            if not head:
                return None
            if not head.next:
                node = Node(head.data)
                node.next = next
                return node
            node = Node(head.data)
            node.next = next
            return recur(head.next, node)

        return recur(head)
