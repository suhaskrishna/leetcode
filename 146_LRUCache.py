class Node:
    def __init__(self, key):
        self.data = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.head
            
            while node.next is not None:
                if node.data == key:
                    if node.prev is None:
                        self.head = node.next
                        self.head.prev = None
                    else:
                        node.prev.next, node.next.prev = node.next, node.prev
                    break
                node = node.next

            newNode = Node(key)
            curTail = self.tail
            curTail.next = newNode
            newNode.prev = curTail
            self.tail = newNode
            
            val =  self.cache[key]
            return val
        
        return -1

    def put(self, key: int, value: int) -> None:
        self._add(key, value)
        if len(self.cache) > self.capacity:
            leastNode = self.head
            data = leastNode.data
            dic = self.cache
            del self.cache[data]
            nextNode = self.head.next
            self.head = nextNode
            self.head.prev = None
    
    def _add(self, key, value):
        if self.head is None:
            self.head = Node(key)
            self.tail = self.head
            self.cache[key] = value
            return
            
        node = self.head
        
        if key in self.cache:
            while node.next is not None:
                if node.data == key:
                    if node.prev is None:
                        self.head = node.next
                        self.head.prev = None
                    else:
                        node.prev.next, node.next.prev = node.next, node.prev
                    break
                node = node.next
                
        curTail = self.tail
        nextNode = Node(key)
        nextNode.prev = curTail
        curTail.next = nextNode

        self.tail = nextNode
        
        self.cache[key] = value
            
                
        
lRUCache = LRUCache(10)
lRUCache.put(10, 13)
lRUCache.put(3, 17)
lRUCache.put(6, 11)
lRUCache.put(10, 5)
lRUCache.put(9, 10)
print(lRUCache.get(13))
lRUCache.put(2, 19)
print(lRUCache.get(2))
print(lRUCache.get(3))
lRUCache.put(5, 25)
print(lRUCache.get(8))
lRUCache.put(9, 22)
lRUCache.put(5, 5)
lRUCache.put(1, 30)
print(lRUCache.get(11))
lRUCache.put(9, 12)
print(lRUCache.get(7))
print(lRUCache.get(5))
print(lRUCache.get(8))
print(lRUCache.get(9))