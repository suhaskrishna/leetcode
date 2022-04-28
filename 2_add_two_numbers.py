# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        
        res = ListNode(-1)
        resPtr = res
        carry = 0
        
        while n1 and n2:
            val = n1.val + n2.val + carry
            carry = val // 10
            
            resPtr.next = ListNode(val%10)
            resPtr = resPtr.next
            
            n1 = n1.next
            n2 = n2.next
        
        while n1:
            val = n1.val + carry
            carry = val // 10
            
            resPtr.next = ListNode(val%10)
            resPtr = resPtr.next
            
            n1 = n1.next
        
        while n2:
            val = n2.val + carry
            carry = val // 10
            
            resPtr.next = ListNode(val%10)
            resPtr = resPtr.next
            
            n2 = n2.next
        
        if carry > 0:
            resPtr.next = ListNode(carry)
            
        return res.next