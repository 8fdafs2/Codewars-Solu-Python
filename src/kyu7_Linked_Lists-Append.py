class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-append

    Linked Lists - Append

    Write an Append() function which appends one linked list to another.
    The head of the resulting list should be returned.

    If both listA and listB are null/None/nil, return null/None/nil.
    If one list is null/None/nil and the other is not, simply return the non-null/None/nil list.

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

    Inspired by Stanford Professor Nick Parlante's excellent Linked List teachings.
    """

    def __init__(self):
        pass

    def append_01(self, listA, listB):
        """
        intuitive
        """
        if not listA:
            return listB
        if not listB:
            return listA

        node = listA
        while node.next:
            node = node.next
        node.next = listB

        return listA

    def append_02(self, listA, listB):
        """
        recursion
        """
        def recur(listA, listB):
            if not listA:
                return listB
            listA.next = recur(listA.next, listB)
            return listA

        return recur(listA, listB)

