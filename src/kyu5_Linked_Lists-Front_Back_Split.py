class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-front-back-split

    Linked Lists - Front Back Split

    Write a FrontBackSplit() function that takes one list and splits it into two sublists — one for the front half,
    and one for the back half. If the number of elements is odd, the extra element should go in the front list.
    For example, FrontBackSplit() on the list 2 -> 3 -> 5 -> 7 -> 11 -> null should
    yield the two lists 2 -> 3 -> 5 -> null and 7 -> 11 -> null.
    Getting this right for all the cases is harder than it looks.
    You will probably need special case code to deal with lists of length < 2 cases.

    var source = 1 -> 3 -> 7 -> 8 -> 11 -> 12 -> 14 -> null
    var front = new Node()
    var back = new Node()
    frontBackSplit(source, front, back)
    front === 1 -> 3 -> 7 -> 8 -> null
    back === 11 -> 12 -> 14 -> null
    You should throw an error if any of the arguments to FrontBackSplit are null or if the source list has < 2 nodes.

    Hint. Probably the simplest strategy is to compute the length of the list,
    then use a for loop to hop over the right number of nodes to find the last node of the front half,
    and then cut the list at that point. There is a trick technique that uses two pointers to traverse the list.
    A "slow" pointer advances one nodes at a time, while the "fast" pointer goes two nodes at a time.
    When the fast pointer reaches the end, the slow pointer will be about half way.
    For either strategy, care is required to split the list at the right point.

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

    def front_back_split_01(self, source, front, back):
        """
        """
        if not source or not front or not back:
            raise ValueError
        if not source.next:
            raise ValueError

        slow = node = source

        while node.next:
            node = node.next
            if node.next:
                fast = node = node.next
            else:
                fast = node
                break

            slow = slow.next

        back.data = slow.next.data
        back.next = slow.next.next

        slow.next = None

        front.data = source.data
        front.next = source.next

    def front_back_split_02(self, source, front, back):
        """
        """
        assert (source and front and back)
        assert (source.data and source.next)

        slow, fast = source, source.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        back.data = slow.next.data
        back.next = slow.next.next

        slow.next = None

        front.data = source.data
        front.next = source.next


