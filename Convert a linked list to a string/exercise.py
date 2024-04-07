def stringify(node):
    res = []
    curr = node
    if node is not None:
        while True:
            if isinstance(curr.next, Node):
                res.append(str(curr.data))
                curr = curr.next
            else:
                res.append(str(curr.data))
                res.append(str(None))
                break
        return ' -> '.join(res)
    else:
        return 'None'
