class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-sorted-intersect

    Linked Lists - Sorted Intersect

    Write a SortedIntersect() function which creates and returns a list representing
    the intersection of two lists that are sorted in increasing order.
    Ideally, each list should only be traversed once.
    The resulting list should not contain duplicates.

    var first = 1 -> 2 -> 2 -> 3 -> 3 -> 6 -> null
    var second = 1 -> 3 -> 4 -> 5 -> -> 6 -> null
    sortedIntersect(first, second) === 1 -> 3 -> 6 -> null
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

    def sorted_intersect_01(self, first, second):
        """
        """
        if not first or not second:
            return None

        node_new = None

        while first and second:

            if first.data == second.data:
                if node_new and node_new.data != first.data:
                    node.next = Node(first.data)
                    node = node.next
                else:
                    node_new = node = Node(first.data)
                first = first.next
                second = second.next
            elif first.data < second.data:
                first = first.next
            else:
                second = second.next

        return node_new
