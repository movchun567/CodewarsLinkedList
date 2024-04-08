class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    head1 = Node(None)
    head2 = Node(None)
    curr1 = head1
    curr2 = head2
    turn = 1
    curr = head
    while curr:
        if turn == 1:
            curr1.next = curr
            curr1 = curr1.next
        else:
            curr2.next = curr
            curr2 = curr2.next
        turn = 3 - turn
        curr = curr.next
    curr1.next = None
    curr2.next = None
    return Context(head1.next, head2.next)