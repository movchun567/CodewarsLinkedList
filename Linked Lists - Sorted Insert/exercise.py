
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f'Node({self.data})'


def sorted_insert(head, data):
    if head is not None:
        curr = head
        while curr:
            if isinstance(curr.next, Node):
                if data >= curr.data and data <= curr.next.data:
                    data = Node(data)
                    data.next = curr.next
                    curr.next = data
                    return head
            elif curr.next is None:
                curr.next = data
                return head
            curr = curr.next
    else:
        return Node(data)

print(sorted_insert(Node(1), 2))