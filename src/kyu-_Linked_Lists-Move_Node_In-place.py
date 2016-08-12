class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-move-node-in-place

    Linked Lists - Move Node In-place

    Write a MoveNode() function which takes the node from the front of the source list and
    moves it to the front of the destintation list.
    This problem should be done after Linked Lists - Move Node.

    JavaScript

    var source = 1 -> 2 -> 3 -> null
    var dest = 4 -> 5 -> 6 -> null
    moveNode(source, dest)
    source === 2 -> 3 -> null
    dest === 1 -> 4 -> 5 -> 6 -> null
    You should throw an error if any of the following conditions exist:

    The source argument is null.
    The dest argument is null.
    The source argument is an "empty" node with a null data attribute.
    Unlike the Linked Lists - Move Node kata, we are not returning a Context object but
    rather we are changing two objects in-place. We are also introducing the concept of an emtpy Node object whose
    data attribute is set to null.
    Passing in an empty node rather than null for the dest argument to indicate an empty destination list enables
    members/attributes of dest to be mutated within the function with the side effect of
    changing the destination list outside of the function.

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

    def move_node_01(self, source, dest):
        """
        """
        if not source or not dest:
            raise ValueError
        if not source.data:
            raise ValueError

        data = source.data

        if source.next:
            source.data = source.next.data
            source.next = source.next.next
        else:
            source.data = None

        if dest.data is not None:
            node_new = Node(dest.data)
            node_new.next = dest.next
            dest.data = data
            dest.next = node_new
        else:
            dest.data = data
