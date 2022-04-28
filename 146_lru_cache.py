class LRUCache:
    class DLinkedList:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
            
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        
        self.head = None
        self.tail = None
    
    def _remove_last_element(self):
        tail = self.tail
        
        prev = self.tail.prev
        prev.next = None
        self.tail.prev = None
        self.tail = prev
        
        return tail
    
    def _remove_node(self, node):
        if self.size == 1 and self.head == node:
            self.head = self.tail = None            
        else:
            if node == self.head:
                prevHead = self.head
                self.head = self.head.next
                self.head.prev = None
                prevHead.next = None
            elif node == self.tail:
                prevTail = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                prevTail.prev = None
            else:
                prev = node.prev
                nxt = node.next

                prev.next = nxt
                nxt.prev = prev
        self.size -= 1
         
    def _add_node(self, node):
        if self.size == 0:
            self.head = self.tail = node
        else:
            prevHead = self.head
            self.head = node
            prevHead.prev = self.head
            self.head.next = prevHead
        self.size += 1
            
    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if not node:
            newNode = self.DLinkedList(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            
            if self.size > self.capacity:
                tail = self._remove_last_element()
                del self.cache[tail.key]
                self.size -=1
        else:
            node.value = value
            self._move_to_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)