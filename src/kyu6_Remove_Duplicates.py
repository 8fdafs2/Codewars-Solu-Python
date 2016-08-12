class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-remove-duplicates

    Linked Lists - Remove Duplicates

    Write a RemoveDuplicates() function which takes a list sorted in increasing order and
    deletes any duplicate nodes from the list.
    Ideally, the list should only be traversed once. The head of the resulting list should be returned.

    var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
    removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null
    If the passed in list is null/None/nil, simply return null.

    Note: Your solution is expected to work on long lists. Recursive solutions may fail due to stack size limitations.

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

    def remove_duplicates_01(self, head):
        """
        """
        node = head
        node_prev = None
        while node:
            if node_prev and node.data == node_prev.data:
                node_prev.next = node.next
            else:
                node_prev = node
            node = node.next
        return head
