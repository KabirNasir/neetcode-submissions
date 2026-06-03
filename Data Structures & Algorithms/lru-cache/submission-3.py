class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.ahead = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru = {}         

        self.head = Node()      
        self.tail = Node()       
        self.head.ahead = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            self._remove(node)
            self._add_to_end(node)
            return node.val
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self._remove(self.lru[key])
        elif len(self.lru) == self.cap:
            lru = self.head.ahead
            self._remove(lru)
            del self.lru[lru.key]

        new_node = Node(key, value)
        self._add_to_end(new_node)
        self.lru[key] = new_node
        
    def _remove(self, node) -> None:
        prev = node.prev
        nxt = node.ahead
        prev.ahead = nxt
        nxt.prev = prev
        

    
    def _add_to_end(self,node) -> None:
        prev = self.tail.prev
        prev.ahead = node
        node.prev = prev
        node.ahead = self.tail
        self.tail.prev = node




        
