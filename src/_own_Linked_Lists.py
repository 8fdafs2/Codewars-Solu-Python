class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def node2lst(node):
    data_lst = []
    while node:
        data_lst.append(node.data)
        node = node.next
    return data_lst


def node2lst_recur(node):
    if not node:
        return []
    return [node.data, ] + node2lst_recur(node.next)


def lst2node(data_lst):
    if not data_lst:
        return
    head = node = Node(data_lst[0])
    for data in data_lst[1:]:
        node.next = Node(data)
        node = node.next
    return head


def lst2node_recur(data_lst):
    if not data_lst:
        return None
    return Node(data_lst[0], lst2node_recur(data_lst[1:]))


if __name__ == '__main__':
    print('>>> node2lst/node2lst_recur/lst2node/lst2node_recur')
    data_lst = []
    n = lst2node([])
    print(node2lst(n), '==', data_lst)
    assert (node2lst(n) == data_lst)
    n = lst2node_recur([])
    print(node2lst_recur(n), '==', data_lst)
    assert (node2lst_recur(n) == data_lst)
    data_lst = [1, 2, 3]
    n = lst2node(data_lst)
    print(node2lst(n), '==', data_lst)
    assert (node2lst(n) == data_lst)
    n = lst2node_recur(data_lst)
    print(node2lst_recur(n), '==', data_lst)
    assert (node2lst_recur(n) == data_lst)


def length(node):
    i = 0
    while node:
        i += 1
        node = node.next
    return i


def count(node, data):
    i = 0
    while node:
        if node.data == data:
            i += 1
        node = node.next
    return i


if __name__ == '__main__':
    print('>>> length/count')
    data_lst = [1, 2, 3, 2, 1]
    n = lst2node(data_lst)
    print(length(n), '==', len(data_lst))
    assert (length(n) == len(data_lst))
    print(count(n, 1), '==', data_lst.count(1))
    assert (count(n, 1) == data_lst.count(1))
    print(count(n, 2), '==', data_lst.count(2))
    assert (count(n, 2) == data_lst.count(2))
    print(count(n, 3), '==', data_lst.count(3))
    assert (count(n, 3) == data_lst.count(3))


def get_nth(node, index):
    if not node or index < 0:
        raise IndexError
    for _ in range(index):
        node = node.next
        if not node:
            raise IndexError
    return node


def get_nth_recur(node, index):
    if not node or index < 0:
        raise IndexError
    if index == 0:
        return node
    return get_nth_recur(node.next, index - 1)


if __name__ == '__main__':
    print('>>> get_nth/get_nth_recur')
    data_lst = [1, 2, 3]
    n = lst2node(data_lst)
    for i, data in enumerate(data_lst):
        print(node2lst(get_nth(n, i))[0],
              '==', node2lst(get_nth_recur(n, i))[0],
              '==', data)
        assert (get_nth(n, i).data == get_nth_recur(n, i).data == data)


def append(first, second):
    if not first:
        return second
    if not second:
        return None
    node = first
    while node.next:
        node = node.next
    node.next = second
    return first


def append_recur(first, second):
    if not first:
        return second
    first.next = append_recur(first.next, second)
    return first


if __name__ == '__main__':
    print('>>> append/append_recur')
    data_a_lst = [1, 2, 3]
    data_b_lst = [4, 5, 6]
    data_c_lst = [7, 8, 9]
    data_a_b_lst = data_a_lst + data_b_lst
    data_a_b_c_lst = data_a_b_lst + data_c_lst
    n_a = lst2node(data_a_lst)
    n_b = lst2node(data_b_lst)
    n_c = lst2node(data_c_lst)
    n_a_b = append(n_a, n_b)
    print(node2lst(n_a_b), '==', data_a_b_lst)
    assert (node2lst(n_a_b) == data_a_b_lst)
    n_a_b_c = append_recur(n_a_b, n_c)
    print(node2lst(n_a_b_c), '==', data_a_b_c_lst)
    assert (node2lst(n_a_b_c) == data_a_b_c_lst)


def push(node, data):
    return Node(data, node)


if __name__ == '__main__':
    print('>>> push')
    data = 0
    data_lst = [1, 2, 3]
    n = lst2node(data_lst)
    n = push(n, data)
    print(node2lst(n), '==', [data, ] + data_lst)
    assert (node2lst(n) == [data, ] + data_lst)


def insert_nth(head, index, data):
    if index < 0:
        raise IndexError
    if index == 0:
        return Node(data, head)
    node = head
    for _ in range(index - 1):
        node = node.next
        if not node:
            raise IndexError
    node.next = Node(data, node.next)
    return head


def insert_nth_recur(head, index, data):
    if index < 0:
        raise IndexError
    if index == 0:
        return Node(data, head)
    head.next = insert_nth_recur(head.next, index - 1, data)
    return head


