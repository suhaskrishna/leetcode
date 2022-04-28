# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        
        length = 1
        
        front = back = None
        
        while node:
            if length == k:
                front = node
            node = node.next
            length += 1
        
        idx = length-k-1
        node = head
        while idx > 0:
            node = node.next
            idx -= 1
        
        back = node
        
        front.val, back.val = back.val, front.val
        
        return head
        
        
            