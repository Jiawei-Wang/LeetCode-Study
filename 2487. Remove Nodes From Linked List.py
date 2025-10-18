# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# treat it as monotonic decreasing list question
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # turn it into a monotonic decreasing list
        stack = []
        cur = head
        while cur:
            while stack and cur.val > stack[-1]:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next

        # reconstruct the linked list 
        dummy = ListNode()
        cur = dummy
        for n in stack:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next


# reverse the pointers so we can traverse the linked list from end to start
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        head = reverse(head)

        # after the linked list is reversed, we just do it in O(1) space
        current = head
        cur_max = current.val
        while current.next: # the last node (current) will never be removed, so no need to traverse it
            if current.next.val < cur_max:
                current.next = current.next.next # just skip this node
            else:
                cur_max = current.next.val
                current = current.next

        return reverse(head)