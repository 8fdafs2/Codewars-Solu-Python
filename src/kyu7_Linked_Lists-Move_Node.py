class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


class Solution():
    """
    https://www.codewars.com/kata/linked-lists-move-node

    Linked Lists - Move Node

    Write a MoveNode() function which takes the node from the front of the source list and
    moves it to the front of the destintation list. You should throw an error when the source list is empty.
    For simplicity, we use a Context object to store and return the state of the two linked lists.
    A Context object containing the two mutated lists should be returned by moveNode.

    MoveNode() is a handy utility function to have for later problems.

    JavaScript

    var source = 1 -> 2 -> 3 -> null
    var dest = 4 -> 5 -> 6 -> null
    moveNode(source, dest).source === 2 -> 3 -> null
    moveNode(source, dest).dest === 1 -> 4 -> 5 -> 6 -> null
    Python

    source = 1 -> 2 -> 3 -> None
    dest = 4 -> 5 -> 6 -> None
    move_node(source, dest).source == 2 -> 3 -> None
    move_node(source, dest).dest == 1 -> 4 -> 5 -> 6 -> None
    Ruby

    source = 1 -> 2 -> 3 -> nil
    dest = 4 -> 5 -> 6 -> nil
    move_node(source, dest).source == 2 -> 3 -> nil
    move_node(source, dest).dest == 1 -> 4 -> 5 -> 6 -> nil
    The push() and buildOneTwoThree() functions need not be redefined.

    There is another kata called Linked Lists - Move Node In-place that is related but more difficult.

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

        if not source:
            raise ValueError

        node = source
        source = source.next
        node.next = dest

        return Context(source, node)