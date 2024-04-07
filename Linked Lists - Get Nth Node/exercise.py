def get_nth(node, index):
    probe = node
    len_ = 0
    while probe:
        len_ += 1
        probe = probe.next
    if index >= 0 and index < len_ and node is not None:
        curr = node
        count = 0
        while curr:
            if count == index:
                return(curr)
            count += 1
            curr = curr.next
    else:
        raise TypeError