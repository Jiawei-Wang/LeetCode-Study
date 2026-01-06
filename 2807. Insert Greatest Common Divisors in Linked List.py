# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        current = head
        while current.next:
            divisor = ListNode(gcd(current.val, current.next.val))
            divisor.next = current.next
            current.next = divisor
            current = divisor.next
        
        return head
