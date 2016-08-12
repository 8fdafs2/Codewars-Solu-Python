class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-sorted-merge

    Linked Lists - Sorted Merge

    Write a SortedMerge() function that takes two lists,
    each of which is sorted in increasing order,
    and merges the two together into one list which is in increasing order.
    SortedMerge() should return the new list.
    The new list should be made by splicing together the nodes of the first two lists.
    Ideally, SortedMerge() should only make one pass through each list.
    SortedMerge() is tricky to get right and it may be solved iteratively or recursively.

    var first = 2 -> 4 -> 6 -> 7 -> null
    var second = 1 -> 3 -> 5 -> 6 -> 8 -> null
    sortedMerge(first, second) === 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 6 -> 7 -> 8 -> null
    There are many cases to deal with: either 'first' or 'second' may be null/None/nil,
    during processing either 'first' or 'second' may run out first,
    and finally there's the problem of starting the result list empty,
    and building it up while going through 'first' and 'second'.

    If one of the argument lists is null,
    the returned list should be the other linked list (even if it is also null).
    No errors need to be thrown in SortedMerge().

    Try doing Linked Lists - Shuffle Merge before attempting this problem.

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

    def sorted_merge_01(self, first, second):
        """
        """
        if not first:
            return second
        if not second:
            return first

        if first.data < second.data:
            node_new = node = Node(first.data)
            first = first.next
        else:
            node_new = node = Node(second.data)
            second = second.next

        while first or second:
            if not first:
                node.next = second
                return node_new
            if not second:
                node.next = first
                return node_new

            if first.data < second.data:
                node.next = Node(first.data)
                node = node.next
                first = first.next
            else:
                node.next = Node(second.data)
                node = node.next
                second = second.next

        return node_new


    def sorted_merge_02(self, first, second):
        """
        """
        def recur(first, second):

            if not first:
                return second
            if not second:
                return first

            if first.data <= second.data:
                node_new = Node(first.data)
                node_new.next = recur(first.next, second)
            else:
                node_new = Node(second.data)
                node_new.next = recur(first, second.next)

            return node_new

        return recur(first, second)