if __name__ == '__main__':
    print('>>> insert_nth/insert_nth_recur')
    data = 0
    data_lst = []
    n = lst2node(data_lst)
    for i in range(0, 3):
        data += 1
        n = insert_nth(n, i, data)
        n = insert_nth_recur(n, i, data)
        data_lst.insert(i, data)
        data_lst.insert(i, data)
        print(node2lst(n), '==', data_lst)
        assert (node2lst(n) == data_lst)


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


def sorted_insert_recur(head, data):
    if not head:
        return Node(data)
    if head.data > data:
        return Node(data, head)
    head.next = sorted_insert_recur(head.next, data)
    return head


if __name__ == '__main__':
    print('>>> sorted_insert/sorted_insert_recur')
    data = 0
    data_lst = []
    n = lst2node(data_lst)
    for i in range(0, 3):
        data += 1
        n = sorted_insert(n, data)
        n = sorted_insert_recur(n, data)
        data_lst.insert(i, data)
        data_lst.sort()
        data_lst.insert(i, data)
        data_lst.sort()
        print(node2lst(n), '==', data_lst)
        assert (node2lst(n) == data_lst)


def insert_sort(head):
    node = head
    node_new = None
    while node:
        node_new = sorted_insert(node_new, node.data)
        node = node.next
    return node_new


def insert_sort_recur(head):
    if not head:
        return head
    head.next = insert_sort_recur(head.next)
    return sorted_insert(head.next, head.data)


if __name__ == '__main__':
    print('>>> insert_sort/insert_sort_recur')
    data = 0
    data_lst = [3, 4, 2, 1, 6, 5]
    n = lst2node(data_lst)
    n = insert_sort(n)
    print(node2lst(n), '==', sorted(data_lst))
    assert (node2lst(n) == sorted(data_lst))
    n = lst2node(data_lst)
    n = insert_sort_recur(n)
    print(node2lst(n), '==', sorted(data_lst))
    assert (node2lst(n) == sorted(data_lst))


def remove_duplicates(head):
    node = head
    node_prev = None
    while node:
        if node_prev and node.data == node_prev.data:
            node_prev.next = node.next
        else:
            node_prev = node
        node = node.next
    return head


def remove_duplicates_recur(head, data=None):
    if not head:
        return None
    if head.data == data:
        return remove_duplicates_recur(head.next, data)
    head.next = remove_duplicates_recur(head.next, head.data)
    return head


if __name__ == '__main__':
    print('>>> remove_duplicates/remove_duplicates_recur')
    data = 0
    data_lst = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
    n = lst2node(data_lst)
    n = remove_duplicates(n)
    data_lst = list(set(data_lst))
    print(node2lst(n), '==', data_lst)
    assert (node2lst(n) == data_lst)
    data_lst = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
    n = lst2node(data_lst)
    n = remove_duplicates_recur(n)
    data_lst = list(set(data_lst))
    print(node2lst(n), '==', data_lst)
    assert (node2lst(n) == data_lst)


def move_node(source, dest):
    if not source:
        raise ValueError
    return source.next, Node(source.data, dest)


if __name__ == '__main__':
    print('>>> move_node')
    data_a_lst = [1, 2, 3]
    data_b_lst = [4, 5, 6]
    n_a = lst2node(data_a_lst)
    n_b = lst2node(data_b_lst)
    n_a, n_b = move_node(n_a, n_b)
    print(node2lst(n_a), '==', data_a_lst[1:])
    assert (node2lst(n_a) == data_a_lst[1:])
    print(node2lst(n_b), '==', [data_a_lst[0], ] + data_b_lst)
    assert (node2lst(n_b) == [data_a_lst[0], ] + data_b_lst)


def move_node_inplace(source, dest):
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
        node_new = Node(dest.data, dest.next)
        dest.data = data
        dest.next = node_new
    else:
        dest.data = data


if __name__ == '__main__':
    print('>>> move_node_inplace')
    data_a_lst = [1, 2, 3]
    data_b_lst = [4, 5, 6]
    n_a = lst2node(data_a_lst)
    n_b = lst2node(data_b_lst)
    n_a_id = id(n_a)
    n_b_id = id(n_b)
    move_node_inplace(n_a, n_b)
    print(node2lst(n_a), '==', data_a_lst[1:])
    assert (node2lst(n_a) == data_a_lst[1:])
    print(id(n_a), '==', n_a_id)
    assert (id(n_a) == n_a_id)
    print(node2lst(n_b), '==', [data_a_lst[0], ] + data_b_lst)
    assert (node2lst(n_b) == [data_a_lst[0], ] + data_b_lst)
    print(id(n_b), '==', n_b_id)
    assert (id(n_b) == n_b_id)


