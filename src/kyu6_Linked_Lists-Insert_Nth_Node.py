class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-insert-nth-node

    Linked Lists - Insert Nth

    Implement an InsertNth() function which can insert a new node at any index within a list.

    InsertNth() is a more general version of the Push() function that we implemented in the first kata listed below.
    Given a list, an index 'n' in the range 0..length, and a data element,
    add a new node to the list so that it has the given index. InsertNth() should return the head of the list.

    insertNth(1 -> 2 -> 3 -> null, 0, 7) === 7 -> 1 -> 2 -> 3 -> null)
    insertNth(1 -> 2 -> 3 -> null, 1, 7) === 1 -> 7 -> 2 -> 3 -> null)
    insertNth(1 -> 2 -> 3 -> null, 3, 7) === 1 -> 2 -> 3 -> 7 -> null)
    You must throw/raise an exception if the index is too large.

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

    def insert_nth_01(self, head, index, data):
        """
        """
        if index < 0:
            raise IndexError

        node_new = Node(data)

        if index == 0:
            node_new.next = head
            return node_new

        node = head
        for i in range(index - 1):
            node = node.next
            if not node:
                raise IndexError
        node_new.next = node.next
        node.next = node_new

        return head

    def insert_nth_02(self, head, index, data):
        """
        """

        node_new = Node(data)

        def recur(node, index):
            if index < 0:
                raise IndexError

            if index == 0:
                node_new.next = node
                return node_new

            node.next = recur(node.next, index - 1)

            return head

        return recur(head, index)
