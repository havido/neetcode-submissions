class Node:
        def __init__(self, key: int, val: int):
            self.next = None
            self.prev = None
            self.key = key
            self.val = val

class LRUCache:
    # map structure for get
    # doubly linked list structure

    # refactoring: insert (into head of linkedlist), remove (from curr pos in linkedlist)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.node_map = {} # key : val_node

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_node(self, curr: Node): # to head
        nxt = self.head.next
        self.head.next = curr
        curr.next = nxt
        curr.prev = self.head
        nxt.prev = curr

    def remove_node(self, curr: Node):
        prev = curr.prev
        nxt = curr.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        self.remove_node(self.node_map[key])
        self.insert_node(self.node_map[key])
        return self.node_map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.node_map[key].val = value
            self.remove_node(self.node_map[key])
            self.insert_node(self.node_map[key])
        else:
            curr = Node(key, value)
            self.node_map[key] = curr
            self.size += 1
            self.insert_node(curr)
            

        if self.size > self.capacity:
            # evict
            to_evict = self.tail.prev
            del self.node_map[to_evict.key]
            self.remove_node(to_evict)
            self.size -= 1
        
