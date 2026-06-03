class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.lru = {}

    def get(self, key: int) -> int:
        if key in self.lru:
            self.queue.remove(key)
            self.queue.append(key) 
            return self.lru[key]
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.queue:
            self.queue.remove(key)
        elif(len(self.lru) == self.capacity): 
            keytoremove = self.queue.popleft()
            del self.lru[keytoremove]
        self.lru[key] = value
        
        self.queue.append(key)
        
        

        
