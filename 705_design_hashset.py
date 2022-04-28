class MyHashSet:

    def __init__(self):
        self.keyRange = 769
        self.array = [Bucket() for i in range(self.keyRange)]
    
    def _hash(self, key):
        return key%self.keyRange
    
    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.array[idx].insert(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.array[idx].delete(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return self.array[idx].contains(key)

class Node:
    
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        self.root = Node(0)
        
    def insert(self, key):
        if not self.contains(key):
            node = self.root.next
            
            while node and node.next:
                node = node.next
            
            if node == None:
                self.root.next = Node(key)
            else:
                node.next = Node(key)
                node = node.next
    
    def delete(self, key):
        if self.contains(key):
            node = self.root.next
            prev = None
            
            while node:
                if node.value == key:
                    if prev == None:
                        self.root.next = node.next
                        return
                    else:
                        prev.next = node.next
                        return
                prev = node
                node = node.next
    
    def contains(self, value):
        node = self.root.next
        
        while node:
            if node.value == value:
                return True
            node = node.next
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)