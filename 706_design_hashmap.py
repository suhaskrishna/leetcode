class MyHashMap:

    def __init__(self):
        self.key_size = 2069
        self.array = [Bucket() for i in range(self.key_size)]
    
    def _calculate_hash(self, key):
        return key % self.key_size
    
    def put(self, key: int, value: int) -> None:
        keyIdx = self._calculate_hash(key)
        self.array[keyIdx].put(key, value)

    def get(self, key: int) -> int:
        keyIdx = self._calculate_hash(key)
        return self.array[keyIdx].get(key)

    def remove(self, key: int) -> None:
        keyIdx = self._calculate_hash(key)
        self.array[keyIdx].remove(key)
        

class Bucket:
    def __init__(self):
        self.items = []
    
    def put(self, key, value):
        found = False
        for i, kv in enumerate(self.items):
            if kv[0] == key:
                found = True
                self.items[i] = (key, value)
        
        if not found:
            self.items.append((key, value))
    
    def get(self, key):
        found = False
        
        for kv in self.items:
            if kv[0] == key:
                return kv[1]
        
        if not found:
            return -1
    
    def remove(self, key):
        idx = -1
        
        for i, kv in enumerate(self.items):
            if kv[0] == key:
                idx = i
                break
        
        if idx != -1:
            self.items.pop(idx)
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)