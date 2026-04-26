class Node:
     def __init__(self, val: int, key: int, nxt=None, prev=None):
        self.val = val
        self.key = key
        self.next = nxt
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.head = None
        self.tail = None
        self.length = 0
        self.capacity = capacity 

    def add_to_tail(self, node):
        node.next = None
        if self.head:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            node.prev = None
            self.head = self.tail = node
    def remove(self, node):
        if node.prev:
            if node.next:
                node.next.prev = node.prev 
            else:
                self.tail = node.prev
            node.prev.next = node.next
            node.next = None
            node.prev = None
        elif self.head and self.head.next: 
            self.head = self.head.next
            self.head.prev = None
        else:
            self.tail = self.head = None

    def get(self, key: int) -> int:
        if key not in self.data: return -1
        node = self.data[key]
        self.remove(node)
        self.add_to_tail(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            if node.val != value:
                node.val = value
            self.remove(node)
            self.add_to_tail(node)
        else:
            if self.length+1 > self.capacity:
                self.data.pop(self.head.key)
                self.remove(self.head)
            else:
                self.length += 1
            node = Node(value, key)
            self.data[key] = node
            self.add_to_tail(node)
    
