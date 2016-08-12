class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-sorted-insert

    Linked Lists - Sorted Insert

    Write a SortedInsert() function which inserts a node into the correct location of a pre-sorted linked list which
    is sorted in ascending order.
    SortedInsert takes the head of a linked list and data used to create a node as arguments.
    SortedInsert() should also return the head of the list.

    sortedInsert(1 -> 2 -> 3 -> null, 4) === 1 -> 2 -> 3 -> 4 -> null)
    sortedInsert(1 -> 7 -> 8 -> null, 5) === 1 -> 5 -> 7 -> 8 -> null)
    sortedInsert(3 -> 5 -> 9 -> null, 7) === 3 -> 5 -> 7 -> 9 -> null)
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

    def sorted_insert_01(self, head, data):
        """
        """
        node_new = Node(data)

        node = head
        node_prev = None
        while node:
            if node.data > data:
                break
            node_prev = node
            node = node.next

        node_new.next = node
        if not node_prev:
            return node_new

        node_prev.next = node_new
        return head

    def sorted_insert_02(self, head, data):
        """
        """
        def recur(node, data):
            if not node:
                return Node(data)
            if node.data > data:
                node_new = Node(data)
                node_new.next = node
                return node_new
            node.next = recur(node.next, data)
            return node

        return recur(head, data)
