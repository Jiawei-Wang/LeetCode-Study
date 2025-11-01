# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        array = []
        curr = head
        while curr:
            array.append(curr.val)a
            curr = curr.next
        answer = -float("inf")
        for i in range(0, len(array)//2):
            answer = max(answer, array[i]+array[len(array)-1-i])
        return answer


# O(1) space
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        # Get middle of linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second part of linked list
        curr, prev = slow, None

        while curr:       
            curr.next, prev, curr = prev, curr, curr.next   

        # Get max sum of pairs
        maxVal = 0
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxVal