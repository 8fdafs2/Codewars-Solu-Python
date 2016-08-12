class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
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


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-insert-sort

    Linked Lists - Insert Sort

    Write an InsertSort() function which rearranges nodes in a linked list so they are sorted in increasing order.
    You can use the SortedInsert() function that you created in the "Linked Lists - Sorted Insert" kata below.
    The InsertSort() function takes the head of a linked list as an argument and must return the head of the linked list.

    var list = 4 -> 3 -> 1 -> 2 -> null
    insertSort(list) === 1 -> 2 -> 3 -> 4 -> null
    If the passed in head node is null or a single node,
    return null or the single node, respectively.
    You can assume that the head node will always be either null,
    a single node, or a linked list consisting of multiple nodes.

    The push(), buildOneTwoThree(), and sortedInsert() functions need not be redefined.

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

    def insert_sort_01(self, head):
        """
        """
        node = head
        node_new = None
        while node:
            node_new = sorted_insert(node_new, node.data)
            node = node.next
        return node_new


