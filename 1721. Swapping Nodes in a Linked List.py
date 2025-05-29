# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, second, current = None, None, head
        while current:
            k -= 1
            if second:
                second = second.next
            if k == 0:
                first = current
                second = head
            current = current.next

        first.val, second.val = second.val, first.val
        return head