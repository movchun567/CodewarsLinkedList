def sorted_insert(head, data):
    if head is not None:
        new = Node(data)
        if head.data >= data:
            new.next = head
            return new
        curr = head
        while curr.next and curr.next.data < data:
            curr = curr.next
        new.next = curr.next
        curr.next = new
        return head
    else:
        return Node(data)