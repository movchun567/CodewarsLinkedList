def swap_pairs(head):
    if not head or not head.next:
        return head
    dummy = Node(0)
    dummy.next = head
    current = dummy
    while current.next and current.next.next:
        node1 = current.next
        node2 = current.next.next
        current.next = node2
        node1.next = node2.next
        node2.next = node1
        current = node1
    return dummy.next