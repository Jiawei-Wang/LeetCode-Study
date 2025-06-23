# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                duplicate_val = head.val
                while head and head.val == duplicate_val:
                    head = head.next
                prev.next = head
            else: # if head.val != head.next.val or not head.next
                prev = prev.next
                head = head.next

        return dummy.next
