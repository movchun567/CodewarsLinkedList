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