# def alternating_split(head):
#     if not head:
#         raise ValueError
#     if not head.next:
#         raise ValueError
#     node = head
#     first_prev = None
#     second_prev = None
#     while node:
#         first = Node(node.data)
#         if first_prev:
#             first_prev.next = first
#         else:
#             first_new = first
#         first_prev = first
#         if not node.next:
#             return first_new, second_new
#         node = node.next
#         second = Node(node.data)
#         if second_prev:
#             second_prev.next = second
#         else:
#             second_new = second
#         second_prev = second
#         node = node.next
#     return first_new, second_new


def alternating_split(head):
    if not head:
        raise ValueError
    if not head.next:
        raise ValueError
    first = first_new = head
    second = second_new = head.next
    head = head.next.next
    while head:
        first.next = head
        first = head
        if not head.next:
            return first_new, second_new
        head = head.next
        first.next = None
        second.next = head
        second = head
        head = head.next
        second.next = None
    return first_new, second_new


def alternating_split_recur(head, error_ignore=False):
    if not head:
        if error_ignore:
            return None, None
        raise ValueError
    if not head.next:
        if error_ignore:
            return head, None
        raise ValueError
    first = head
    second = head.next
    head = head.next.next
    first.next, second.next = alternating_split_recur(head, True)
    return first, second


if __name__ == '__main__':
    print('>>> alternating_split/alternating_split_recur')
    data_lst = [1, 2, 3, 4, 5, 6, 7]
    n = lst2node(data_lst)
    n_a, n_b = alternating_split(n)
    print(node2lst(n_a), '==', data_lst[::2])
    assert (node2lst(n_a) == data_lst[::2])
    print(node2lst(n_b), '==', data_lst[1::2])
    assert (node2lst(n_b) == data_lst[1::2])
    n = lst2node(data_lst)
    n_a, n_b = alternating_split_recur(n)
    print(node2lst(n_a), '==', data_lst[::2])
    assert (node2lst(n_a) == data_lst[::2])
    print(node2lst(n_b), '==', data_lst[1::2])
    assert (node2lst(n_b) == data_lst[1::2])


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


