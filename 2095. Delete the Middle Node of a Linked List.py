# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: # 1 node
            return None
        if not head.next.next: # 2 nodes
            head.next = None
            return head

        # >= 3 nodes
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = slow.next
        return head
