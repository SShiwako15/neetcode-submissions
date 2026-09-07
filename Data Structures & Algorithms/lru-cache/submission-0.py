class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.prev, self.tail.next = self.tail, self.head

    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 
    
    def insert(self, node) -> None:
        prev, nxt = self.head.prev, self.head
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:    
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lnext = self.tail.next
            self.remove(lnext)
            del self.cache[lnext.key]

