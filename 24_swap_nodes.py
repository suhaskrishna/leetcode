# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if not node:
            return node
        
        if not node.next:
            return node
        
        newHead = None
        while node is not None and node.next is not None:
            nxtNode = node.next
            furtherNext = nxtNode.next
            
            curNode = node
            curNode.next = furtherNext
            
            node = nxtNode
            node.next = curNode
            
            if newHead == None:
                newHead = node
            else:
                prev.next = node
                
            prev = node.next
            node = furtherNext
        
        return newHead
        
            