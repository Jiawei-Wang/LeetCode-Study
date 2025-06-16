# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # turn linked lists into stacks
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        total = 0
        answer = ListNode(0) # dummy node also acts as a carry
        
        # add nodes backward
        while s1 or s2:
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            answer.val = total % 10
            head = ListNode(total // 10)
            head.next = answer
            answer = head
            total //= 10
        
        return answer if answer.val != 0 else answer.next
        