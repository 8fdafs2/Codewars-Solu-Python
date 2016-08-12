class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-shuffle-merge

    Linked Lists - Shuffle Merge

    Write a ShuffleMerge() function that takes two lists and merges their nodes together to make one list,
    taking nodes alternately between the two lists.
    So ShuffleMerge() with 1 -> 2 -> 3 -> null and 7 -> 13 -> 1 -> null should
    yield 1 -> 7 -> 2 -> 13 -> 3 -> 1 -> null.
    If either list runs out, all the nodes should be taken from the other list.
    ShuffleMerge() should return the new list.
    The solution depends on being able to move nodes to the end of a list.

    var first = 3 -> 2 -> 8 -> null
    var second = 5 -> 6 -> 1 -> 9 -> 11 -> null
    shuffleMerge(first, second) === 3 -> 5 -> 2 -> 6 -> 8 -> 1 -> 9 -> 11 -> null
    If one of the argument lists is null,
    the returned list should be the other linked list (even if it is also null).
    No errors need to be thrown in ShuffleMerge().

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

    def shuffle_merge_01(self, first, second):
        """
        """
        if not first:
            return second
        if not second:
            return first

        node_new = node = Node(first.data)
        node.next = Node(second.data)
        node = node.next
        first = first.next
        second = second.next

        while first or second:
            if first:
                node.next = Node(first.data)
                node = node.next
                first = first.next
            if second:
                node.next = Node(second.data)
                node = node.next
                second = second.next

        return node_new



