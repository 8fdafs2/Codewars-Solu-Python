class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def front_back_split(source, front, back):
    if not source or not front or not back:
        raise ValueError
    if not source.next:
        raise ValueError

    slow, fast = source, source.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    back.data = slow.next.data
    back.next = slow.next.next

    slow.next = None

    front.data = source.data
    front.next = source.next


def sorted_merge(first, second):
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


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-merge-sort

    Linked Lists - Merge Sort

    Write a MergeSort() function which recursively sorts a list in ascending order.
    Note that this problem requires recursion.
    Given FrontBackSplit() and SortedMerge(), you can write a classic recursive MergeSort().
    Split the list into two smaller lists, recursively sort those lists,
    and finally merge the two sorted lists together into a single sorted list. Return the list.

    var list = 4 -> 2 -> 1 -> 3 -> 8 -> 9 -> null
    mergeSort(list) === 1 -> 2 -> 3 -> 4 -> 8 -> 9 -> null
    FrontBackSplit() and SortedMerge() need not be redefined. You may call these functions in your solution.

    These function names will depend on the accepted naming conventions of language you are using.
    In Python, FrontBackSplit() is actually front_back_split(). In JavaScript, it is frontBackSplit(), etc.

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

    def merge_sort_01(self, list):
        """
        """
        def recur(list):
            if not list:
                return None
            if not list.next:
                return list
            front = Node()
            back = Node()
            front_back_split(list, front, back)
            return sorted_merge(recur(front), recur(back))

        return recur(list)