if __name__ == '__main__':
    print('>>> front_back_split')
    data_lst = [1, 2, 3, 4, 5, 6]
    n = lst2node(data_lst)
    n_a, n_b = Node(), Node()
    front_back_split(n, n_a, n_b)
    print(node2lst(n_a), '==', data_lst[:(len(data_lst) + 1) // 2])
    assert (node2lst(n_a) == data_lst[:(len(data_lst) + 1) // 2])
    print(node2lst(n_b), '==', data_lst[(len(data_lst) + 1) // 2:])
    assert (node2lst(n_b) == data_lst[(len(data_lst) + 1) // 2:])
    data_lst = [1, 2, 3, 4, 5, 6, 7]
    n = lst2node(data_lst)
    n_a, n_b = Node(), Node()
    front_back_split(n, n_a, n_b)
    print(node2lst(n_a), '==', data_lst[:(len(data_lst) + 1) // 2])
    assert (node2lst(n_a) == data_lst[:(len(data_lst) + 1) // 2])
    print(node2lst(n_b), '==', data_lst[(len(data_lst) + 1) // 2:])
    assert (node2lst(n_b) == data_lst[(len(data_lst) + 1) // 2:])


def shuffle_merge(first, second):
    if not first:
        return second
    if not second:
        return first
    node_new = node = Node(first.data, Node(second.data))
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


def shuffle_merge_recur(first, second):
    if not first:
        return second
    if not second:
        return first
    return Node(first.data, Node(second.data, shuffle_merge_recur(first.next, second.next)))


if __name__ == '__main__':
    print('>>> shuffle_merge/shuffle_merge_recur')
    data_a_lst = [1, 3, 5]
    data_b_lst = [2, 4, 6, 7, 8]
    n_a = lst2node(data_a_lst)
    n_b = lst2node(data_b_lst)
    n_a_b = shuffle_merge(n_a, n_b)
    print(node2lst(n_a_b), '==', [1, 2, 3, 4, 5, 6, 7, 8])
    assert (node2lst(n_a_b) == [1, 2, 3, 4, 5, 6, 7, 8])
    n_a_b = shuffle_merge_recur(n_a, n_b)
    print(node2lst(n_a_b), '==', [1, 2, 3, 4, 5, 6, 7, 8])
    assert (node2lst(n_a_b) == [1, 2, 3, 4, 5, 6, 7, 8])


def sorted_merge(first, second):
    if not first:
        return second
    if not second:
        return first

    node_new = None
    while first or second:
        if not first:
            node.next = second
            return node_new
        if not second:
            node.next = first
            return node_new

        if first.data < second.data:
            if node_new:
                node.next = Node(first.data)
                node = node.next
            else:
                node_new = node = Node(first.data)
            first = first.next
        else:
            if node_new:
                node.next = Node(second.data)
                node = node.next
            else:
                node_new = node = Node(second.data)
            second = second.next

    return node_new


def sorted_merge_recur(first, second):
    if not first:
        return second
    if not second:
        return first
    if first.data < second.data:
        node_new = Node(first.data, sorted_merge_recur(first.next, second))
    else:
        node_new = Node(second.data, sorted_merge_recur(first, second.next))
    return node_new


if __name__ == '__main__':
    print('>>> sorted_merge/sorted_merge_recur')
    data_a_lst = [2, 3, 5, 8]
    data_b_lst = [1, 4, 6, 7]
    n_a = lst2node(data_a_lst)
    n_b = lst2node(data_b_lst)
    n_a_b = sorted_merge(n_a, n_b)
    print(node2lst(n_a_b), '==', [1, 2, 3, 4, 5, 6, 7, 8])
    assert (node2lst(n_a_b) == [1, 2, 3, 4, 5, 6, 7, 8])
    n_a_b = sorted_merge_recur(n_a, n_b)
    print(node2lst(n_a_b), '==', [1, 2, 3, 4, 5, 6, 7, 8])
    assert (node2lst(n_a_b) == [1, 2, 3, 4, 5, 6, 7, 8])


def merge_sort_recur(head):
    if not head:
        return None
    if not head.next:
        return Node(head.data)
    front = Node()
    back = Node()
    front_back_split(head, front, back)
    return sorted_merge(merge_sort_recur(front), merge_sort_recur(back))


if __name__ == '__main__':
    print('>>> merge_sort_recur')
    data_lst = [4, 1, 7, 6, 8, 5, 3, 2]
    n = lst2node(data_lst)
    n = merge_sort_recur(n)
    print(node2lst(n), '==', sorted(data_lst))
    assert (node2lst(n) == sorted(data_lst))


def sorted_intersect(first, second):
    if not first or not second:
        return None
    node_new = node = Node(first.data)
    while first and second:
        if first.data == second.data:
            if node.data != first.data:
                node.next = Node(first.data)
                node = node.next
            first = first.next
            second = second.next
        elif first.data < second.data:
            first = first.next
        else:
            second = second.next
    return node_new


def sorted_intersect_recur(first, second, data=None):
    if not first or not second:
        return None
    if first.data == second.data:
        if not data or first.data != data:
            return Node(first.data, sorted_intersect_recur(first.next, second.next, first.data))
        return sorted_intersect_recur(first.next, second.next, first.data)
    if first.data < second.data:
        return sorted_intersect_recur(first.next, second, data)
    return sorted_intersect_recur(first, second.next, data)


if __name__ == '__main__':
    print('>>> sorted_intersect/sorted_intersect_recur')
    data_a_lst = [1, 1, 2, 3, 4, 5, 5, 5]
    data_b_lst = [1, 1, 4, 4, 5, 6, 7, 7]
    n_a = lst2node(data_a_lst)
    n_b = lst2node(data_b_lst)
    n_a_b = sorted_intersect(n_a, n_b)
    print(node2lst(n_a_b), '==', sorted(set(data_a_lst) & set(data_b_lst)))
    assert (node2lst(n_a_b) == sorted(set(data_a_lst) & set(data_b_lst)))
    n_a = lst2node(data_a_lst)
    n_b = lst2node(data_b_lst)
    n_a_b = sorted_intersect_recur(n_a, n_b)
    print(node2lst(n_a_b), '==', sorted(set(data_a_lst) & set(data_b_lst)))
    assert (node2lst(n_a_b) == sorted(set(data_a_lst) & set(data_b_lst)))


def reverse(head):
    if not head:
        return None
    node = head
    node_new = Node(node.data)
    node = node.next
    while node:
        node_new = Node(node.data, node_new)
        node = node.next
    head.data = node_new.data
    head.next = node_new.next


def reverse_recur(head, next=None):
    if not head:
        return None
    if not head.next:
        return Node(head.data, next)
    return reverse_recur(head.next, Node(head.data, next))


if __name__ == '__main__':
    print('>>> reverse/reverse_recur')
    data_lst = [1, 2, 3, 4, 5, 6]
    n = lst2node(data_lst)
    reverse(n)
    print(node2lst(n), '==', list(reversed(data_lst)))
    assert (node2lst(n) == list(reversed(data_lst)))
    n = lst2node(data_lst)
    n = reverse_recur(n)
    print(node2lst(n), '==', list(reversed(data_lst)))
    assert (node2lst(n) == list(reversed(data_lst)))
