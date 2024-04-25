# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        slow.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt


# 2024
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # corner case: linked list is shorter than 2
        if not head or not head.next:
            return
        
        # find middle node
        slow = fast = head
        while fast and fast.next: # (fast = fast.next.next) may go into None, (while fast.next) will throw error 
            temp_end = slow # after last loop, temp_end will point to the node before slow
            slow = slow.next 
            fast = fast.next.next
        temp_end.next = None # break the link between two parts
        """
        for example: 1 -> 2 -> 3 -> 4            slow points to 3, fast points to None
        for example: 1 -> 2 -> 3 -> 4 -> 5       slow points to 3, fast points to 5
        """
        
        # reverse the second half
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge two 
        cur = ListNode(0) # dummy head
        l1, l2 = head, prev
        while l1 and l2:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        # no need to return anything, head still points at the same node