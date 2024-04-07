class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
    def __str__(self):
        return f'Node({str(self.data)})'
    def __repr__(self):
        return f'Node({str(self.data)})'

def linked_list_from_string(s):
    if s == "None":
        return None
    s = s.split(" -> ")[:-1]
    head = Node(int(s[0]))
    current = head
    for i in range(1, len(s)):
        current.next = Node(int(s[i]))
        current = current.next
    return head

print(linked_list_from_string("1 -> 2 -> 3 -> 4 -> None"))