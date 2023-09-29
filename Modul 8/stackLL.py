class StackLL(object):
    def __init__(self):
        self.top = None
        self.size = 0
        
    def isEmpty(self):
        return self.top is None
    
    def __len__(self):
        return self.size
    
    def peek(self):
        assert not self.isEmpty(), "Tidak bisa diintip. Stack kosong."
        return self.top.item
    
    def pop(self):
        assert not self.isEmpty(), "Tidak bisa pop dari stack kosong."
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item
    
    def push(self, data):
        self.top = _StackNode(data, self.top)
        self.size += 1
        
class _StackNode(object):
    def __init__(self, data, link):
        self.item = data
        self.next = link
        
