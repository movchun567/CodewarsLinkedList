class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError
    else:
        if dest is None:
            dest = Node(source.data)
            source = source.next
        else:
            dest_next = dest
            dest = Node(source.data)
            dest.next = dest_next
            source = source.next
        return Context(source, dest)