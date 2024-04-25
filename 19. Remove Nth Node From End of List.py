# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# one pointer two passes
# time n space 1
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length
        ptr, length = head, 0
        while ptr:
            ptr, length = ptr.next, length + 1
            
        # find (length-n)th node
        if length == n : return head.next
        ptr = head
        for i in range(1, length - n):
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head


# two pointers one pass
# time n space 1
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = back = head
        for i in range(n):
            front = front.next # front先走n步
        if not front: return head.next
        while front.next:
            front, back = front.next, back.next # front走到尽头时，back正好走到倒数第n个node
        back.next = back.next.next
        return head


# 2024
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if only one node, return None
        if not head.next:
            return None

        collection = []
        cur = head
        while cur:
            collection.append(cur)
            cur = cur.next
        
        index = len(collection) - n
        if n == 1: # if removing last node
            collection[index-1].next = None
        elif index == 0: # if removing first node
            collection[0].next = None
            head = collection[1]
        else: 
            collection[index-1].next = collection[index+1]
        
        return head


