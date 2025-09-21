# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # For odd-length list → slow ends on the true middle.
        # For even-length list → slow ends on the second middle.
        return slow

        """
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        For odd-length list → slow ends on the true middle.
        For even-length list → slow ends on the first middle.
        """
