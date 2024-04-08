def loop_size(node):
    lst = {}
    while node not in lst:
        lst[node] = len(lst)
        node = node.next
    return len(lst) - lst[node]