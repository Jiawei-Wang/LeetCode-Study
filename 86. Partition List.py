# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        hd1=p1=ListNode()
        hd2=p2=ListNode()
        while head:
            if head.val<x:
                p1.next=head
                p1=p1.next
            else:
                p2.next=head
                p2=p2.next
            head=head.next

        p2.next=None
        p1.next=hd2.next
        return hd1.next
                